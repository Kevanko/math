#include <iostream>
#include <vector>
#include <cmath>

using namespace std;

const double EPSILON = 1e-10;

void swap_rows(vector<vector<double>>& matrix, int row1, int row2) {
    matrix[row1].swap(matrix[row2]);
}

void gaussian_elimination(vector<vector<double>>& matrix) {
    int rows = matrix.size();
    int cols = matrix[0].size() - 1;

    for (int i = 0; i < rows; ++i) {
        int pivot_row = i;
        for (int j = i + 1; j < rows; ++j) {
            if (abs(matrix[j][i]) > abs(matrix[pivot_row][i])) {
                pivot_row = j;
            }
        }

        if (abs(matrix[pivot_row][i]) < EPSILON) {
            continue;
        }

        if (pivot_row != i) {
            swap_rows(matrix, i, pivot_row);
        }

        for (int j = i + 1; j < rows; ++j) {
            double factor = matrix[j][i] / matrix[i][i];
            for (int k = i; k < cols + 1; ++k) {
                matrix[j][k] -= factor * matrix[i][k];
            }
        }
    }

    // Back substitution
    for (int i = rows - 1; i >= 0; --i) {
        if (abs(matrix[i][i]) < EPSILON) {
            continue;
        }
        matrix[i][cols] /= matrix[i][i];
        matrix[i][i] = 1;
        for (int j = i - 1; j >= 0; --j) {
            if (abs(matrix[j][i]) < EPSILON) {
                continue;
            }
            double factor = matrix[j][i] / matrix[i][i];
            matrix[j][cols] -= factor * matrix[i][cols];
            matrix[j][i] = 0;
        }
    }
}

int main() {
    // Пример входных данных (матрица коэффициентов системы уравнений)
    vector<vector<double>> matrix = {{2, 1, -1, 8},
                                      {-3, -1, 2, -11},
                                      {-2, 1, 2, -3}};

    gaussian_elimination(matrix);

    // Извлечение и вывод значений x, y, z
    double x = matrix[0].back();
    double y = matrix[1].back();
    double z = matrix[2].back();
    cout << "x = " << x << endl;
    cout << "y = " << y << endl;
    cout << "z = " << z << endl;

    // Вывод полученной матрицы
    for (const auto& row : matrix) {
        for (const auto& val : row) {
            cout << val << "\t";
        }
        cout << endl;
    }

    return 0;
}
