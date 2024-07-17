import logging

from os import getenv
from asyncio import run
from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties
from aiogram.fsm.storage.memory import MemoryStorage

from handlers import handlers
from database.db import Database

from dotenv import load_dotenv

db = Database()
load_dotenv()

async def main():
    storage = MemoryStorage()
    dp = Dispatcher(storage=storage)

    dp.include_router(handlers.router)

    TOKEN = getenv('BOT_TOKEN')
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    try:
        run(main())
    finally:
        db.close()
