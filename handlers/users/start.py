from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import CommandStart

from keyboards.default.main_menu import main_menu_keyboard
from loader import dp
from states.menuStates import MenuState


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(text=f'Привет, {message.from_user.full_name}!, введи название своей компании')
    await MenuState.nameOfYourCompany.set()


@dp.message_handler(state=MenuState.nameOfYourCompany)
async def name_comp(message: types.Message, state: FSMContext):
    await message.answer("Спасибо за ответ, теперь введи адрес объекта")
    await state.update_data(name_company=message.text)
    await MenuState.address.set()


@dp.message_handler(state=MenuState.address)
async def address(message: types.Message, state:FSMContext):
    await message.answer("Теперь можем продолжать", reply_markup=main_menu_keyboard)
    await state.update_data(address=message.text)
