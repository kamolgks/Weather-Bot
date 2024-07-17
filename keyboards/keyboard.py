from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

def get_cancel_keyboard():
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text="🚫 Cancel"),
            ],
        ],
        one_time_keyboard=True,
        resize_keyboard=True,
    )
    return keyboard