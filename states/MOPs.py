from aiogram.dispatcher.filters.state import StatesGroup, State


class MOP(StatesGroup):
    finishing_material = State()  # материал отделки
    stairs_to_the_attic = State()  # лестница на чердак
    description_of_steps = State()  # описание ступеней и их количество, размеры, сколько ступеней с дефектами
    flooring = State()  # напольное покрытие, есть ли дефекты, отметить на плане и описать
    material = State()  # материал
    dimensions = State()  # размеры
    shoe_box = State()  # есть ли галошница

