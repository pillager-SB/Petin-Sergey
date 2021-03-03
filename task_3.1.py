eng_set = {'one': 'один', 'two': 'два', 'three': 'три', 'four': 'четыре', 'five': 'пять', 'six': 'шесть',
           'seven': 'семь', 'eight': 'восемь', 'nine': 'девять', 'ten': 'десять'}


def num_translate(word):
    return eng_set.get(word.lower())


w = input('Введите числительное от 1 д 10 на английском языке: ')
print(f'"{num_translate(w)}"')
