# 🔒 Licensed under the GNU GPLv3
# 🌐 https://www.gnu.org/licenses/agpl-3.0.html

import sqlite3
import aiohttp
import asyncio

from os import getenv
from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.filters import Command, CommandStart, CommandObject
from aiogram.types import Message
from aiogram.enums import ParseMode

storage = MemoryStorage()

dp = Dispatcher(storage=storage)
connection = sqlite3.connect("data.db")
q = connection.cursor()


q.execute("""CREATE TABLE IF NOT EXISTS users (
                user_id INTEGER PRIMARY KEY,
                username TEXT,
                nickname TEXT,
                city TEXT
            )""")
connection.commit()


@dp.message(CommandStart())
async def start(message: Message):
    caption = (
        "🪄 <b>Hello! I am a weather bot. Enter the name of your city.</b>\n\n"
        "<b>Enter the command:</b> <code>/weather_city City</code>\n"
        "<b>Then send this command to view the weather</b>: <code>/weather</code>."
    )
    await message.answer_video(
        video="https://x0.at/GfoN.mp4", 
        caption=caption,
    )


@dp.message(Command("weather_city"))
async def weather_city(message: Message, command: CommandObject):
    args = command.args
    city = args.strip()

    if not city:
        return await message.answer("<b>🚫 U didn't specify a city in the command. Here is an example of how to do it: <code>/weather_city Tashkent</code></b>")

    user_id = message.from_user.id
    username = message.from_user.username
    nickname = message.from_user.first_name

    q.execute("INSERT OR IGNORE INTO users (user_id, username, nickname) VALUES (?, ?, ?)", (user_id, username, nickname))
    q.execute("UPDATE users SET city = ? WHERE user_id = ?", (city, user_id))
    connection.commit()

    await message.answer(f"<b> 🫶 Ur current city</b>: <code>{city}</code>")


@dp.message(Command("weather"))
async def weather(message: Message):
    user_id = message.from_user.id 
    q.execute("SELECT city FROM users WHERE user_id = ?", (user_id,))
    result = q.fetchone()
    city = result[0] if result else None

    if not city:
        return await message.answer("<b>🚫 Default city is not set. Use the command /weather_city [city] to set a default city.</b>")

    api_key = "your_api_key"
    units = "metric"
    api_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units={units}"

    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(api_url) as response:
                response.raise_for_status()
                weather_data = await response.json()

        temperature = weather_data["main"]["temp"]
        humidity = weather_data["main"]["humidity"]
        wind_speed = weather_data["wind"]["speed"]
        weather_description = weather_data["weather"][0]["description"]

        t_emoji = "🌡" if temperature > 0 else "❄️"

        weather_img = {
            "clear sky": "https://te.legra.ph/file/59fb2206eef46231322fd.jpg",
            "smoke": "https://te.legra.ph/file/fb713f2fc775f2d410150.jpg",
            "scattered clouds": "https://te.legra.ph/file/fb713f2fc775f2d410150.jpg",
            "few clouds": "https://te.legra.ph/file/fb713f2fc775f2d410150.jpg",
        }
        
        photo_url = weather_img.get(weather_description, "https://te.legra.ph/file/a370559984d0da124b97a.jpg")
        caption = (
            "<b>❔ Here is the weather in your city</b>:\n\n"
            f"<pre><code class='language-weather'>🌤 <b>City</b>: {city}\n"
            f"{t_emoji} <b>Temperature:</b> <u>{temperature}°C</u>\n"
            f"💧 <b>Humidity</b>: {humidity}%\n"
            f"💨 <b>Wind speed</b>: {wind_speed} m/s\n"
            f"☀️ <b>Description:</b> {weather_description}</code></pre>\n"
        )
        await message.answer_photo(photo=photo_url, caption=caption)

    except aiohttp.ClientError:
        await message.answer("<b>🚫 Error retrieving weather data. Please try again later.</b>")


async def main():
    TOKEN = getenv("BOT_TOKEN", "your_bot_token")
    bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
    await dp.start_polling(bot)


if __name__ == "__main__":
    print("Bot started!\nDeveloper: Kamolgks")
    try:
        asyncio.run(main())
    finally:
        connection.close()
