# Это просто заглушка, если можно, само решение я сдам позже.

class StoreHouse:
    def reception(self):  # Все что связано с приемом оборудования
        pass

    def storage(self):  # Все что связано с хранением (получение данных по запросам)
        pass

    def delivery(self):  # Все что связано с выдачей в другие отделы.
        pass

    def read(self):  # Чтение базы (предварительно, планирую сохранять данные в текстовый файл)
        pass

    def write(self):  # Запись изменений в базу.
        pass


class Apparats:  # Класс-предок для всех классов оборудования
    def __init__(self, mod_name, pg_model, quantity, id_storage, *args):
        self.mod_name = mod_name
        self.pg_model = pg_model
        self.quantity = quantity
        self.id_storage = id_storage

    def __str__(self):
        return f'Тип утройства: {self.id_type}' \
               f'Модель устройства: {self.id_storage}\n' \
               f'Количество устройств: {self.quantity}\n' \
               f'Место хранения: {self.id_storage}'


class Printers(Apparats):
    def __init__(self, max_size='A4', color=True):
        pass


class Scanners(Apparats):
    def __init__(self, max_dpi):
        pass


class Copier(Apparats):
    def __init__(self, max_size='A4', color=True, ADF=True):
        pass
