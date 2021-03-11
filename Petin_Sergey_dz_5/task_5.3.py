from itertools import islice, zip_longest

tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей',
    'Дмитрий', 'Борис', 'Елена', 'Павел', 'Галина'
]
klasses = [
    '9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А', '10В', '11А'
]
# В случае, если список учителей больше списка классов, используем zip_longest на исходных списках.
# В противном случае - ограничиваем длину списка классов длиной списка учителей.
school_gen = (i for i in (zip_longest(tutors, klasses, fillvalue=None) if len(tutors) > len(klasses)
                          else zip(tutors, klasses[:len(tutors)])))
print('Тип объекта: ', type(school_gen))
print(*school_gen, sep=', ')
print(tuple(islice(school_gen, 2)))  # При попытке получить данные из истощенного генератора, видим, что там ничего нет.
