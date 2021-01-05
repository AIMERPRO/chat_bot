from aiogram.dispatcher import FSMContext
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

facade_inline_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Размеры: ", callback_data="size")
    ],
    [
        InlineKeyboardButton(text="Цвет: ", callback_data="color")
    ],
    [
        InlineKeyboardButton(text="Фотографии: ", callback_data="photo")
    ]
])