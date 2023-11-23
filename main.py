# 🔒 Licensed under the GNU GPLv3
# 🌐 https://www.gnu.org/licenses/agpl-3.0.html

import sqlite3

import aiohttp
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
    caption = (
        "🪄 <b>Hello! I am a weather bot. Enter the name of your city.</b>\n\n"
        "<b>Enter the command:</b> <code>/weather_city City</code>\n"
        "<b>Then send this command to view the weather</b>: <code>/weather</code>."
    )
    await message.answer_video(video="https://x0.at/GfoN.mp4", caption=caption)


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
    user_id = message.from_user.id #
    q.execute("SELECT city FROM users WHERE user_id = ?", (user_id,))
    result = q.fetchone()
    city = result[0] if result else None

    if not city:
        return await message.answer("<b>🚫 Default city is not set. Use the command /weather_city [city] to set a default city.</b>")

    api_key = "YOUR_API_KEY"
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

        t_emoji = "🌡" if temperature > 0 else "❄️"

        weather_images = {
            "clear sky": "https://te.legra.ph/file/59fb2206eef46231322fd.jpg",
            "smoke": "https://te.legra.ph/file/fb713f2fc775f2d410150.jpg",
            "scattered clouds": "https://te.legra.ph/file/fb713f2fc775f2d410150.jpg",
            "few clouds": "https://te.legra.ph/file/fb713f2fc775f2d410150.jpg",
        }

        photo_url = weather_images.get(
            weather_description, "https://te.legra.ph/file/a370559984d0da124b97a.jpg")

        caption = (
            f"<b>❔ Here is the weather in your city</b>:\n\n"
            f"🌤 <b>City</b>: <code>{city}</code>\n"
            f"{t_emoji} <b>Temperature: <u>{temperature}°C</u></b>\n"
            f"💧 <b>Humidity</b>: <code>{humidity} %</code>\n"
            f"💨 <b>Wind speed</b>: <code>{wind_speed} m/s</code>\n"
            f"☀️ <b>Description: {weather_description}</b>"
        )
        await message.answer_photo(photo=photo_url, caption=caption)

    except aiohttp.ClientError:
        await message.answer("<b>🚫 Error retrieving weather data. Please try again later.</b>")


@dp.errors_handler()
async def errors_handler(update, exception):
    print(f"Exception has been returned in update {update}. {exception}")


if __name__ == "__main__":
    print("Bot started!\nDeveloper: https://t.me/kamolgks")
    try:
        executor.start_polling(dp, skip_updates=True)
    finally:
        connection.close()
