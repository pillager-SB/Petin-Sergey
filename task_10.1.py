class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        return str(('\n'*2).join([('\t' * 2).join([str(j) for j in i]) for i in self.matrix])) + f'\n{"-" * 10}'

    def __add__(self, other):
        if len(self.matrix) == len(other.matrix):
            return Matrix([
                [cell_1 + cell_2 for cell_1, cell_2 in zip(row_1, row_2)]
                for row_1, row_2 in zip(self.matrix, other.matrix)
            ])

        else:
            return f'Попытка сложения разноразмерных матриц.'


matrix_1 = Matrix([[1, 2], [3, 4], [5, 6]])
matrix_2 = Matrix([[7, 8], [9, 10], [11, 12]])

print(matrix_1)
print(matrix_2)
print(matrix_1 + matrix_2)
