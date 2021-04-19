import shutil


class Storage:
    @staticmethod
    def check(device_name):  # Проверяем на совпадение вводимого назавания техники с базой
        with open('basa.txt', 'r', encoding='utf-8') as r:
            count = 0
            for i in r:
                count += 1
                arg = i.rstrip('\n').split(sep=';')
                if arg[1] == device_name:
                    return count, int(arg[-1])
            return 0, f'{device_name} в базе не обнаружен.'

    @staticmethod
    def change(count, val):  # Изменение количества единиц техники (Перезапись строки).
        # count - Номер искомой строки в документе.
        # val - Новое значение количества.

        with open('basa.txt', 'r', encoding='utf-8') as out_log:
            with open('basa.txt', 'a', encoding='utf-8') as in_log:
                for line in range(int(count)):
                    rline = out_log.readline()
                rline = rline[0:(rline.rfind(';') + 1)]
                if val == 0:  # Если количество устройств равно нулю - перезаписываем файл без этой строки.
                    Storage.erase(count)
                else:
                    print(f'{rline}{val}', file=in_log)  # Записываем новое значение в конец файла
                    Storage.erase(count)  # Удаляем строку со старым значением.

    @staticmethod
    def erase(es_num):  # Удаление строки по номеру и перезапись файла базы.
        count = 0
        with open('basa.txt', 'r', encoding='utf-8') as fr:
            with open('newbasa.txt', 'w', encoding='utf-8') as fs:
                for line in fr:
                    count += 1
                    if count != es_num:
                        fs.write(line)
        shutil.move('newbasa.txt', 'basa.txt')

    @staticmethod
    def outprintlong(type_app):  # Полная форма вывода информации
        with open('basa.txt', 'r', encoding='utf-8') as fr:
            for line in fr:
                if line[0] == type_app:
                    st = line.rstrip('\n').split(sep=';')
                    if type_app == '1':  # Принтеры.
                        print(f'Принтер {st[1]}\nТип ПУ: {st[2]}\n{st[3]}\nРазрешение печати: {st[4]} т/д\n'
                              f'Max размер листа: {st[5]}\nИнтерфейс: {st[6][1:-1]}\nКартридж: {st[7][1:-1]}\n'
                              f'Место хранения: Стеллаж{st[8]}\nКоличество: {st[9]} шт.\n')
                    if type_app == '2':  # Сканеры.
                        print(f'Сканер {st[1]}\nТип СУ: {st[2]}\nРазрешение сканирования: {st[3]} т/д\n'
                              f'Max размер скана: {st[4]}\nИнтерфейс: {st[5][1:-1]}\n'
                              f'Место хранения: Стеллаж {st[6]}\nКоличество: {st[7]} шт.\n')
                    if type_app == '3':  # МФУ.
                        print(f'МФУ {st[1]}\nТип ПУ: {st[2]}\n{st[3]}\nРазрешение печати: {st[4]} т/д\n'
                              f'Max размер листа: {st[5]}\nИнтерфейс: {st[6][1:-1]}\nКартридж: {st[7][1:-1]}\n'
                              f'Разрешение сканирования: {st[8]} т/д\nMax размер скана: {st[9]}\n'
                              f'Место хранения: Стеллаж {st[10]}\nКоличество: {st[11]} шт.\n')

    @staticmethod
    def outprintshort(type_app):  # Сокращенная форма вывода информации
        with open('basa.txt', 'r', encoding='utf-8') as fr:
            count = 0
            n = {}
            for line in fr:
                if line[0] == type_app:
                    st = line.rstrip('\n').split(sep=';')
                    count += 1
                    if type_app == '1':  # Принтеры.
                        print(f'{count}. Принтер {st[1]}, Max размер листа: {st[5]}, Место хранения: Стеллаж {st[8]}, '
                              f'Количество: {st[9]} шт.')
                        n[count] = [st[1], st[9]]

                    if type_app == '2':  # Сканеры.
                        print(f'{count}. Сканер {st[1]}, Max размер скана: {st[4]}, Место хранения: Стеллаж {st[6]}, '
                              f'Количество: {st[7]} шт.')
                        n[count] = [st[1], st[7]]

                    if type_app == '3':  # МФУ.
                        print(f'{count}. МФУ {st[1]}, Max размер листа: {st[5]}, Max размер скана: {st[9]}, '
                              f'Место хранения: Стеллаж {st[10]}, Количество: {st[11]} шт.')
                        n[count] = [st[1], st[11]]
            return n

    @staticmethod
    def save(newstr):  # Дописываем новую строку в базу.
        with open('basa.txt', 'a', encoding='utf-8') as f:
            print(newstr, file=f)

    @staticmethod
    def sort():  # Сортировка по возрастанию для файла basa.txt. Пока не знаю алгоритмов сортировки - такое решение.
        with open('basa.txt', 'r', encoding='utf-8') as log_r:
            with open('sort.txt', 'w', encoding='utf-8') as log_s:
                fr = log_r.readlines()
                fs = sorted(fr)
                for line in fs:
                    log_s.write(line)
        shutil.move('sort.txt', 'basa.txt')
