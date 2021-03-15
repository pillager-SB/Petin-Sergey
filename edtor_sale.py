from sys import argv

pos, val = argv[1:]
count = 0
with open('bakery.csv', 'r+', encoding='utf-8') as log:
    # Проверяем, существует ли запрошенная позиция в документе
    for t in log:
        count +=1
    if int(pos) not in range(1, count + 1):
        exit('Error: Строки с такой позицией в документе нет')
    log.seek(0)  # Возвращаемся на начало файла
    for line in range(int(pos) - 1):
        n = log.readline()
    p = log.tell()  # Запоминаем позицию курсора
    old_val = log.readline().strip()  # Обращаемся к заменяемой строке
    if len(val) < len(old_val):
        sp = len(old_val) - len(val)  # Если новая строка короче, получаем разницу в количестве символов.
    else:
        sp = 0
    log.seek(p)  # Возвращаемся на начало заменяемой строки
    log.write(f'{val}{" " * sp}')  # Записываем новое значение + необходимое количество пробелов

