from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import ContentTypes, InputFile, InlineKeyboardMarkup, InlineKeyboardButton

from keyboards.inline import facade_keyboard
from keyboards.inline.facade_keyboard import facade_inline_keyboard
from loader import dp, bot
from states.roof import Roof


@dp.message_handler(text="Кровля")
async def facade_testing_menu(message: types.Message, state: FSMContext):

    data = await state.get_data()

    await message.answer(text="Ответьте на следующие вопросы: ")
    await message.answer(text="Опишите внешний вид: ")




@dp.message_handler(state=Roof)
async def facade_testing_size(message: types.Message, state: FSMContext):

    await message.answer("Отправьте размеры фасада: ")



@dp.message_handler(state=Roof)


@dp.message_handler(state=Roof)
async def facade_testing_thanks(message: types.Message, state: FSMContext):
    pass