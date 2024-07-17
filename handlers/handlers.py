import aiohttp

from os import getenv
from aiogram import Router
from aiogram.filters import Command, CommandStart
from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.fsm.context import FSMContext

from database.db import Database
from states.user_states import WeatherState
from keyboards.keyboard import get_cancel_keyboard
from config.config import city_is_not_set, send_weather, images, welcome_gif, send_welcome

router = Router()
db = Database()

@router.message(CommandStart())
async def send_welcome_message(message: Message):
    await message.answer_video(video=welcome_gif, caption=send_welcome)

@router.message(Command("weather_city"))
async def prompt_for_city(message: Message, state: FSMContext):
    await message.answer("Please enter your city:", reply_markup=get_cancel_keyboard())
    await state.set_state(WeatherState.waiting_for_city)

@router.message(WeatherState.waiting_for_city)
async def process_city_submission(message: Message, state: FSMContext):
    city = message.text

    user_id = message.from_user.id
    username = message.from_user.username
    nickname = message.from_user.first_name

    db.add_user(user_id, username, nickname)
    db.update_user_city(user_id, city)

    if city == "🚫 Cancel":
        await state.clear()
        await message.reply("OK")
    else:
        await message.answer(f"<b>🫶 Your current city</b>: <code>{city}</code>", reply_markup=ReplyKeyboardRemove())
        await state.clear()

@router.message(Command("weather"))
async def send_weather_info(message: Message):
    user_id = message.from_user.id
    city = db.get_user_city(user_id)

    if not city:
        return await message.answer(city_is_not_set)

    api_key = getenv('API_KEY')
    api_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(api_url) as response:
                response.raise_for_status()
                weather_data = await response.json()

        temperature = weather_data["main"]["temp"]
        humidity = weather_data["main"]["humidity"]
        wind_speed = weather_data["wind"]["speed"]
        weather_description = weather_data["weather"][0]["description"]

        temperature_emoji = "🌡" if temperature > 0 else "❄️"
        photo_url = images.get(
            weather_description,
            "https://te.legra.ph/file/a370559984d0da124b97a.jpg",
        )

        await message.answer_photo(
            photo=photo_url,
            caption=send_weather.format(
                city, 
                temperature_emoji,
                temperature,
                humidity,
                wind_speed,
                weather_description,
            ),
        )

    except aiohttp.ClientError:
        await message.answer("<b>🚫 Error retrieving weather data. Please try again later.</b>")