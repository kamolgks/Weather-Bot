<!-- <p align="center">
   <a href="https://t.me/weatherv_robot">
     <img src="https://te.legra.ph/file/c47319f50a8a426e1a415.jpg" alt="bot_img">
   </a>
</p> -->

[![bot_img](https://te.legra.ph/file/c47319f50a8a426e1a415.jpg)](https://t.me/weatherv_robot)

# WeatherBot

## Description

***Weather-Bot is a chatbot designed to provide current weather information. The bot uses the weather API to retrieve weather data and can provide the user with up-to-date information about temperature, humidity, wind speed and other meteorological parameters.***

## Installation

1. Clone the repository:

```sh
git clone https://github.com/kamolgks/Weather-Bot.git && cd Weather-Bot
```

2. Install dependencies:

```sh
pip install -r requirements.txt
```

3. Create a .env file in the root directory of your project and add your weather API ([OpenWeatherMap](http://api.openweathermap.org)) and your bot's token:

```
API_KEY='YOUR_API_KEY'
BOT_TOKEN='YOUR_BOT_TOKEN'
```

## Usage

1. Launch the bot:

- **Linux**
  - ```python3 main.py```

- **Windows**

  - Launch ***"start.bat"***

2. Connect to chat with the bot.

3. Enter the command to add your city:

`/weather_sity `

```

and send name of your city

Tashkent
```

<img src="https://i.imgur.com/MQSUFI1.jpeg" alt="city">

And then:

```
/weather
```

The bot will respond with the current weather in Tashkent.

<img src="https://i.imgur.com/KddA1xS.jpeg" alt="result">

## Teams

- `/weather_sity` -> `City`: Save your city.
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