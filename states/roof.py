from aiogram.dispatcher.filters.state import StatesGroup, State


class Roof(StatesGroup):

    class Roofing(StatesGroup):
        vertical_coverings = State()  # вертикальные покрытия
        roofing_engineering_systems = State()  # Инженерные системы кровельные
        transit_engineering_systems = State()  # Инженерные системы транзитные
        roof_equipment = State()  # Оборудование и надстройки на кровле
        fencing = State()  # Ограждение
        parapet_coverings = State()  # парапетиные покрытия
        ordinary_coverage = State()  # рядовое покрытие
        snow_holders = State()  # снегозадержатели
        wall_architectural = State()  # Стеновые архитектурные элементы
        safety_pipes = State()  # Страховочные трубы
        elimination_of_defects = State()  # сущ. или следы ликвидации дефектов, повреждений, недостатков.
        leaks = State() # существующие или видимые следы протечек, конденсата
        External_and_main_walls = State() # Наружные и капитальные стены

    class Roof_access(StatesGroup):  # Доступ на кровлю
        door = State()  # Дверь
        stairs = State()  # Лестница
        hatch = State()  # Люк

    class UnderRoofing(StatesGroup):
        firewalls = State()  # Брандмауэрные стены
        ventilation = State()  # Вентиляция подкровельного пространства
        internal_walls = State()  # Внутренние стены, перегородки, шахты, вентканалы.
        access_to_attic = State()  # Доступ в чердачное пространство.
        engineering_attic = State()  # Инженерные системы чердачные

        class Transit_engineering(StatesGroup):  # Инженерные системы транзитные
            hot_water_supply = State()  # горячее водоснабжение
            internet = State()  # интернет, связь, телевидение
            fanny_risers = State()  # фанрвые стояки
            cold_water_supply = State()  # холодное водоснабжение
            power_supply = State()  # электроснабжение

        class Rafter_system(StatesGroup):  # Стропильная система
            humidity = State()  # Влажность
            ridge_height = State()  # Высота в коньке
            mauerlat = State()  # гидроизоляция под мауэрлат
            fire_bioprotection = State()  # огнеобиозащита
            rotten_rafters = State()  # отметить гнилые стропила
            size_mauerlat = State()  # размер и состояние мауэрлата
            pitch_crate = State()  # размер и шаг обрешетки
            rafter_scheme = State()  # схема стропил
            walkways = State()  # ходовые мостки
            rafter_pitch = State()  # шаг стропил

        class Warming(StatesGroup):  # Утепление
            attic_floor = State()  # чердачное перекрытие
            mines = State()  # шахт, вентканалов, дымоходов и тд





