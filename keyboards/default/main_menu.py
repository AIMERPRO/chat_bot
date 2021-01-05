from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton

main_menu_keyboard = ReplyKeyboardMarkup(
    [
        [
            KeyboardButton(text="Фасад"),
            KeyboardButton(text="Кровля"),
            KeyboardButton(text="Окна")
        ],
        [
            KeyboardButton(text="Трубы"),
            KeyboardButton(text="Электрика"),
            KeyboardButton(text="Отопление"),
        ],
        [
            KeyboardButton(text="Отправить документ 💾 13%")
        ]
    ],
    resize_keyboard=True
)