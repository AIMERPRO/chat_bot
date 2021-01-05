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
    outdoor_temperature = State()  # температура наружного воздуха
    attic_temperature = State()  # температура чердака
    the_rotten_rafters = State()  # отметить гнилые стропила
    roof_width = State()  # ширина кровли
    roof_length = State()  # длина кровли
    weather_vane = State()  # флюгарки
    condition_of_the_top = State() # состояние верхней поверхности оцинковки
    condition_of_brick = State()  # состояние кирпичных или других вентшахт
    superstructures_on_the_roof = State()  # есть ли надстройки на кровле
    communications_the_attic = State()  # какие коммуникации идут по чердаку



class MineInsulation(StatesGroup):  # утепление шахт
    pass



class FireFall(StatesGroup):  # брандмауэр
    pass
