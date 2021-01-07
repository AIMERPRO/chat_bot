from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import ContentTypes, InputFile, InlineKeyboardMarkup, InlineKeyboardButton

from keyboards.default.roof import roof1_keyboard
from keyboards.inline import facade_keyboard
from keyboards.inline.facade_keyboard import facade_inline_keyboard
from loader import dp, bot
from states.roof import Roof


