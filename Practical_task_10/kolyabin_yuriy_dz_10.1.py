class Matrix:
    def __init__(self, mtrx):
        self.mtrx = mtrx

    def __str__(self):
        str_mtrx = ''
        for row in self.mtrx:
            for x in row:
                if x == row[0]:
                    str_mtrx += f'|{x} '
                elif x == row[-1]:
                    str_mtrx += f'{x}|\n'
                else:
                    str_mtrx += f'{x} '
        return str_mtrx

    def __add__(self, other):
        sum_mtrx = [[self.mtrx[i][j] + other.mtrx[i][j] for j in range(len(self.mtrx[0]))] for i in
                    range(len(self.mtrx))]
        return Matrix(sum_mtrx)


matrix_1 = Matrix([[345, 45], [45, 7457], [435, 78]])
matrix_2 = Matrix([[25, -345], [55, -345], [-22, 547]])
print(matrix_1)
print(matrix_2)
print(matrix_1 + matrix_2)
matrix_3 = Matrix([[3, 5, 32], [2, 4, 6], [-1, 64, -8]])
matrix_4 = Matrix([[-1, 64, -8], [2, 4, 6], [3, 5, 32]])
print(matrix_3)
print(matrix_4)
print(matrix_3 + matrix_4)
