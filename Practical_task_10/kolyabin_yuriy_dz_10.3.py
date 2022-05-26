class Cell:
    def __init__(self, num_cell):
        self.num_cell = num_cell

    def __str__(self):
        return f'{self.num_cell}'

    def __add__(self, other):
        print(f'сложение 2х клеток = ', end="")
        return Cell(self.num_cell + other.num_cell)

    def __sub__(self, other):
        if self.num_cell < other.num_cell:
            raise ValueError('Ошибка. 1я клетка меньше 2ой.')
        print(f'вычитание 2ой клетки из 1ой = ', end="")
        return Cell(self.num_cell - other.num_cell)

    def __mul__(self, other):
        print(f'умножение 2х клеток = ', end="")
        return Cell(self.num_cell * other.num_cell)

    def __floordiv__(self, other):
        print(f'деление 1ой клетки на 2ю клетку (без остатка) = ', end="")
        return Cell(self.num_cell // other.num_cell)

    def __truediv__(self, other):
        print(f'деление 1ой клетки на 2ю клетку  = ', end="")
        return Cell(self.num_cell / other.num_cell)

    def make_order(self, num_line):
        str_cell = ['*' * num_line] * (self.num_cell // num_line)
        if self.num_cell % num_line:
            str_cell.append('*' * (self.num_cell % num_line))
        return '\n'.join(str_cell)


cell_1 = Cell(27)
cell_2 = Cell(10)
print(cell_1 + cell_2)
print(cell_1 - cell_2)
print(cell_1 * cell_2)
print(cell_1 // cell_2)
print(cell_1 / cell_2)
print(cell_1.make_order(12))
print(cell_2.make_order(6))
