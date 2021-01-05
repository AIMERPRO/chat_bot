from aiogram.dispatcher.filters.state import StatesGroup, State


class Roof(StatesGroup):
    appearance = State()  # Внешний вид
    on_the_roof = State()  # Выход на кровлю
    on_the_attic = State()  # выход на чердак
    step_rafters = State()  # шаг стропил
    size_and_pitch_crate = State()  # размер и шаг обрешетки
    number_of_outputs = State()  # количество выходов
    presence_of_insulation = State()  # наличие утеплителя и толщина
    galvanized_thickness = State()  # толщина оцинковки
    rafter_scheme = State()  # схема стропил
    ridge_height = State()  # высота в коньке
    wives = State()  # норожники
    stairs = State()  # лестницы
    humidity = State()  # влажность
    walkways = State()  # ходовые мостки
    leaks = State()  # протечки
    state_of_mauerlat = State()  # состояние мауэрлата
    outer_wall_thickness = State()  # толщина наружной стены
    firewall = State()  # брандмауэр
    