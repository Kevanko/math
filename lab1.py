MIN = 1e-10

def swap_max_col(m, row, cols):
    for i in range(row, cols):
        if abs(m[row][row]) < abs(m[i][row]):
            matrix[row], matrix[i] = matrix[i], matrix[row]


def gauss(m):
    cols = len(m)
    rows = len(m[0]) - 1

    for i in range(rows):
        swap_max_col(m, i, cols)
        for j in range(i + 1, cols):
            factor = matrix[j][i] / matrix[i][i]
            for k in range(i, rows + 1):
                matrix[j][k] -= matrix[i][k] * factor

    for i in range(rows - 1, -1, -1):
            if abs(matrix[i][i]) < MIN:
                continue
            matrix[i][cols] /= matrix[i][i]
            matrix[i][i] = 1
            for j in range(i - 1, -1, -1):
                if abs(matrix[j][i]) < MIN:
                    continue
                factor = matrix[j][i] / matrix[i][i]
                matrix[j][cols] -= factor * matrix[i][cols]
                matrix[j][i] = 0

matrix = [
    [-2, 1, -3, -8],
    [3, 1, -6, -9],
    [1, 1, 2, 5]
]

gauss(matrix)

for row in matrix:
    print("\t".join(map(str, row)))