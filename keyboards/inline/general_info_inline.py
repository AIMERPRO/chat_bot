from aiogram.dispatcher import FSMContext
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

general_inline_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text=f"Класс строения по надежности: ", callback_data="class_reliability")
    ],
    [
        InlineKeyboardButton(text="Назначение объекта: ", callback_data="purpose_object")
    ],
    [
        InlineKeyboardButton(text="Степень долговечности: ", callback_data="durability_degree")
    ],
    [
        InlineKeyboardButton(text="Степень огнестойкости: ", callback_data="fire_resistance")
    ],
    [
        InlineKeyboardButton(text="Год постройки: ", callback_data="year_built")
    ],
    [
        InlineKeyboardButton(text="Класс функциональной пожарной опасности: ", callback_data="class_fire_hazard")
    ],
    [
        InlineKeyboardButton(text="Есть ли подвал?: ", callback_data="have_basement")
    ],
    [
        InlineKeyboardButton(text="Есть ли чердак?: ", callback_data="have_attic")
    ],
    [
        InlineKeyboardButton(text="Количество этажей с учетом подвала и чердака: ", callback_data="floors_nums")
    ],
    [
        InlineKeyboardButton(text="Высота здания: ", callback_data="build_height")
    ],
    [
        InlineKeyboardButton(text="Конструктивный тип здания: ", callback_data="construct_type")
    ],
    [
        InlineKeyboardButton(text="Площадь (полезная жилая): ", callback_data="living_S")
    ],
    [
        InlineKeyboardButton(text="Площадь общая: ", callback_data="full_S")
    ],
    [
        InlineKeyboardButton(text="Количество квартир: ", callback_data="appart_num")
    ],
    [
        InlineKeyboardButton(text="Количество секций: ", callback_data="section_num")
    ],
    [
        InlineKeyboardButton(text="Год последнего кап. ремонта: ", callback_data="last_cap_year")
    ],
    [
        InlineKeyboardButton(text="Площадь нежилых помещений: ", callback_data="not_living_S")
    ],
    [
        InlineKeyboardButton(text="Строительный объем: ", callback_data="build_S")
    ],
    [
        InlineKeyboardButton(text="Индивидуальный проект: ", callback_data="individual_project")
    ],
    [
        InlineKeyboardButton(text="Наличие арендаторов: ", callback_data="have_arendators")
    ],
    [
        InlineKeyboardButton(text="Это объект культурного наследия?: ", callback_data="culture_obj")
    ],
    [
        InlineKeyboardButton(text="Назад в главное меню: ", callback_data="back_to_main_menu")
    ]
])


back_keyboard_inline = InlineKeyboardMarkup(
    inline_keyboard=[[
        InlineKeyboardButton(text="Назад в меню", callback_data="back_general")
    ]]
)
