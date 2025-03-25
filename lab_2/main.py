import numpy as np


def get_T(A):
    n = len(A)
    T = np.zeros((n, n))

    for i in range(n):
        for j in range(i + 1):
            sum_ = sum(T[i][k] * T[j][k] for k in range(j))
            if i == j:
                T[i][j] = (A[i][i] - sum_) ** 0.5
            else:
                T[i][j] = (A[i][j] - sum_) / T[j][j]

    return T


def solve(A, b):
    n = len(b)
    y = np.zeros(n)
    T = get_T(A)
    for i in range(n):
        sum_ = sum(T[i][j] * y[j] for j in range(i))
        y[i] = (b[i] - sum_) / T[i][i]

    print(f"Матриця T:\n{T}\n\nвектор y: {y}\n")

    x = np.zeros(n)
    Tt = T.T
    print(f"Матриця T транспанована\n{Tt}\n")
    for i in range(n - 1, -1, -1):
        sum_ = sum(Tt[i][j] * x[j] for j in range(i + 1, n))
        x[i] = (y[i] - sum_) / Tt[i][i]

    return x


A = np.array([
    [5.5, 7.0, 6.0, 5.5],
    [7.0, 10.5, 8.0, 7.0],
    [6.0, 8.0, 10.5, 9.0],
    [5.5, 7.0, 9.0, 10.5]
], dtype=float)
b = np.array([23, 32, 33, 31], dtype=float)
x = solve(A, b)

print(f"Розв'язок системи: {x}\n")

r = b - np.dot(A, x)
print(f"Вектор нев'язки: {r}")