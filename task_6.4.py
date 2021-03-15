from itertools import zip_longest

with open('users.csv', 'r', encoding='utf-8') as names:
    with open('hobby.csv', 'r', encoding='utf-8') as hobbies:
        end_list = zip_longest(names, hobbies, fillvalue=None)
        with open('users_hobby.txt', 'w', encoding='utf-8') as e_list:
            print(*(f'{str(i[0]).strip()}: {str(i[1]).strip()}' for i in end_list), sep='\n', file=e_list)
