<!-- ![anime-road](https://github.com/kamolgks/Weather-Bot/assets/101630621/3436e127-f07e-4fe7-88e9-742e233257c0) -->

<p align="center">
  <a href="https://t.me/weatherv_robot">
    <img src="https://te.legra.ph/file/c47319f50a8a426e1a415.jpg" alt="Photo">
  </a>
</p>

# Weather-Bot

## Описание

Weather-Bot - это чат-бот, предназначенный для предоставления текущей погодной информации. Бот использует API погоды для получения данных о погоде и может предоставлять пользователю актуальные сведения о температуре, влажности, скорости ветра и других метеорологических параметрах.

## Установка

1. Клонировать репозиторий:

```bash
git clone https://github.com/yourusername/Weather-Bot.git
cd Weather-Bot
```

2. Установить зависимости:

```bash
pip install -r requirements.txt
```

3. Получить API ключ для погодного API (OpenWeatherMap) и добавить его в файл (`main.py`):

```python
# main.py
# найдёте в коде, поле api_key

api_key = "your_api_key_here"
```

4. Вставить токен своего бота в (`config.py`):

```python
# config.py
token = "bot token"
```

## Использование

1. Запустить бот:

```bash
python main.py
```

2. Подключиться к чату с ботом.

3. Введите команду чтобы добавить свой город:

```
/weather_sity Moscow 
(можно вводит и на русском)
```

А потом:

```
/weather
```

Бот ответит текущей погодой в Москве.

## Команды

- `/weather_sity <город>`: Сохраняем свой город.
- `/weather`: Получить текущую погоду для указанного города.

## Технологии

- Python
- [Погодное API](http://api.openweathermap.org)

## Лицензия

Этот проект лицензируется по лицензии GNU General Public License v3.0 - подробности см. в файле `LICENSE`.

## Автор

[Kamoliddin Tukhtaboev](https://t.me/kamolgks)

## Вклад

Если вы хотите внести свой вклад в развитие проекта, пожалуйста, создайте запрос на объединение изменений.
