from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton

main_menu_keyboard = ReplyKeyboardMarkup(
    [
        [
            KeyboardButton(text="Общие сведения"),
            KeyboardButton(text="Несущие элементы"),
            KeyboardButton(text="Состояние здания")
        ],
        [
            KeyboardButton(text="Благоустройство"),
            KeyboardButton(text="Наружная отделка"),
        ],
        [
            KeyboardButton(text="Отправить документ 💾")
        ]
    ],
    resize_keyboard=True
)

