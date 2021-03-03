from random import choice

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]


def get_jokes(n=5, key=False):
    """
    Функция генерирует фразы, получаемые комбинацией случайных элементов из трех списков слов.

    Функция берет случайным образом по одному объекту из трех списков и собирает из них фразу.
    Возможны два режима работы:
    1. Без ограничений на повторы слов. Установлен по умолчанию, позволяет получит произвольное количество фраз.
    Включается флагом key = False.
    2. Использование только уникальных слов (слово не может быть использовано более чем в одной фразе).
    Включается ключом key = True.

    :param n: количество "заказанных" фраз. По умолчнию: 5
    В режиме уникальных слов позволит создать количество фраз не более количества слов в самом коротком списке.
    :param key: Выбор режима (True or False) уникальных слов или без ораничения повторов. По умолчнию: False
    :return: Возвращаемое значение - список содержащий сгенерированные фразы в качестве объектов.
    """

    first, second, third = nouns.copy(), adverbs.copy(), adjectives.copy()
    jokes = []

    for i in range(n):
        if key:
            if len(first) != 0 and len(second) != 0 and len(third) != 0:
                jokes.append(
                    f'{first.pop(first.index(choice(first)))} {second.pop(second.index(choice(second)))} '
                    f'{third.pop(third.index(choice(third)))}')
        else:
            jokes.append(f'{choice(first)} {choice(second)} {choice(third)}')

    return jokes


print(get_jokes(15, 1))
#  print(get_jokes.__doc__)
