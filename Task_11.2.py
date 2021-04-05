class ZeroDivErr(Exception):
    def __init__(self, mess):
        self.mess = mess


message = ["Введите делимое: ", "Введите делитель: "]
num = []
for i in range(len(message)):
    num.append(int(input(message[i])))

try:
    if int(num[1]) == 0:
        raise ZeroDivErr("Деление на ноль невозможно!")
except ZeroDivErr as err:
    print(err)
else:
    print(f'{num[0]} / {num[1]} = {num[0] / num[1]}')
