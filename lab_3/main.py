import numpy as np


A = np.array([[5.5, -0.4, 0, 2.1],
              [0, 1.6, 0.3, 0],
              [0, 0.3, 3.9, 3],
              [0, 0, 3, 5]])
b = np.array([11, 2.7, 7.9, 8], dtype=float)
x = np.zeros_like(b)

d = np.diag(A)
C = A - np.diagflat(d)

for i in range(len(C)):
    for j in range(len(C)):
        if i != j:
            C[i, j] = -(A[i, j]/A[i, i])
print(f"C:\n{C}")

i = 1
while True:
    print(f"\nІтерація №{i}")
    x_new = np.dot(C, x) + d
    print(f"x = {x_new}")
    cr = np.linalg.norm(x_new - x, ord=np.inf)
    print(cr)
    if cr < 1e-4:
        break
    x = x_new
    i += 1

r = abs(b - np.dot(A, x))
print(f"Вектор нев'язки: {r}")
