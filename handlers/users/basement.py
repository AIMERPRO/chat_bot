from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from keyboards.default.main_menu import main_menu_keyboard
from keyboards.inline.basement_inline import basement_inline_keyboard, enter_to_basement_inline, stairs_inline, \
    steps_inline
from loader import dp
from states.menuStates import MenuState


@dp.message_handler(text_contains="Подвал", state=MenuState.main_menu)
async def basement_menu(message: types.Message, state: FSMContext):
    await message.answer("Опрос по подвалу", reply_markup=types.ReplyKeyboardRemove())
    await message.answer("Все вопросы по подвалу", reply_markup=basement_inline_keyboard)

    await MenuState.Basement.b_keyboard_inline.set()


@dp.callback_query_handler(text="back_basement", state="*")
async def back_basement(call: types.CallbackQuery, state: FSMContext):
    await call.answer(cache_time=60)

    await call.message.answer("Опрос по подвалу", reply_markup=basement_inline_keyboard)

    await call.message.delete()

    await MenuState.Basement.b_keyboard_inline.set()


@dp.callback_query_handler(text="back_to_main_menu", state=MenuState.Basement.b_keyboard_inline)
async def back_to_main_menu(call: types.CallbackQuery, state: FSMContext):
    await call.answer(cache_time=60)

    await call.message.answer(text="Главное меню", reply_markup=main_menu_keyboard)

    await call.message.delete()

    await MenuState.main_menu.set()


@dp.callback_query_handler(text="enter_to_basement", state=MenuState.Basement.b_keyboard_inline)
async def enter_to_basement(call: types.CallbackQuery, state: FSMContext):
    await call.answer(cache_time=60)

    await call.message.answer(text="Вход в подвал", reply_markup=enter_to_basement_inline)

    await call.message.delete()

    await MenuState.Basement.EnterToBasement.enter_to_basement_inline.set()


@dp.callback_query_handler(text="b_stairs", state=MenuState.Basement.EnterToBasement.enter_to_basement_inline)
async def b_stairs(call: types.CallbackQuery, state: FSMContext):
    await call.answer(cache_time=60)

    await call.message.answer(text="Лестница", reply_markup=stairs_inline)

    await call.message.delete()

    await MenuState.Basement.EnterToBasement.Stairs.stairs_inline.set()


@dp.callback_query_handler(text="b_width", state=MenuState.Basement.EnterToBasement.Stairs.stairs_inline)
async def b_width(call: types.CallbackQuery, state: FSMContext):
    await call.answer(cache_time=60)

    await call.message.answer(text="Введи ширину")

    await call.message.delete()

    await MenuState.Basement.EnterToBasement.Stairs.width.set()


@dp.message_handler(state=MenuState.Basement.EnterToBasement.Stairs.width)
async def b_width(message: types.Message, state: FSMContext):
    await state.update_data(stairs_width=message.text)

    await message.answer("Спасибо за ответ", reply_markup=stairs_inline)

    await MenuState.Basement.EnterToBasement.Stairs.stairs_inline.set()


@dp.callback_query_handler(text="b_length", state=MenuState.Basement.EnterToBasement.Stairs.stairs_inline)
async def b_length(call: types.CallbackQuery, state: FSMContext):
    await call.answer(cache_time=60)

    await call.message.answer(text="Введи длинну")

    await call.message.delete()

    await MenuState.Basement.EnterToBasement.Stairs.length.set()


@dp.message_handler(state=MenuState.Basement.EnterToBasement.Stairs.length)
async def b_length(message: types.Message, state: FSMContext):
    await state.update_data(stairs_lenght=message.text)

    await message.answer("Спасибо за ответ", reply_markup=stairs_inline)

    await MenuState.Basement.EnterToBasement.Stairs.stairs_inline.set()


@dp.callback_query_handler(text="b_steps", state=MenuState.Basement.EnterToBasement.Stairs.stairs_inline)
async def b_steps(call: types.CallbackQuery, state: FSMContext):
    await call.answer(cache_time=60)

    await call.message.answer("Ступени", reply_markup=steps_inline)

    await call.message.delete()

    await MenuState.Basement.EnterToBasement.Stairs.Steps.steps_inline.set()


@dp.callback_query_handler(text="steps_size", state=MenuState.Basement.EnterToBasement.Stairs.Steps.steps_inline)
async def b_steps(call: types.CallbackQuery, state: FSMContext):
    await call.answer(cache_time=60)

    await call.message.answer("Введи ширину")

    await call.message.delete()

    await MenuState.Basement.EnterToBasement.Stairs.Steps.width.set()


@dp.message_handler(state=MenuState.Basement.EnterToBasement.Stairs.Steps.width)
async def b_length(message: types.Message, state: FSMContext):
    await state.update_data(steps_width=message.text)

    await message.answer("Спасибо за ответ, теперь введи высоту")

    await MenuState.Basement.EnterToBasement.Stairs.Steps.height.set()


@dp.message_handler(state=MenuState.Basement.EnterToBasement.Stairs.Steps.height)
async def b_length(message: types.Message, state: FSMContext):
    await state.update_data(steps_height=message.text)

    await message.answer("Спасибо за ответ", reply_markup=steps_inline)

    await MenuState.Basement.EnterToBasement.Stairs.Steps.steps_inline.set()


@dp.callback_query_handler(text="steps_material", state=MenuState.Basement.EnterToBasement.Stairs.Steps.steps_inline)
async def b_steps(call: types.CallbackQuery, state: FSMContext):
    await call.answer(cache_time=60)

    await call.message.answer("Укажи материал", reply_markup=InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="Бетон", callback_data="steps_material_beton")
            ],
            [
                InlineKeyboardButton(text="Дерево", callback_data="steps_material_tree")
            ],
            [
                InlineKeyboardButton(text="Другое", callback_data="steps_material_another")
            ]
        ]
    ))

    await call.message.delete()

    await MenuState.Basement.EnterToBasement.Stairs.Steps.material.set()


@dp.callback_query_handler(text="steps_material_beton", state=MenuState.Basement.EnterToBasement.Stairs.Steps.material)
async def steps_material(call: types.CallbackQuery, state: FSMContext):
    await call.answer(cache_time=60)

    await state.update_data(steps_material="Бетон")

    await call.message.answer("Спасибо за ответ", reply_markup=steps_inline)

    await call.message.delete()

    await MenuState.Basement.EnterToBasement.Stairs.Steps.steps_inline.set()


@dp.callback_query_handler(text="steps_material_tree", state=MenuState.Basement.EnterToBasement.Stairs.Steps.material)
async def steps_material(call: types.CallbackQuery, state: FSMContext):
    await call.answer(cache_time=60)

    await state.update_data(steps_material="Дерево")

    await call.message.answer("Спасибо за ответ", reply_markup=steps_inline)

    await call.message.delete()

    await MenuState.Basement.EnterToBasement.Stairs.Steps.steps_inline.set()


@dp.callback_query_handler(text="steps_material_another", state=MenuState.Basement.EnterToBasement.Stairs.Steps.material)
async def steps_material(call: types.CallbackQuery, state: FSMContext):
    await call.answer(cache_time=60)

    await call.message.answer("Введи материал: ")

    await call.message.delete()

    await MenuState.Basement.EnterToBasement.Stairs.Steps.material_answer.set()


@dp.message_handler(state=MenuState.Basement.EnterToBasement.Stairs.Steps.material_answer)
async def steps_material(message: types.Message, state: FSMContext):
    await state.update_data(steps_material=message.text)

    await message.answer("Спасибо за ответ", reply_markup=steps_inline)

    await MenuState.Basement.EnterToBasement.Stairs.Steps.steps_inline.set()


@dp.callback_query_handler(text="steps_finishing", state=MenuState.Basement.EnterToBasement.Stairs.Steps.steps_inline)
async def steps_finishing(call: types.CallbackQuery, state: FSMContext):
    await call.answer(cache_time=60)

    await call.message.answer("Укажи материал", reply_markup=InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="Плитка", callback_data="finishing_material_tile")
            ],
            [
                InlineKeyboardButton(text="Бетон", callback_data="finishing_material_beton")
            ],
            [
                InlineKeyboardButton(text="Мозаичный бетон", callback_data="finishing_material_mozaic")
            ],
            [
                InlineKeyboardButton(text="Другое", callback_data="finishing_material_another")
            ]
        ]
    ))

    await call.message.delete()

    await MenuState.Basement.EnterToBasement.Stairs.Steps.finishing.set()


@dp.callback_query_handler(text="finishing_material_beton", state=MenuState.Basement.EnterToBasement.Stairs.Steps.finishing)
async def finishing_material(call: types.CallbackQuery, state: FSMContext):
    await call.answer(cache_time=60)

    await state.update_data(finishing_material="Бетон")

    await call.message.answer("Спасибо за ответ", reply_markup=steps_inline)

    await call.message.delete()

    await MenuState.Basement.EnterToBasement.Stairs.Steps.steps_inline.set()


@dp.callback_query_handler(text="finishing_material_tile", state=MenuState.Basement.EnterToBasement.Stairs.Steps.finishing)
async def finishing_material(call: types.CallbackQuery, state: FSMContext):
    await call.answer(cache_time=60)

    await state.update_data(finishing_material="Плитка")

    await call.message.answer("Укажи размер плитки")

    await call.message.delete()

    await MenuState.Basement.EnterToBasement.Stairs.Steps.tile_answer.set()


@dp.callback_query_handler(text="finishing_material_mozaic", state=MenuState.Basement.EnterToBasement.Stairs.Steps.finishing)
async def finishing_material(call: types.CallbackQuery, state: FSMContext):
    await call.answer(cache_time=60)

    await state.update_data(finishing_material="Мозаичный бетон")

    await call.message.answer("Спасибо за ответ", reply_markup=steps_inline)

    await call.message.delete()

    await MenuState.Basement.EnterToBasement.Stairs.Steps.steps_inline.set()


@dp.callback_query_handler(text="finishing_material_another", state=MenuState.Basement.EnterToBasement.Stairs.Steps.finishing)
async def finishing_material(call: types.CallbackQuery, state: FSMContext):
    await call.answer(cache_time=60)

    await call.message.answer("Введи материал: ")

    await call.message.delete()

    await MenuState.Basement.EnterToBasement.Stairs.Steps.finishing_answer.set()


@dp.message_handler(state=MenuState.Basement.EnterToBasement.Stairs.Steps.finishing_answer)
async def finishing_material(message: types.Message, state: FSMContext):
    await state.update_data(finishing_material=message.text)

    await message.answer("Спасибо за ответ", reply_markup=steps_inline)

    await MenuState.Basement.EnterToBasement.Stairs.Steps.steps_inline.set()


@dp.message_handler(state=MenuState.Basement.EnterToBasement.Stairs.Steps.tile_answer)
async def steps_material(message: types.Message, state: FSMContext):
    await state.update_data(finishing_tile=message.text)

    await message.answer("Спасибо за ответ", reply_markup=steps_inline)

    await MenuState.Basement.EnterToBasement.Stairs.Steps.steps_inline.set()


@dp.callback_query_handler(text="b_walls", state=MenuState.Basement.EnterToBasement.enter_to_basement_inline)
async def b_stairs(call: types.CallbackQuery, state: FSMContext):
    await call.answer(cache_time=60)

    await call.message.answer(text="Стены", reply_markup=stairs_inline)

    await call.message.delete()

    await MenuState.Basement.EnterToBasement.Stairs.stairs_inline.set()
