from sys import argv


def test_n(str_in):  # Функция проверки введенных данных (цифры или нет).
    num_in = str_in[1]
    if num_in.isdigit():
        return num_in
    else:
        piese = num_in.replace('.', ',').split(',')
        if piese[0].strip().isdigit() and piese[1].strip().isdigit():
            num_in = f'{piese[0].strip()},{piese[1].strip()}' # стандартизация вывода, используются только ','
            return num_in
        else:
            exit('Error: Сумма прибыли должна быть введена числом')


if len(argv) == 2:
    txt_line = test_n(argv)
    with open('bakery.csv', 'a', encoding='utf-8') as log:
        print(txt_line, file=log)
else:
    exit('Error: Ошибка при вводе')
