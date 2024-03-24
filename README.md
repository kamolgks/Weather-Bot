<p align="center">
   <a href="https://t.me/weatherv_robot">
     <img src="https://te.legra.ph/file/c47319f50a8a426e1a415.jpg" alt="bot">
   </a>
</p>

# WeatherBot

## Description

Weather-Bot is a chatbot designed to provide current weather information. The bot uses the weather API to retrieve weather data and can provide the user with up-to-date information about temperature, humidity, wind speed and other meteorological parameters.

## Installation

1. Clone the repository:

```bash
git clone https://github.com/kamolgks/Weather-Bot.git && cd Weather-Bot
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Get the API key for the weather API (OpenWeatherMap) and add it to the file (`main.py`):

```python
# main.py
# you will find in the code, the api_key field

api_key = "your_api_key"
```

4. Insert your bot token into (`main.py`):

```python
# main.py
TOKEN = getenv("BOT_TOKEN", "YOUR_BOT_TOKEN")
```

## Usage

1. Launch the bot:

```bash
python3 main.py
```

2. Connect to chat with the bot.

3. Enter the command to add your city:

```
/weather_sity Tashkent
(can also be entered in Russian)
```

<img src="https://i.imgur.com/Aoeu5Pj.jpeg" alt="city">

And then:

```
/weather
```

The bot will respond with the current weather in Tashkent.

<img src="https://i.imgur.com/SfXRaA3.jpeg" alt="result">

## Teams

- `/weather_sity <city>`: Save your city.
- `/weather`: Get the current weather for the specified city.

## Technologies

- Python
- Aiogram 
- [Weather API](http://api.openweathermap.org)

## License

This project is licensed under the GNU General Public License v3.0 - see the `LICENSE` file for details.

## Author

[Kamoliddin Tukhtaboev](https://t.me/kamolgks)

## Contribution

If you would like to contribute to the development of the bot, please create a merge request.