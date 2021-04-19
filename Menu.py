import Apparats as App
import Storage as St


class Menu:
    @staticmethod
    def start_menu():
        while True:
            dialog = input('Выберите код операции: \n'
                           '1. Получение оборудования.\n'
                           '2. Выдача оборудования в отдел.\n'
                           '3. Данные о запасах хранения.\n'
                           'stop - для выхода из программы.\n'
                           ': ')
            if dialog.lower() == 'stop':
                exit('Вы вышли из программы.')
            if dialog not in ('1', '2', '3'):
                print('Нужно ввести код операции (1, 2, 3 или stop)')
                continue
            else:
                return dialog

    @staticmethod
    def menu_type():
        while True:
            set_type = input('Выберите тип оборудования: \n'
                             '1. Принтеры.\n'
                             '2. Сканеры.\n'
                             '3. Копиры\n'
                             ': ')
            if set_type not in ('1', '2', '3'):
                continue
            else:
                return set_type

    @staticmethod
    def menu_dep():
        while True:
            dep = input('Введите код подразделения для передачи обрудования со склада: \n'
                        '1. Управление\n'
                        '2. Отдел маркетинга.\n'
                        '3. Техническй отдел.\n'
                        '4. Отдел бухгалтеского учета\n'
                        ': ')

            if dep not in ('1', '2', '3', '4'):
                continue
            else:
                if dep == '1':
                    return 'Управление'
                if dep == '2':
                    return 'Отдел маркетинга'
                if dep == '3':
                    return 'Техническй отдел'
                if dep == '4':
                    return 'Отдел бухгалтеского учета'

    @staticmethod
    def name_in():
        while True:
            name = input('Введите название фирмы-производителя и модель устройства : ')
            return name

    @staticmethod
    def name_out(d):
        while True:
            out = input(f'Для выбора ведите номер строки (от 1 до {len(d)}): ')
            if out.isdigit():
                if int(out) in range(1, len(d) + 1):
                    out = int(out)
                    print(f'\nДля выдачи выбран {d[out][0]}. В наличии {d[out][1]} шт.\n')
                    while True:
                        num = int(Menu.count_menu())
                        if num in range(1, int(d[out][1])+1):
                            return d[out][0], d[out][1], num
                        else:
                            print(f'В наличии только {d[out][1]} шт.')
                            continue

    @staticmethod
    def count_menu():
        while True:
            count = input('Введите количество единиц: ')
            if count.isdigit():
                return count
            else:
                print('Введите число')
                continue

    @staticmethod
    def place_menu():  # Место хранения. Записываем место на котором будет храниться оборудование.
        # В дальнейшем возможно добавление функции проверки наличия свободных мест.
        while True:
            place = input('Введите код места хранения:\n'
                          '1. Стеллаж 1\n'
                          '2. Стеллаж 2\n'
                          '3. Стеллаж 3\n'
                          ': ')
            if place not in ('1', '2', '3'):
                continue
            else:
                return place

    @staticmethod
    def stock_in_trade_menu():
        while True:
            stock = input('Введите код просмотра:\n'
                          '1. Все оборудование\n'
                          '2. Оборудование по типам\n'
                          ': ')
            if stock not in ('1', '2'):
                continue
            else:
                while True:
                    form = input('Выберите форму просмотра:\n'
                                 '1. Краткая\n'
                                 '2. Полная\n: ')
                    if stock not in ('1', '2'):
                        continue
                    else:
                        return stock, form

    @staticmethod
    def work():
        print('')
        _ = Menu.start_menu()
        if int(_) == 1:
            st = int(Menu.menu_type())
            if st == 1:
                request_name = App.Printers.request_name()
            if st == 2:
                request_name = App.Scanners.request_name()
            if st == 3:
                request_name = App.Copiers.request_name()
            n = Menu.name_in()
            new_str = [f'{st}', n]

            t = St.Storage.check(n)
            if t[0] != 0:
                num = Menu.count_menu()
                St.Storage.change(t[0], int(t[1]) + int(num))
                St.Storage.sort()
                Menu.work()
            else:
                for i in request_name:
                    n = input(i)
                    if i.find('запятую') == -1:
                        n = f'{n}'
                    else:
                        n = f'({n})'
                    new_str.append(n)

                n = Menu.place_menu()
                new_str.append(n)

                n = Menu.count_menu()
                new_str.append(n)

                if new_str[0] == '1':
                    new_p = App.Printers(*new_str)
                    new_str = new_p.str_gen()
                if new_str[0] == '2':
                    new_p = App.Scanners(*new_str)
                    new_str = new_p.str_gen()
                if new_str[0] == '3':
                    new_p = App.Copiers(*new_str)
                    new_str = new_p.str_gen()
                    
                St.Storage.save(new_str)
                St.Storage.sort()
                Menu.work()

        if int(_) == 2:
            dp = Menu.menu_dep()  # Выбор департамента для выдачи техники.
            st = Menu.menu_type()  # Выбор типа оборудования.
            gm = St.Storage.outprintshort(st)  # Вывод информации из базы по выбранному типу в краткой форме.
            num_out = Menu.name_out(gm)
            t = St.Storage.check(num_out[0])
            St.Storage.change(t[0], int(t[1]) - num_out[2])
            print(f'\nВ {dp.lower()} передано:\n'
                  f'{num_out[0]}....{num_out[2]} шт.\n')
            St.Storage.sort()
            Menu.work()

        if int(_) == 3:  # Показ оборудования, находящегося на хранении
            stm = Menu.stock_in_trade_menu()

            if stm[0] == '1' and stm[1] == '1':
                St.Storage.outprintshort('1')
                St.Storage.outprintshort('2')
                St.Storage.outprintshort('3')
            if stm[0] == '1' and stm[1] == '2':
                St.Storage.outprintlong('1')
                St.Storage.outprintlong('2')
                St.Storage.outprintlong('3')
            if stm[0] == '2' and stm[1] == '1':
                tm = Menu.menu_type()
                St.Storage.outprintshort(f'{tm}')
            if stm[0] == '2' and stm[1] == '2':
                tm = Menu.menu_type()
                St.Storage.outprintlong(f'{tm}')

            Menu.work()


Menu.work()
