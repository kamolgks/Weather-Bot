from aiogram.fsm.state import State, StatesGroup

class WeatherState(StatesGroup):
    waiting_for_city = State()
