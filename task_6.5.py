from sys import argv
from itertools import zip_longest

if len(argv) != 4:
    exit('Ошибка при вводе данных')
else:
    u_list, h_list, all_list = argv[1:]
    with open(u_list, 'r', encoding='utf-8') as names:
        with open(h_list, 'r', encoding='utf-8') as hobbies:
            end_list = zip_longest(names, hobbies, fillvalue=None)
            with open(all_list, 'w', encoding='utf-8') as e_list:
                print(*(f'{str(i[0]).strip()}: {str(i[1]).strip()}' for i in end_list), sep='\n', file=e_list)
