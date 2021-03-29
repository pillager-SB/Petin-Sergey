# Реализовать проект расчёта суммарного расхода ткани на производство одежды.
# Основная сущность (класс) этого проекта — одежда, которая может иметь определённое название.
# К типам одежды в этом проекте относятся пальто и костюм.
# У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
# Это могут быть обычные числа: V и H соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
# для костюма (2*H + 0.3). Проверить работу этих методов на реальных данных.
# Выполнить общий подсчёт расхода ткани.
# Проверить на практике полученные на этом уроке знания.
#  Реализовать абстрактные классы для основных классов проекта и проверить работу декоратора @property.

from abc import ABC, abstractmethod
from decimal import Decimal


class MyAbstractClass(ABC):
    @abstractmethod
    def get_area(self):
        pass


class Textil:
    def __init__(self, type_of_clothing, num):
        self.type_of_clothing = type_of_clothing
        self.num = num

    # Выбор формулы рассчета площади ткани, исходя из типа одежды.
    @property
    def get_area(self):
        if self.type_of_clothing == 'coat':
            num = Decimal(self.num / 6.5 + 0.5)
            num = num.quantize(Decimal("1.00"))
            return num
        elif self.type_of_clothing == 'suit':
            num = Decimal(2 * self.num + 0.3)
            num = num.quantize(Decimal("1.00"))
            return num
        else:
            exit('Доступны только два типа одежды: coat и suit')

    def __str__(self):
        return f'Расход ткани для {self.type_of_clothing}: {self.get_area}'

    def __add__(self, other):
        return f'Общая площадь ткани: {self.get_area + other.get_area}'


coat = Textil('coat', 56)
suit = Textil('suit', 4)
print(coat)
print(suit)
print(suit + coat)
