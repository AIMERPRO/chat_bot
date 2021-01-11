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

    class Basement(StatesGroup):
        b_keyboard_inline = State()

        class EnterToBasement(StatesGroup):
            enter_to_basement_inline = State()

            class Stairs(StatesGroup):
                stairs_inline = State()
                width = State()
                length = State()

                class Steps(StatesGroup):
                    steps_inline = State()

                    width = State()
                    height = State()

                    material = State()
                    material_answer = State()

                    finishing = State()
                    finishing_answer = State()

                    tile_answer = State()

            class Walls(StatesGroup):
                walls = State()

                class Handrail(StatesGroup):
                    handrail = State()

                    material = State()
                    material_answer = State()

                    length = State()
                    width = State()
                    height = State()

                    finishing = State()
                    finishing_answer = State()

                    mounting_method = State()

                class Finishing(StatesGroup):
                    finishing = State()
                    finishing_answer = State()

            class Door(StatesGroup):
                door = State()

                length = State()
                width = State()

                material = State()
                material_answer = State()

            class Photo(StatesGroup):
                photo = State()

                full_photo = State()
                defect_photo = State()

        class Sizes(StatesGroup):
            sizes = State()

            height = State()

            area_full = State()

            class WaterIntake(StatesGroup):
                class Yes(StatesGroup):
                    yes = State()

                    width = State()
                    height = State()
                    depth = State()

                    class Grid(StatesGroup):
                        grid = State()

                        length = State()
                        width = State()

                        material = State()
                        material_answer = State()

                    class Photo(StatesGroup):
                        photo = State()

                        full_photo = State()
                        defect_photo = State()

        class Floor(StatesGroup):
            floor = State()

            material = State()
            material_answer = State()

            finishing = State()
            finishing_answer = State()

            class Photo(StatesGroup):
                photo = State()

                full_photo = State()
                defect_photo = State()

            defect = State()
            defect_answer = State()

        class Walls(StatesGroup):
            walls = State()

            area = State()

            material = State()
            material_answer = State()

            finishing = State()
            finishing_answer = State()

            class Photo(StatesGroup):
                photo = State()

                full_photo = State()
                defect_photo = State()

            defect = State()
            defect_answer = State()

        class Ceiling(StatesGroup):
            ceiling = State()

            area = State()

            material = State()
            material_answer = State()

            finishing = State()
            finishing_answer = State()

            class Photo(StatesGroup):
                photo = State()

                full_photo = State()
                defect_photo = State()

            defect = State()
            defect_answer = State()

        class Windows(StatesGroup):
            grids = State()

            length = State()
            width = State()

            material = State()
            material_answer = State()

            count_glass = State()

            class WindowSills(StatesGroup):
                length = State()
                width = State()

                material = State()
                material_answer = State()

        class Lighting(StatesGroup):
            cable_routing = State()
            cable_routing_answer = State()

            type_cabel = State()
            cross = State()

            switches = State()
            switches_photo = State()
            switches_photo_full = State()
            switches_photo_sketch = State()

            VRU = State()
            VRU_photo = State()

            class Photo(StatesGroup):
                photo = State()

                full_photo = State()

            class Switchboard(StatesGroup):
                length = State()
                width = State()
                height = State()

                finishing = State()
                finishing_answer = State()

            class LightFixtures(StatesGroup):
                light_fixtures = State()

                yes = State()

                lighting_type = State()
                lighting_type_answer = State()

                class Photo(StatesGroup):
                    photo = State()

                    full_photo = State()
                    defect_photo = State()
                    photo_sketches = State()


