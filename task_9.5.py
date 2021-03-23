class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        return 'Запуск отрисовки'


class Pen(Stationery):
    def draw(self):
        return f'{self.title}: Запуск отрисовки ручкой.'


class Pencil(Stationery):
    def draw(self):
        return f'{self.title}: Запуск отрисовки карандшом.'


class Handle(Stationery):
    def draw(self):
        return f'{self.title}: Запуск отрисовки маркером.'


pen = Pen('Pen')
pencil = Pencil('Pencil')
handle = Handle('Handle')
print(pen.draw())
print(pencil.draw())
print(handle.draw())
