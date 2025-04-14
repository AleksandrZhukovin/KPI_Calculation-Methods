import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from scipy.interpolate import CubicSpline


matplotlib.use('TkAgg')


def f(x):
    return x * np.tan(x)


x_nodes = np.linspace(-np.pi/3, np.pi/3, 15)
y_nodes = f(x_nodes)

print(f"X|"+''.join(f"{x:5.2f}|" for x in x_nodes))
print(f"Y|"+''.join(f"{y:5.2f}|" for y in y_nodes))


def lagrange(x, x_nodes, y_nodes):
    total = 0
    n = len(x_nodes)
    for j in range(n):
        term = y_nodes[j]
        for m in range(n):
            if m != j:
                term *= (x - x_nodes[m]) / (x_nodes[j] - x_nodes[m])
        total += term
    return total


x_dense = np.linspace(-np.pi/3, np.pi/3, 1000)
y_true = f(x_dense)
y_lagrange = np.array([lagrange(xi, x_nodes, y_nodes) for xi in x_dense])


cubic_spline = CubicSpline(x_nodes, y_nodes)
y_spline = cubic_spline(x_dense)


e_lagrange = np.abs(y_true - y_lagrange)
e_spline = np.abs(y_true - y_spline)
e_l = max(e_lagrange)
e_s = max(e_spline)
print(f"Похибка Лагранжа: {e_l}")
print(f"Похибка сплайн: {e_s}")


plt.plot(x_dense, y_true, label="x*tg(x)", linewidth=2)
plt.plot(x_dense, y_lagrange, '--', label="Поліном Лагранжа")
plt.plot(x_dense, y_spline, ':', label="Кубічний сплайн")
plt.plot(x_nodes, y_nodes, 'o', label="Вузли")
plt.legend()
plt.grid(True)
plt.show()

plt.plot(x_dense, e_lagrange)
plt.title("Похибка Лагранжа")
plt.grid(True)
plt.show()

plt.plot(x_dense, e_spline)
plt.title("Похибка сплайн")
plt.grid(True)
plt.show()
