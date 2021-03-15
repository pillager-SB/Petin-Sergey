import json
from itertools import zip_longest

# Считываем данные списков users.csv и hobby.csv
with open('users.csv', 'r', encoding='utf-8') as f:
    with open('hobby.csv', 'r', encoding='utf-8') as ff:
        names = f.read().split('\n')
        hobbies = ff.read().split('\n')
        end_list = dict(i for i in (zip_longest(names, hobbies, fillvalue=None)))

        with open('end_list.json', 'w', encoding='utf-8') as fff:
            if None in end_list:  # так как это просто маркер выхода - немного экономим на памяти,
                # т.к. такое значение ключа будет одно, а не весь диапазон списка увлечений,
                # превышающий список пользоватлей.
                exit(1)  # Выходим с кодом '1'
            else:  # если пользоателей оказалось не меньше чем увлечений -
                # записываем в файл end_list.json с сериализацей
                json.dump(end_list, fff, ensure_ascii=False, indent=4)
# Считываем информацию из файла , после десериализации (если пользоателей оказалось не меньше чем увлечений
# и список был в него записан), видим, что данные сохранились и их тип <class 'dict'>
# иначе был выход, файл пустой и до этой части мы не дойдем.
with open('end_list.json', 'r', encoding='utf-8') as f:
    end_list = json.load(f)

print(end_list, type(end_list))
