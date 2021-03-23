import time


def out_red(text):
    print("\033[5m\033[31m {}".format(text))
    time.sleep(7)


def out_yellow(text):
    print("\033[33m {}".format(text))
    time.sleep(2)


def out_green(text):
    print("\033[32m {}".format(text))
    time.sleep(3)


class CustomError(Exception):
    pass


class TrafficError(CustomError):
    pass


class TrafficLight:
    def __init__(self, r='Red', y='Yellow', g='Green'):
        self.__color = (r, y, g)  # Порядок следования - как в задании, но изменив последовательность,
        # можем получить любой порядок следования этих трех цветов.
        # ('Red', 'Yellow', 'Green', 'Yellow')- приведет к переключению между зеленым и красным через желтый.
        self.t_color = ('Red', 'Yellow', 'Green')

    def running(self):
        colors = self.__color
        t_colors = self.t_color

        try:

            for n in range(len(t_colors)):
                if colors != t_colors:
                    raise TrafficError
                else:
                    i = 0
                    while i < 10:  # Ограничил работу 10-ю повторениями
                        for clr in colors:
                            if clr == 'Red':
                                out_red(f'{clr}')
                            if clr == 'Yellow':
                                out_yellow(f'{clr}')
                            if clr == 'Green':
                                out_green(f'{clr}')
                                i += 1

        except TrafficError:
            print(f'Порядок следования цветов отличается от эталонного.')


a = TrafficLight()
# a = TrafficLight('Red', 'Green', 'Yellow')  # В случае назначения последовательности цветов отличной от эталонной,
# будет выведено предупреждение и осуществлен выход из скрипта.
# print(a.__color) при попытке обратиться к приватному атрибуту - получим ошибку отсутствия атрибута.
a.running()
