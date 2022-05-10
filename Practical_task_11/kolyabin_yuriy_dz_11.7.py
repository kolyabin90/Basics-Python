class ComplexNumber:
    def __init__(self, z):
        self.z = z

    def __add__(self, other):
        print(f'Сложение двух комплексных чисел: {self.z} + {other.z}')
        return f'Результат: {ComplexNumber(self.z + other.z)}'

    def __mul__(self, other):
        print(f'Произведение двух комплексных чисел: {self.z} * {other.z}')
        return f'Результат: {ComplexNumber(self.z * other.z)}'

    def __repr__(self):
        return f'{self.z}'


a = 3 + 8j
b = -5 + 1j
x = ComplexNumber(a)
y = ComplexNumber(b)
print(x.__add__(y))
print(x.__mul__(y))
