from sys import argv
from itertools import islice


def test_n(argv):  # Функция проверки введенных данных.
    if len(argv) > 3:
        exit('Введено слишком много данных')
    else:
        for n in argv[1:]:
            if not n.isdigit():
                exit('Error: Для запроса нужно вводить только целые числа')
    return len(argv[1:])

with open('bakery.csv', 'r', encoding='utf-8') as log:
    n = test_n(argv)
    if n == 0:
        print(log.read())
    if n > 0:
        f_num = int(argv[1])
        if f_num < 1:
            exit('Error: поиск начинается с первой строки.')
        else:
            if n == 1:
                print(*islice(log, int(argv[1])-1, None), sep='')
            if n == 2:
                print(*islice(log, int(argv[1])-1, int(argv[2])), sep='')

