start_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
tex_tape = ''
number_tape = []

for n in start_list:
    if not n[-1].isdigit():
        tex_tape += n + ' '
    else:
        if ord(n[0]) == 43 or ord(n[0]) == 45:  # Проверка на знак '+' или '-'
            rank = '+0' + str(len(n)+1)  # Наращиваем разрядность числа, так как знак 'съедает' один разряд.
        else:
            rank = '02'
        tex_tape += '"{:' + rank + 'd}" '
        number_tape.append(int(n))
print(tex_tape[:-1].format(*number_tape))  # tex_tape[:-1] Убираем лишний пробел в конце строки
