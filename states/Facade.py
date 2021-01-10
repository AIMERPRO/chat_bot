from aiogram.dispatcher.filters.state import StatesGroup, State


class Facade(StatesGroup): # Фасад
    drainage_trays = State()  # водоотводящие лотки
    gutters = State()  # Водостоки
    basement_entrances = State()  # Входы в подвал
    fire_ladders = State()  # лестницы пожарные
    ladders = State()  # Лестницы, ступени, пандусы входные
    transit_engineering = State()  # Инженерные системы транзитные
    facade_lighting = State()  # Фасадное освещение

    class Balconies(StatesGroup):  # Балконы
        class Fences(StatesGroup):  # ограждения
            filling = State()  # заполнения
            visors = State()  # козырьки
            stucco = State()  # лепнина
            material = State()  # материал
            facing = State()  # облицовка
            coloration = State()  # окраска
            glazing = State()  # остекление
            plaster = State()  # штукатурка

        class Bearing_plate(StatesGroup):  # Плиита несущая
            filling = State()  # заполнения
            visors = State()  # козырьки
            stucco = State()  # лепнина
            material = State()  # материал
            facing = State()  # облицовка
            coloration = State()  # окраска
            plaster = State()  # штукатурка

    class Gate(StatesGroup):  # Ворота
        class Canvases(StatesGroup):  # Полотна
            material = State()  # материал
            finishing = State()  # отделка

        class Pillars(StatesGroup):  # Столбы
            stucco = State()  # лепнина
            material = State()  # материал
            plaster = State()  # штукатурка
            facing = State()  # облицовка
            coloration = State()  # окраска

    class Entrances(StatesGroup):  # Входы в подъезды
        intercoms = State()  # Домофоны
        Information_boards = State()  # Информационные доски
        fencing = State()  # Ограждения
        ramps = State()  # Пандусы
        sites = State()  # Площадки
        steps = State()  # Ступени

        class Visors(StatesGroup):  # Козырьки
            support = State()  # Опора
            coating = State()  # Покрытие


        class Openings(StatesGroup):  # Проёмы
            filling = State()  # Заполнения
            cornices = State()  # карнизы
            slopes = State()  # откосы
            ebb = State()  # отливы
            gratings = State() # решетки

    class Window_openings(StatesGroup):  # Оконные проемы
        class Curvilinear(StatesGroup):  # криволинейные
            filling = State()  # Заполнения
            cornices = State()  # карнизы
            slopes = State()  # откосы
            ebb = State()  # отливы
            gratings = State() # решетки

        class Rectangular(StatesGroup):  # прямоугольные
            filling = State()  # Заполнения
            cornices = State()  # карнизы
            slopes = State()  # откосы
            ebb = State()  # отливы
            gratings = State() # решетки

    class Walls(StatesGroup):  # стены
        class Arches(StatesGroup):  # Арки-проезды, проходы
            stucco = State()  # лепнина
            material = State()  # материал
            facing = State()  # облицовка
            coloration = State()  # окраска
            plaster = State()  # штукатурка

        class Columns(StatesGroup):  # колонны
            stucco = State()  # лепнина
            material = State()  # материал
            facing = State()  # облицовка
            coloration = State()  # окраска
            plaster = State()  # штукатурка

        class Curved_walls(StatesGroup):  # криволинейные стены
            stucco = State()  # лепнина
            material = State()  # материал
            facing = State()  # облицовка
            coloration = State()  # окраска
            plaster = State()  # штукатурка

        class Cornices(StatesGroup):  # пилястры, карнизы
            stucco = State()  # лепнина
            material = State()  # материал
            facing = State()  # облицовка
            coloration = State()  # окраска
            plaster = State()  # штукатурка

        class Rectilinear_walls(StatesGroup):  # рядовые прямолинейные стены
            stucco = State()  # лепнина
            material = State()  # материал
            facing = State()  # облицовка
            coloration = State()  # окраска
            plaster = State()  # штукатурка

        class Light_pits(StatesGroup):  # Световые приямки
            stucco = State()  # лепнина
            material = State()  # материал
            facing = State()  # облицовка
            coloration = State()  # окраска
            plaster = State()  # штукатурка

        class Plinth(StatesGroup):  # Цоколь
            stucco = State()  # лепнина
            material = State()  # материал
            facing = State()  # облицовка
            coloration = State()  # окраска
            plaster = State()  # штукатурка
