from aiogram.dispatcher.filters.state import StatesGroup, State


class MenuState(StatesGroup):
    nameOfYourCompany = State()
    address = State()
    main_menu = State()

    class General_Information(StatesGroup):
        g_inline_keyboard = State()

        reliability = State()  # Класс строения по надёжности
        durability_degree = State()  # Степень долговечности
        fire_resistance = State()  # Степень огнестойкости
        year_built = State()  # Год постройки
        fire_hazard = State()  # Класс функциональной пожарной опасности
        Number_of_floors = State()  # Количество этажей с учетом подвала и чердака
        building_height = State()  # Высота здания
        structural_type = State()  # структурный тип
        living_space = State()  # полезная площадь
        total_area = State()  # общая площадь
        number_of_apartments = State()  # Количество квартир
        number_of_sections = State()  # Количество секций
        Non_residential_area = State()  # Площадь нежилых помещений
        Non_residential_area_answer = State()  # Ввести вручную
        building_volume = State()  # Строительный объем
        last_major_overhaul = State()  # Последний кап.ремонт
        tenants = State()  # Наличие арендаторов
        purpose = State()  # Введите назначение
        purpose_answer = State()
        arendator = State()
        culture = State()
        culture_name = State()

        class Building_Configuration(StatesGroup):
            simple = State()  # Простая геометрическая форма
            hard = State()  # Сложная геометрическая форма

        class Basement(StatesGroup):
            have_basement = State()
            on_full = State()  # Над всей площадью здания?
            answer = State()


        class Structural_Scheme(StatesGroup):
            name_of_the_object = State()  # Введите название объекта


        class Series(StatesGroup):
            individual_project = State()  # Индивидуальный проект
            answer = State()  # Введите серию/модификацию

        class Attic(StatesGroup):
            have_attic = State()
            on_full = State()
            answer = State()