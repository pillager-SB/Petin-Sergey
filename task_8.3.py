from functools import wraps


def logger(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        full_list = [num for num in (*args, *kwargs.values())]
        result = [f'{func.__name__}({num}: {type(num)})' for num in full_list]
        print(*result, *func(*args, **kwargs), sep=',\n')

    return wrapper


@logger
def calc_cube(*x, **y):  # По условию задачи мы должны в функции получить квадрат некого числа,
    # соответственно нас интересуют только числа
    # (*y.values() нужен для получения значения из именованного аргумента типа h=9)
    num_list = [num for num in (*x, *y.values()) if isinstance(num, int) or isinstance(num, float)]
    return [i ** 3 for i in num_list]


a = calc_cube({'let': 37}, 23.09, (23, 33), 15, [12, 89], h=9)
print(calc_cube.__name__)  # Проверяем, удалось ли скрыть функцию-обертку.
