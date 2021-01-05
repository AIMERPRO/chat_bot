from aiogram.dispatcher.filters.state import StatesGroup, State


class PlywoodRisers(StatesGroup):
    mark_on_the_plan = State()  # отметить на плане
    highways_and_risers = State()  # отметить на плане магистрали и стояки
    shut_off_valves = State()  # запорная арматура
    how_pass = State()  # как проходят через перекрытия
    condition = State()  # состояние
    