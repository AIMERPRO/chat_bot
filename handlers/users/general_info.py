from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ContentTypes, ReplyKeyboardMarkup, KeyboardButton

from keyboards.default.main_menu import main_menu_keyboard
from keyboards.inline.general_info_inline import general_inline_keyboard, back_keyboard_inline
from loader import dp, bot
from states.menuStates import MenuState


@dp.message_handler(text_contains="Общие сведения", state=MenuState.main_menu)
async def general_info(message: types.Message):
    await message.answer("Начнём опрос по общей информации", reply_markup=types.ReplyKeyboardRemove())
    await message.answer("Все вопросы по общей информации", reply_markup=general_inline_keyboard)

    await MenuState.General_Information.g_inline_keyboard.set()


@dp.callback_query_handler(text="back_general", state="*")
async def back_menu(call: types.CallbackQuery, state: FSMContext):
    await call.answer(cache_time=60)

    await call.message.answer("Все вопросы по общей информации", reply_markup=general_inline_keyboard)

    await call.message.delete()

    await MenuState.General_Information.g_inline_keyboard.set()


@dp.callback_query_handler(text="class_reliability", state=MenuState.General_Information.g_inline_keyboard)
async def general_info(call: types.CallbackQuery):
    await call.answer(cache_time=60)

    await call.message.answer("Введите класс строения по надёжности: ", reply_markup=back_keyboard_inline)

    await call.message.delete()

    await MenuState.General_Information.reliability.set()


@dp.message_handler(state=MenuState.General_Information.reliability)
async def reliability(message: types.Message, state: FSMContext):
    await state.update_data(reliability=message.text)

    await message.answer("Спасибо за ответ", reply_markup=general_inline_keyboard)

    await MenuState.General_Information.g_inline_keyboard.set()


@dp.callback_query_handler(text="purpose_object", state=MenuState.General_Information.g_inline_keyboard)
async def reliability(call: types.CallbackQuery, state: FSMContext):
    await call.answer(cache_time=60)

    await call.message.answer("Назначение объекта")
    await call.message.answer("Это жилое здание со встроенными нежилыми помещениями?", reply_markup=InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="Да", callback_data="purpose_yes"),
                InlineKeyboardButton(text="Нет", callback_data="purpose_no")
            ],
            [
                InlineKeyboardButton(text="Назад в меню", callback_data="back_general")
            ]
        ]
    ))

    await call.message.delete()

    await MenuState.General_Information.purpose.set()


@dp.callback_query_handler(text="purpose_yes", state=MenuState.General_Information.purpose)
async def purpose_yes(call: types.CallbackQuery, state: FSMContext):
    await call.answer(cache_time=60)

    await state.update_data(purpose="Да")

    await call.message.answer("Спасибо за ответ", reply_markup=general_inline_keyboard)

    await MenuState.General_Information.g_inline_keyboard.set()


@dp.callback_query_handler(text="purpose_no", state=MenuState.General_Information.purpose)
async def purpose_yes(call: types.CallbackQuery, state: FSMContext):
    await call.answer(cache_time=60)

    await call.message.answer("Введите назначение: ")

    await MenuState.General_Information.purpose_answer.set()


@dp.message_handler(state=MenuState.General_Information.purpose_answer)
async def durability_degree(message: types.Message, state: FSMContext):
    await message.answer("Спасибо за ответ", reply_markup=general_inline_keyboard)

    await state.update_data(purpose=message.text)

    await MenuState.General_Information.g_inline_keyboard.set()


@dp.callback_query_handler(text="durability_degree", state=MenuState.General_Information.g_inline_keyboard)
async def class_reliability(call: types.CallbackQuery):
    await call.answer(cache_time=60)

    await call.message.answer("Введите Степень долговечности: ", reply_markup=back_keyboard_inline)

    await call.message.delete()

    await MenuState.General_Information.durability_degree.set()


@dp.message_handler(state=MenuState.General_Information.durability_degree)
async def fire_resistance(message: types.Message, state: FSMContext):
    await message.answer("Спасибо за ответ", reply_markup=general_inline_keyboard)

    await state.update_data(durability_degree=message.text)

    await MenuState.General_Information.g_inline_keyboard.set()


@dp.callback_query_handler(text="fire_resistance", state=MenuState.General_Information.g_inline_keyboard)
async def class_reliability(call: types.CallbackQuery):
    await call.answer(cache_time=60)

    await call.message.answer("Введите Степень огнестойкости: ", reply_markup=back_keyboard_inline)

    await call.message.delete()

    await MenuState.General_Information.fire_resistance.set()


@dp.message_handler(state=MenuState.General_Information.fire_resistance)
async def fire_resistance(message: types.Message, state: FSMContext):
    await message.answer("Спасибо за ответ", reply_markup=general_inline_keyboard)

    await state.update_data(durability_degree=message.text)

    await MenuState.General_Information.g_inline_keyboard.set()


@dp.callback_query_handler(text="year_built", state=MenuState.General_Information.g_inline_keyboard)
async def year_built(call: types.CallbackQuery):
    await call.answer(cache_time=60)

    await call.message.answer("Введите Год постройки: ", reply_markup=back_keyboard_inline)

    await call.message.delete()

    await MenuState.General_Information.year_built.set()


@dp.message_handler(state=MenuState.General_Information.year_built)
async def year_built(message: types.Message, state: FSMContext):
    await message.answer("Спасибо за ответ", reply_markup=general_inline_keyboard)

    await state.update_data(year_built=message.text)

    await MenuState.General_Information.g_inline_keyboard.set()


@dp.callback_query_handler(text="class_fire_hazard", state=MenuState.General_Information.g_inline_keyboard)
async def class_fire_hazard(call: types.CallbackQuery):
    await call.answer(cache_time=60)

    await call.message.answer("Введите Класс функциональной пожарной опасности:: ", reply_markup=back_keyboard_inline)

    await call.message.delete()

    await MenuState.General_Information.fire_hazard.set()


@dp.message_handler(state=MenuState.General_Information.fire_hazard)
async def fire_hazard(message: types.Message, state: FSMContext):
    await message.answer("Спасибо за ответ", reply_markup=general_inline_keyboard)

    await state.update_data(year_built=message.text)

    await MenuState.General_Information.g_inline_keyboard.set()


@dp.callback_query_handler(text="have_basement", state=MenuState.General_Information.g_inline_keyboard)
async def have_basement(call: types.CallbackQuery, state: FSMContext):
    await call.answer(cache_time=60)

    await call.message.answer("Есть ли подвал в здании?", reply_markup=InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="Да", callback_data="basement_yes"),
                InlineKeyboardButton(text="Нет", callback_data="basement_no")
            ],
            [
                InlineKeyboardButton(text="Назад в меню", callback_data="back_general")
            ]
        ]
    ))

    await call.message.delete()

    await MenuState.General_Information.Basement.have_basement.set()


@dp.callback_query_handler(text="basement_yes", state=MenuState.General_Information.Basement.have_basement)
async def basement_yes(call: types.CallbackQuery, state: FSMContext):
    await call.answer(cache_time=60)

    await call.message.answer("Над всей площадью здания?", reply_markup=InlineKeyboardMarkup(
        inline_keyboard=[[
            InlineKeyboardButton(text="Да", callback_data="basement_on_full_yes"),
            InlineKeyboardButton(text="Нет", callback_data="basement_on_full_no")
        ]]
    ))

    await MenuState.General_Information.Basement.on_full.set()


@dp.callback_query_handler(text="basement_no", state=MenuState.General_Information.Basement.have_basement)
async def basement_no(call: types.CallbackQuery, state: FSMContext):
    await call.answer(cache_time=60)

    await state.update_data(basement="Нет")

    await call.message.answer(text="Спасибо за ответ", reply_markup=general_inline_keyboard)

    await MenuState.General_Information.g_inline_keyboard.set()


@dp.callback_query_handler(text="basement_on_full_yes", state=MenuState.General_Information.Basement.on_full)
async def basement_yes(call: types.CallbackQuery, state: FSMContext):
    await call.answer(cache_time=60)

    await state.update_data(basement_on_full="Да")

    await call.message.answer("Пометь на плане и сделай фото")

    await MenuState.General_Information.Basement.answer.set()


@dp.callback_query_handler(text="basement_on_full_no", state=MenuState.General_Information.Basement.on_full)
async def basement_yes(call: types.CallbackQuery, state: FSMContext):
    await call.answer(cache_time=60)

    await state.update_data(basement_on_full="Нет")

    await call.message.answer("Пометь на плане и сделай фото")

    await MenuState.General_Information.Basement.answer.set()


@dp.message_handler(content_types=types.ContentTypes.PHOTO, state=MenuState.General_Information.Basement.answer)
async def basement_on_full(message: types.Message):
    photo = await message.photo[-1].download(f"media/photos/{message.from_user.id}_basement_plan.jpg")

    await message.answer(text="Спасибо за ответ", reply_markup=general_inline_keyboard)

    await MenuState.General_Information.g_inline_keyboard.set()


@dp.callback_query_handler(text="have_attic", state=MenuState.General_Information.g_inline_keyboard)
async def attic(call: types.CallbackQuery, state: FSMContext):
    await call.answer(cache_time=60)

    await call.message.answer("Есть ли чердак в здании?", reply_markup=InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="Да", callback_data="attic_yes"),
                InlineKeyboardButton(text="Нет", callback_data="attic_no")
            ],
            [
                InlineKeyboardButton(text="Назад в меню", callback_data="back_general")
            ]
        ]
    ))

    await call.message.delete()

    await MenuState.General_Information.Attic.have_attic.set()


@dp.callback_query_handler(text="attic_yes", state=MenuState.General_Information.Attic.have_attic)
async def attic_yes(call: types.CallbackQuery, state: FSMContext):
    await call.answer(cache_time=60)

    await call.message.answer("Над всей площадью здания?", reply_markup=InlineKeyboardMarkup(
        inline_keyboard=[[
            InlineKeyboardButton(text="Да", callback_data="attic_on_full_yes"),
            InlineKeyboardButton(text="Нет", callback_data="attic_on_full_no")
        ]]
    ))

    await MenuState.General_Information.Attic.on_full.set()


@dp.callback_query_handler(text="attic_no", state=MenuState.General_Information.Attic.have_attic)
async def attic_no(call: types.CallbackQuery, state: FSMContext):
    await call.answer(cache_time=60)

    await state.update_data(attic="Нет")

    await call.message.answer(text="Спасибо за ответ", reply_markup=general_inline_keyboard)

    await MenuState.General_Information.g_inline_keyboard.set()


@dp.callback_query_handler(text="attic_on_full_yes", state=MenuState.General_Information.Attic.on_full)
async def attic_yes(call: types.CallbackQuery, state: FSMContext):
    await call.answer(cache_time=60)

    await state.update_data(attic_on_full="Да")

    await call.message.answer("Пометь на плане и сделай фото")

    await MenuState.General_Information.Attic.answer.set()


@dp.callback_query_handler(text="attic_on_full_no", state=MenuState.General_Information.Attic.on_full)
async def attic_yes(call: types.CallbackQuery, state: FSMContext):
    await call.answer(cache_time=60)

    await state.update_data(attic_on_full="Нет")

    await call.message.answer("Пометь на плане и сделай фото")

    await MenuState.General_Information.Attic.answer.set()


@dp.message_handler(content_types=types.ContentTypes.PHOTO, state=MenuState.General_Information.Attic.answer)
async def attic_on_full(message: types.Message):
    photo = await message.photo[-1].download(f"media/photos/{message.from_user.id}_attic_plan.jpg")

    await message.answer(text="Спасибо за ответ", reply_markup=general_inline_keyboard)

    await MenuState.General_Information.g_inline_keyboard.set()


@dp.callback_query_handler(text="floors_nums", state=MenuState.General_Information.g_inline_keyboard)
async def floors_nums(call: types.CallbackQuery):
    await call.answer(cache_time=60)

    await call.message.answer("Введите Количество этажей с учетом подвала и чердака: ", reply_markup=back_keyboard_inline)

    await call.message.delete()

    await MenuState.General_Information.Number_of_floors.set()


@dp.message_handler(state=MenuState.General_Information.Number_of_floors)
async def Number_of_floors(message: types.Message, state: FSMContext):
    await message.answer("Спасибо за ответ", reply_markup=general_inline_keyboard)

    await state.update_data(floors_nums=message.text)

    await MenuState.General_Information.g_inline_keyboard.set()


@dp.callback_query_handler(text="build_height", state=MenuState.General_Information.g_inline_keyboard)
async def build_height(call: types.CallbackQuery):
    await call.answer(cache_time=60)

    await call.message.answer("Введите Высоту здания: ", reply_markup=back_keyboard_inline)

    await call.message.delete()

    await MenuState.General_Information.building_height.set()


@dp.message_handler(state=MenuState.General_Information.building_height)
async def building_height(message: types.Message, state: FSMContext):
    await message.answer("Спасибо за ответ", reply_markup=general_inline_keyboard)

    await state.update_data(building_height=message.text)

    await MenuState.General_Information.g_inline_keyboard.set()


@dp.callback_query_handler(text="construct_type", state=MenuState.General_Information.g_inline_keyboard)
async def construct_type(call: types.CallbackQuery, state: FSMContext):
    await call.answer(cache_time=60)

    await call.message.answer("Конструктивный тип здания?", reply_markup=InlineKeyboardMarkup(
        inline_keyboard=[[
            InlineKeyboardButton(text="Каркасный", callback_data="carkas"),
            InlineKeyboardButton(text="Бескаркасный", callback_data="not_carkas")
        ]]
    ))

    await call.message.delete()

    await MenuState.General_Information.structural_type.set()


@dp.callback_query_handler(text="carkas", state=MenuState.General_Information.structural_type)
async def carkas(call: types.CallbackQuery, state: FSMContext):
    await call.answer(cache_time=60)

    await state.update_data(carcas="Каркасный")

    await call.message.answer("Спасибо за ответ", reply_markup=general_inline_keyboard)

    await MenuState.General_Information.g_inline_keyboard.set()


@dp.callback_query_handler(text="not_carkas", state=MenuState.General_Information.structural_type)
async def not_carkas(call: types.CallbackQuery, state: FSMContext):
    await call.answer(cache_time=60)

    await state.update_data(carcas="Бескаркасный")

    await call.message.answer("Спасибо за ответ", reply_markup=general_inline_keyboard)

    await MenuState.General_Information.g_inline_keyboard.set()


@dp.callback_query_handler(text="living_S", state=MenuState.General_Information.g_inline_keyboard)
async def living_S(call: types.CallbackQuery):
    await call.answer(cache_time=60)

    await call.message.answer("Введите Площадь (полезная жилая): ", reply_markup=back_keyboard_inline)

    await call.message.delete()

    await MenuState.General_Information.living_space.set()


@dp.message_handler(state=MenuState.General_Information.living_space)
async def living_space(message: types.Message, state: FSMContext):
    await message.answer("Спасибо за ответ", reply_markup=general_inline_keyboard)

    await state.update_data(living_space=message.text)

    await MenuState.General_Information.g_inline_keyboard.set()


@dp.callback_query_handler(text="full_S", state=MenuState.General_Information.g_inline_keyboard)
async def full_S(call: types.CallbackQuery):
    await call.answer(cache_time=60)

    await call.message.answer("Введите Площадь общая: ", reply_markup=back_keyboard_inline)

    await call.message.delete()

    await MenuState.General_Information.total_area.set()


@dp.message_handler(state=MenuState.General_Information.total_area)
async def total_area(message: types.Message, state: FSMContext):
    await message.answer("Спасибо за ответ", reply_markup=general_inline_keyboard)

    await state.update_data(full_space=message.text)

    await MenuState.General_Information.g_inline_keyboard.set()


@dp.callback_query_handler(text="appart_num", state=MenuState.General_Information.g_inline_keyboard)
async def appart_num(call: types.CallbackQuery):
    await call.answer(cache_time=60)

    await call.message.answer("Введите Количество квартир: ", reply_markup=back_keyboard_inline)

    await call.message.delete()

    await MenuState.General_Information.number_of_apartments.set()


@dp.message_handler(state=MenuState.General_Information.number_of_apartments)
async def number_of_apartments(message: types.Message, state: FSMContext):
    await message.answer("Спасибо за ответ", reply_markup=general_inline_keyboard)

    await state.update_data(number_of_apartments=message.text)

    await MenuState.General_Information.g_inline_keyboard.set()


@dp.callback_query_handler(text="section_num", state=MenuState.General_Information.g_inline_keyboard)
async def section_num(call: types.CallbackQuery):
    await call.answer(cache_time=60)

    await call.message.answer("Введите Количество секций: ", reply_markup=back_keyboard_inline)

    await call.message.delete()

    await MenuState.General_Information.number_of_sections.set()


@dp.message_handler(state=MenuState.General_Information.number_of_sections)
async def number_of_sections(message: types.Message, state: FSMContext):
    await message.answer("Спасибо за ответ", reply_markup=general_inline_keyboard)

    await state.update_data(number_of_sections=message.text)

    await MenuState.General_Information.g_inline_keyboard.set()


@dp.callback_query_handler(text="last_cap_year", state=MenuState.General_Information.g_inline_keyboard)
async def last_cap_year(call: types.CallbackQuery):
    await call.answer(cache_time=60)

    await call.message.answer("Введите Год последнего кап. ремонта: (если нет данных пиши прочерк) ", reply_markup=back_keyboard_inline)

    await call.message.delete()

    await MenuState.General_Information.last_major_overhaul.set()


@dp.message_handler(state=MenuState.General_Information.last_major_overhaul)
async def last_major_overhaul(message: types.Message, state: FSMContext):
    await message.answer("Спасибо за ответ", reply_markup=general_inline_keyboard)

    await state.update_data(last_cap_year=message.text)

    await MenuState.General_Information.g_inline_keyboard.set()


@dp.callback_query_handler(text="not_living_S", state=MenuState.General_Information.g_inline_keyboard)
async def not_living_S(call: types.CallbackQuery):
    await call.answer(cache_time=60)

    await call.message.answer("Введите Площадь нежилых помещений: ", reply_markup=back_keyboard_inline)

    await call.message.delete()

    await MenuState.General_Information.Non_residential_area.set()


@dp.message_handler(state=MenuState.General_Information.Non_residential_area)
async def Non_residential_area(message: types.Message, state: FSMContext):
    await message.answer("Спасибо за ответ", reply_markup=general_inline_keyboard)

    await state.update_data(Non_residential_area=message.text)

    await MenuState.General_Information.g_inline_keyboard.set()


@dp.callback_query_handler(text="build_S", state=MenuState.General_Information.g_inline_keyboard)
async def build_S(call: types.CallbackQuery):
    await call.answer(cache_time=60)

    await call.message.answer("Введите Строительный объем: ", reply_markup=back_keyboard_inline)

    await call.message.delete()

    await MenuState.General_Information.building_volume.set()


@dp.message_handler(state=MenuState.General_Information.building_volume)
async def building_volume(message: types.Message, state: FSMContext):
    await message.answer("Спасибо за ответ", reply_markup=general_inline_keyboard)

    await state.update_data(Non_residential_area=message.text)

    await MenuState.General_Information.g_inline_keyboard.set()


@dp.callback_query_handler(text="individual_project", state=MenuState.General_Information.g_inline_keyboard)
async def individual_project(call: types.CallbackQuery, state: FSMContext):
    await call.answer(cache_time=60)

    await call.message.answer("Это индивидуальный проект?", reply_markup=InlineKeyboardMarkup(
        inline_keyboard=[[
            InlineKeyboardButton(text="Да", callback_data="individual_project_yes"),
            InlineKeyboardButton(text="Нет", callback_data="individual_project_no")
        ]]
    ))

    await call.message.delete()

    await MenuState.General_Information.Series.individual_project.set()


@dp.callback_query_handler(text="individual_project_no", state=MenuState.General_Information.Series.individual_project)
async def individual_project_yes(call: types.CallbackQuery, state: FSMContext):
    await call.answer(cache_time=60)

    await state.update_data(individual_project="Нет")

    await call.message.answer("Введи серию/модификацию")

    await MenuState.General_Information.Series.answer.set()


@dp.callback_query_handler(text="individual_project_yes", state=MenuState.General_Information.Series.individual_project)
async def individual_project_yes(call: types.CallbackQuery, state: FSMContext):
    await call.answer(cache_time=60)

    await state.update_data(individual_project="Да")

    await call.message.answer(text="Спасибо за ответ", reply_markup=general_inline_keyboard)

    await MenuState.General_Information.g_inline_keyboard.set()


@dp.message_handler(state=MenuState.General_Information.Series.answer)
async def series_answer(message: types.Message, state: FSMContext):
    await state.update_data(series_answer=message.text)

    await message.answer("Спасибо за ответ", reply_markup=general_inline_keyboard)

    await MenuState.General_Information.g_inline_keyboard.set()


@dp.callback_query_handler(text="have_arendators", state=MenuState.General_Information.g_inline_keyboard)
async def arendator_yes(call: types.CallbackQuery, state: FSMContext):
    await call.answer(cache_time=60)

    await call.message.answer("Наличие арендаторов:", reply_markup=InlineKeyboardMarkup(
        inline_keyboard=[[
            InlineKeyboardButton(text="Да", callback_data="arendator_yes"),
            InlineKeyboardButton(text="Нет", callback_data="arendator_no")
        ]]
    ))

    await call.message.delete()

    await MenuState.General_Information.arendator.set()


@dp.callback_query_handler(text="arendator_yes", state=MenuState.General_Information.arendator)
async def arendator_no(call: types.CallbackQuery, state: FSMContext):
    await call.answer(cache_time=60)

    await state.update_data(arendator="Да")

    await call.message.answer(text="Спасибо за ответ", reply_markup=general_inline_keyboard)

    await MenuState.General_Information.g_inline_keyboard.set()

@dp.callback_query_handler(text="arendator_no", state=MenuState.General_Information.arendator)
async def arendator_no(call: types.CallbackQuery, state: FSMContext):
    await call.answer(cache_time=60)

    await state.update_data(arendator="Нет")

    await call.message.answer(text="Спасибо за ответ", reply_markup=general_inline_keyboard)

    await MenuState.General_Information.g_inline_keyboard.set()


@dp.callback_query_handler(text="culture_obj", state=MenuState.General_Information.g_inline_keyboard)
async def culture_yes(call: types.CallbackQuery, state: FSMContext):
    await call.answer(cache_time=60)

    await state.update_data(culture="Да")

    await call.message.answer("Это объект культурного наследия?: ", reply_markup=InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="Да", callback_data="culture_yes"),
                InlineKeyboardButton(text="Да", callback_data="culture_no"),
            ],
            [
                InlineKeyboardButton(text="Назад в меню", callback_data="back_general")
            ]
        ]
    ))

    await call.message.delete()

    await MenuState.General_Information.culture.set()


@dp.callback_query_handler(text="culture_yes", state=MenuState.General_Information.culture)
async def culture_yes(call: types.CallbackQuery, state: FSMContext):
    await call.answer(cache_time=60)

    await state.update_data(culture="Да")

    await call.message.answer("Введи название объекта: ")

    await MenuState.General_Information.culture_name.set()


@dp.callback_query_handler(text="culture_no", state=MenuState.General_Information.culture)
async def culture_no(call: types.CallbackQuery, state: FSMContext):
    await call.answer(cache_time=60)

    await state.update_data(culture="Нет")

    await call.message.answer("Спасибо за ответ", reply_markup=general_inline_keyboard)

    await MenuState.General_Information.g_inline_keyboard.set()


@dp.message_handler(state=MenuState.General_Information.culture_name)
async def culture_name(message: types.Message, state: FSMContext):
    await state.update_data(culture_name=message.text)

    await message.answer("Какого значения объект?", reply_markup=InlineKeyboardMarkup(
        inline_keyboard=[[
            InlineKeyboardButton(text="Федерального значения", callback_data="federal_status"),
            InlineKeyboardButton(text="Регионального значения", callback_data="regional_status")
        ]]
    ))


@dp.callback_query_handler(text="federal_status", state=MenuState.General_Information.culture_name)
async def federal_status(call: types.CallbackQuery, state: FSMContext):
    await call.answer(cache_time=60)

    await state.update_data(obj_status="Федерального значения")

    await call.message.answer("Переходи к следующему пункту", reply_markup=general_inline_keyboard)

    await MenuState.General_Information.g_inline_keyboard.set()


@dp.callback_query_handler(text="regional_status", state=MenuState.General_Information.culture_name)
async def regional_status(call: types.CallbackQuery, state: FSMContext):
    await call.answer(cache_time=60)

    await state.update_data(obj_status="Регионального значения")

    await call.message.answer("Переходи к следующему пункту", reply_markup=general_inline_keyboard)

    await MenuState.General_Information.g_inline_keyboard.set()


@dp.callback_query_handler(text="back_to_main_menu", state=MenuState.General_Information.g_inline_keyboard)
async def back_to_main_menu(call: types.CallbackQuery):
    await call.answer(cache_time=60)

    await call.message.answer("Возврат в главное меню", reply_markup=main_menu_keyboard)

    await call.message.delete()

    await MenuState.main_menu.set()