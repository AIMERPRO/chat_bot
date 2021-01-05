from aiogram.dispatcher.filters.state import StatesGroup, State


class MOP(StatesGroup):
    finishing_material = State()  # материал отделки