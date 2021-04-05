class Data:
    def __init__(self, dey, month, year):
        self.dey = dey
        self.month = month
        self.year = year

    @classmethod
    def get_data_param(cls, input_data):
        dmy = input_data.split('-')
        d, m, y = (int(n) for n in dmy)
        return cls(d, m, y)

    @staticmethod
    def valid_num(obj):
        if obj.month in range(1, 12 + 1):
            if obj.year in range(0, 2021 + 201):  # ограничиваю дату пределами нашей эры
                # (годы от нулевого и +200 лет от текущей даты).
                return 'Все в порядке!'
            return 'Дата за пределами разумного'
        return 'В нашем календаре только 12 месяцев!'


my_data = input('Введите дату (dd-mm-yyyy): ')

cls_data = Data.get_data_param(my_data)
print(cls_data.dey, cls_data.month, cls_data.year, sep='.')
print(Data.valid_num(cls_data))
