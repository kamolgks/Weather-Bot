images = {
    "clear sky": "https://te.legra.ph/file/59fb2206eef46231322fd.jpg",
    "smoke": "https://te.legra.ph/file/fb713f2fc775f2d410150.jpg",
    "scattered clouds": "https://te.legra.ph/file/fb713f2fc775f2d410150.jpg",
    "few clouds": "https://te.legra.ph/file/fb713f2fc775f2d410150.jpg"
}

welcome_gif = "https://x0.at/GfoN.mp4"
send_welcome = """
🪄 <b>Heeey! I am a weather bot. Enter the name of your city.</b>

<b>Enter this command:</b> /weather_city <b>and send the name of your city</b>
<b>Then send this command to view the weather</b>: /weather
"""

city_is_not_set = """
<b>🚫 Default city is not set. Use the command</b> /weather_city <b>city to set a default city.</b>
"""

send_weather = """
<b>❔ Here is the weather in your city</b>:

<pre><code class='language-weather'>🌤 <b>City</b>: {}

{} <b>Temperature:</b> <u>{}°C</u>
💧 <b>Humidity</b>: {}%
💨 <b>Wind speed</b>: {} m/s
☀️ <b>Description:</b> {}</code></pre>
"""
