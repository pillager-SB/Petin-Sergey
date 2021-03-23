class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': wage, 'bonus': bonus}


class Position(Worker):
    def get_full_name(self):
        return f'{self.name} {self.surname}'

    def get_total_income(self):
        return f'Полный доход: {sum(self._income.values())} рублей'


a = Position('Иван', 'Петров', 'Токарь 4 разряда', 5000, 2000)
print(a.position)
print(a.get_full_name())
print(a.get_total_income())
print(a._income)  # если нам известно имя атрибута с модификатором доступа Protected,
# то мы можем получить к нему доступ.
