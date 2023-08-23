# developer: https://t.me/kamolgks

import sqlite3

import requests
from aiogram import Bot, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import Dispatcher

storage = MemoryStorage()
bot = Bot(token="TOKEN", parse_mode="HTML")
dp = Dispatcher(bot, storage=storage)
connection = sqlite3.connect("data.db")
q = connection.cursor()

q.execute("""CREATE TABLE IF NOT EXISTS users (
                    user_id INTEGER PRIMARY KEY,
                    username TEXT,
                    nickname TEXT,
                    city TEXT
                )""")
connection.commit()


@dp.message_handler(commands=["start"])
async def start_cmd(message: types.Message):
    await message.answer_video(
        video="https://x0.at/GfoN.mp4",
        caption="🪄 <b>Hello! I am a weather bot. Enter the name of your city.</b>\n\n<b>Enter the command:</b> <code>/weather_city City</code>\n\n<b>Then send this command to view the weather</b>: <code>/weather</code>.",
    )


@dp.message_handler(commands=["weather_city"])
async def weathercity_cmd(message: types.Message):
    args = message.get_args()
    city = args.strip()

    if not city:
        return await message.answer("<b>🚫 U didn't specify a city in the command. Here is an example of how to do it: <code>/weather_city Tashkent</code></b>")

    user_id = message.from_user.id
    username = message.from_user.username
    nickname = message.from_user.first_name

    q.execute("INSERT OR IGNORE INTO users (user_id, username, nickname) VALUES (?, ?, ?)",
              (user_id, username, nickname))
    q.execute("UPDATE users SET city = ? WHERE user_id = ?", (city, user_id))
    connection.commit()

    await message.answer(f"<b> 🫶 Ur current city</b>: <code>{city}</code>")


@dp.message_handler(commands=["weather"])
async def weather_cmd(message: types.Message):
    user_id = message.from_user.id
    q.execute("SELECT city FROM users WHERE user_id = ?", (user_id, ))
    result = q.fetchone()
    city = result[0] if result else None

    if not city:
        return await message.answer("<b>🚫 Default city is not set. Use the command /weather_city [city] to set a default city.</b>")

    api_key = "" # api.openweathermap.org token
    units = "metric"
    api_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units={units}"
    response = requests.get(api_url)
    weather_data = response.json()

    if response.status_code != 200:
        return await message.answer("<b>🚫 Error retrieving weather data. Please try again later.</b>")

    temperature = weather_data["main"]["temp"]
    humidity = weather_data["main"]["humidity"]
    wind_speed = weather_data["wind"]["speed"]
    weather_description = weather_data["weather"][0]["description"]

    if temperature > 0:
        t_emoji = "🌡"
    elif temperature <= 0:
        t_emoji = "❄️"

    await message.answer_video(
        video="https://x0.at/OV-J.mp4",
        caption=f"<b>❔ Here is the weather in your city</b>:\n\n🌤 <b>City</b>: <code>{city}</code>\n{t_emoji} <b>Temperature: <u>{temperature}°C</u></b>\n💧 <b>Humidity</b>: <code>{humidity} %</code>\n💨 <b>Wind speed</b>: <code>{wind_speed} m/s</code>\n☀️ <b>Description: {weather_description}</b>",
    )


if __name__ == "__main__":
    print("Bot started!\nDeveloper: https://t.me/kamolgks")
    try:
        executor.start_polling(dp, skip_updates=True)
    finally:
        connection.close()
