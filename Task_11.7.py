class ComplexNumber:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.z = f'({self.a}+{self.b}j)'.replace('+-', '-')
        self.t = complex(self.a, self.b)

    def __add__(self, other):
        return f'Сумма комплексных чисел равна:\n{self.z} + {other.z} = ({self.a + other.a}+{self.b + other.b}j)' \
            .replace('+-', '-')

    def __mul__(self, other):
        return f'произведение комплексных чисел равно:\n{self.z} * {other.z} = ({self.a * other.a - self.b * other.b}' \
               f'+{self.a * other.b + self.b * other.a}j)'.replace('+-', '-')

    def test(self, other):  # Проверка результата через встроенную функцию complex()
        return f'Проверка:\n{self.t} + {other.t} = {complex(self.t + other.t)}\n{self.t} * {other.t} ' \
               f'= {complex(self.t * other.t)}'

    def __str__(self):
        return self.z


z_1 = ComplexNumber(1, -2)
z_2 = ComplexNumber(3, 4)
print(z_1)
print(z_2)
print(z_1 + z_2)
print(z_1 * z_2)
print(ComplexNumber.test(z_1, z_2))
