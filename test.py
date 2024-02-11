EPSILON = 1e-10

def swap_rows(matrix, row1, row2):
    matrix[row1], matrix[row2] = matrix[row2], matrix[row1]

def gaussian_elimination(matrix):
    rows = len(matrix)
    cols = len(matrix[0]) - 1

    for i in range(rows):
        pivot_row = i
        for j in range(i + 1, rows):
            if abs(matrix[j][i]) > abs(matrix[pivot_row][i]):
                pivot_row = j

        if abs(matrix[pivot_row][i]) < EPSILON:
            continue

        if pivot_row != i:
            swap_rows(matrix, i, pivot_row)

        for j in range(i + 1, rows):
            factor = matrix[j][i] / matrix[i][i]
            for k in range(i, cols + 1):
                matrix[j][k] -= factor * matrix[i][k]

    # Обратный ход с занулением элементов под главной диагональю
    for i in range(rows - 1, -1, -1):
        if abs(matrix[i][i]) < EPSILON:
            continue
        matrix[i][cols] /= matrix[i][i]
        matrix[i][i] = 1
        for j in range(i - 1, -1, -1):
            if abs(matrix[j][i]) < EPSILON:
                continue
            factor = matrix[j][i] / matrix[i][i]
            matrix[j][cols] -= factor * matrix[i][cols]
            matrix[j][i] = 0

# Пример входных данных (матрица коэффициентов системы уравнений)
matrix = [
    [-2, 1, -3, -8],
    [3, 1, -6, -9],
    [1, 1, 2, 5]
]

gaussian_elimination(matrix)

# Извлечение и вывод значений x, y, z
x, y, z = matrix[0][-1], matrix[1][-1], matrix[2][-1]
print("x =", x)
print("y =", y)
print("z =", z)

# Вывод полученной матрицы
for row in matrix:
    print("\t".join(map(str, row)))