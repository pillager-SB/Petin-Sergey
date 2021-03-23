# 3. Реализовать базовый класс Worker (работник).
#
#     определить атрибуты: name, surname, position (должность), income (доход);
#     последний атрибут должен быть защищённым и ссылаться на словарь, содержащий элементы:
#     оклад и премия, например, {"wage": wage, "bonus": bonus};
#     создать класс Position (должность) на базе класса Worker;
#     в классе Position реализовать методы получения полного имени сотрудника (get_full_name)
#     и дохода с учётом премии (get_total_income);
#     проверить работу примера на реальных данных: создать экземпляры класса Position,
#     передать данные, проверить значения атрибутов, вызвать методы экземпляров.

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
