from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

roof1_keyboard = ReplyKeyboardMarkup([
    [
        KeyboardButton(text="Кровля"),
        KeyboardButton(text="Подкровельное пространство")
    ],
    [
        KeyboardButton(text="Назад")
    ]
], resize_keyboard=True)