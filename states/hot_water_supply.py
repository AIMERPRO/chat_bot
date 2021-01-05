from aiogram.dispatcher.filters.state import StatesGroup, State


class HotWaterSupply(StatesGroup):
    highways = State()  # есть ли магистрали
    mark_the_risers = State()  # отметить стояки на плане
    measure_diameters = State()  # замерить диаметры
    description_of_the_insulation = State()  # осмотр и описание утеплителя
    shut_off_valves = State()  # запорная арматура
    downhills = State()  # спускники
    mark_highways = State()  # отметить магистрали на плане
