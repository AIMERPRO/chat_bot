from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

basement_inline_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Вход в подвал", callback_data="enter_to_basement"),
            InlineKeyboardButton(text="Размеры", callback_data="sizes")
        ],
        [
            InlineKeyboardButton(text="Пол", callback_data="floor"),
            InlineKeyboardButton(text="Стены", callback_data="walls")
        ],
        [
            InlineKeyboardButton(text="Потолок", callback_data="ceiling"),
            InlineKeyboardButton(text="Окна", callback_data="windows")
        ],
        [
            InlineKeyboardButton(text="Освещение", callback_data="lighting"),
            InlineKeyboardButton(text="Водоснабжение", callback_data="water_supply")
        ],
        [
            InlineKeyboardButton(text="Отопление", callback_data="heating"),
            InlineKeyboardButton(text="Канализация", callback_data="canals"),
        ],
        [
            InlineKeyboardButton(text="Назад в главное меню", callback_data="back_to_main_menu"),
        ],
    ]
)


enter_to_basement_inline = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Лестница", callback_data="b_stairs")
        ],
        [
            InlineKeyboardButton(text="Стены", callback_data="b_walls")
        ],
        [
            InlineKeyboardButton(text="Дверь", callback_data="b_door")
        ],
        [
            InlineKeyboardButton(text="Фото", callback_data="b_photo")
        ],
        [
            InlineKeyboardButton(text="Назад в меню", callback_data="back_basement")
        ]
    ]
)


stairs_inline = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Ширина", callback_data="b_width")
        ],
        [
            InlineKeyboardButton(text="Длина", callback_data="b_length")
        ],
        [
            InlineKeyboardButton(text="Ступени", callback_data="b_steps")
        ],
        [
            InlineKeyboardButton(text="Назад в меню", callback_data="back_basement")
        ]
    ]
)


steps_inline = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Размер", callback_data="steps_size")
        ],
        [
            InlineKeyboardButton(text="Материал", callback_data="steps_material")
        ],
        [
            InlineKeyboardButton(text="Отделка", callback_data="steps_finishing")
        ],
        [
            InlineKeyboardButton(text="Назад в меню", callback_data="back_basement")
        ]
    ]
)


walls_inline = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Поручни", callback_data="walls_handrail")
        ],
        [
            InlineKeyboardButton(text="Отделка", callback_data="walls_finishing")
        ],
        [
            InlineKeyboardButton(text="Назад в меню", callback_data="back_basement")
        ]
    ]
)
