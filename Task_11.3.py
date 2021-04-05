class NotNumErr(Exception):
    def __init__(self, number, no_num_err=0):
        self.number = number
        self.no_num_err = no_num_err

    @classmethod
    def test(cls, data):
        if data[0] == '-':
            sign = -1
            data = data[1:]
        else:
            sign = 1

        if data.isdigit():
            n = int(data) * sign
            return cls(n)
        else:
            try:
                a = float(data)
                n = a * sign
                return cls(n)

            except Exception:  # Если оставить "голый" except , то скрипт отработает,но покажет нарушение PEP 8
                return cls(None, 1)


my_list = []
print('Для выхода из программы введите stop')
while True:
    in_string = input('Введите число: ')
    if in_string.lower() == 'stop':
        print(f'Вы вышли из программы.\n{my_list}')
        break
    else:
        k = NotNumErr.test(in_string)
        if k.no_num_err == 0:
            my_list.append(k.number)
        else:
            print('Это не число')
