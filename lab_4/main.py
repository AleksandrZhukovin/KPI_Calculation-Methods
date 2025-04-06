import numpy as np


A = np.array([[7, 0.88, 0.93, 1.21],
              [0.88, 4.16, 1.3, 0.15],
              [0.93, 1.3, 6.44, 2],
              [1.21, 0.15, 2, 9]],  dtype=float)

n = A.shape[0]
iter = 1

while True:
    off_diagonal_indices = np.triu_indices(n, k=1)
    abs_A = np.abs(A[off_diagonal_indices])
    max_idx = np.argmax(abs_A)

    if abs_A[max_idx] < 1e-5:
        break

    i, j = off_diagonal_indices[0][max_idx], off_diagonal_indices[1][max_idx]

    if A[i, i] == A[j, j]:
        theta = np.pi / 4
    else:
        tau = (A[j, j] - A[i, i]) / (2 * A[i, j])
        t = np.sign(tau) / (abs(tau) + np.sqrt(1 + tau ** 2))
        theta = np.arctan(t)

    c, s = np.cos(theta), np.sin(theta)

    T = np.eye(n)
    T[i, i] = c
    T[j, j] = c
    T[i, j] = s
    T[j, i] = -s
    A = T.T @ A @ T

    print(f"Ітерація {iter}")
    print(f"Матриця T:\n", T)
    print(f"Сферична норма: {np.sum(A**2):.2f}")
    print(f"Сферична норма діагональна: {np.sum(np.diag(A) ** 2):.2f}")
    a = A.copy()
    np.fill_diagonal(a, 0)
    print(f"Сферична норма недіагональна: {np.sum(a ** 2):.2f}\n\n")
    iter += 1


print(np.diag(A))
