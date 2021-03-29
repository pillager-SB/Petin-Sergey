class Cell:
    def __init__(self, cells):

        if str(cells).isdigit():
            self.cells = int(cells)
        else:
            exit('Все операции проводятся только с целыми числами')

    def __str__(self):
        return f'Результат: {"*" * self.cells}({self.cells})'

    def __add__(self, other):
        return Cell(self.cells + other.cells)

    def __sub__(self, other):
        if self.cells - other.cells > 0:
            return Cell(abs(self.cells - other.cells))
        elif self.cells - other.cells == 0:
            return 'Результат равен нулю'
        else:
            return 'Результат меньше нуля'

    def __mul__(self, other):
        return Cell(self.cells * other.cells)

    # оба следующих метода реализуют округление до целого числа деления.
    def __floordiv__(self, other):
        return Cell(self.cells // other.cells)

    def __truediv__(self, other):
        return Cell(int(self.cells / other.cells))

    def make_order(self, cells_in_row=6):
        row = ''
        for i in range(self.cells // cells_in_row):
            row += '*' * cells_in_row + '\n'
        row += '*' * (self.cells % cells_in_row)
        return f'Результат:\n{row}({self.cells})'


cells_1 = Cell(5)
cells_2 = Cell(9)
print(cells_1)
print(cells_2)
print((cells_1 + cells_2).make_order())
print(cells_1 - cells_2)
print((cells_1 * cells_2).make_order(8))
print(cells_2 // cells_1)
print(cells_1 / cells_2)
print(cells_2.make_order(4))
