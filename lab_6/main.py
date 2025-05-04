import numpy as np
import matplotlib.pyplot as plt
import matplotlib


matplotlib.use('TkAgg')


def rk(f, x0, y0, h, n):
    x = [x0]
    y = [y0]
    for i in range(n):
        k1 = h * f(x[i], y[i])
        k2 = h * f(x[i] + h / 2, y[i] + k1 / 2)
        k3 = h * f(x[i] + h / 2, y[i] + k2 / 2)
        k4 = h * f(x[i] + h, y[i] + k3)
        x.append(x[i] + h)
        y.append(y[i] + (k1 + 2 * k2 + 2 * k3 + k4) / 6)
    return np.array(x), np.array(y)


def ab(f, x0, y0, h, n):
    x_rk, y_rk = rk(f, x0, y0, h, 3)
    x = list(x_rk)
    y = list(y_rk)

    for i in range(3, n):
        x_new = x[-1] + h
        f1 = f(x[-1], y[-1])
        f2 = f(x[-2], y[-2])
        f3 = f(x[-3], y[-3])
        f4 = f(x[-4], y[-4])
        y_new = y[-1] + h / 24 * (55 * f1 - 59 * f2 + 37 * f3 - 9 * f4)
        x.append(x_new)
        y.append(y_new)
    return np.array(x), np.array(y)


def f(x, y):
    return (1 - x**2) * y + (1 / np.cos(x))**2 - (1 - x**2) * np.tan(x)


x0 = 0
y0 = 0
h = 0.1
xn = 1
n = int((xn - x0) / h)

x_rk, y_rk = rk(f, x0, y0, h, n)
x_ab, y_ab = ab(f, x0, y0, h, n)

dy = np.tan(x_rk)

error_rk = np.abs(dy - y_rk)
error_ab = np.abs(dy - y_ab)

plt.figure(figsize=(10, 5))
plt.plot(x_rk, dy, label="Точне рішення", linewidth=2)
plt.plot(x_rk, y_rk, 'o--', label="Рунге-Кутта", markersize=4)
plt.plot(x_ab, y_ab, 's--', label="Адамс-Башфорт", markersize=4)
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.legend()
plt.show()

plt.figure(figsize=(10, 5))
plt.plot(x_rk, error_rk, 'o-', label="Похибка Рунге-Кутта")
plt.plot(x_ab, error_ab, 's-', label="Похибка Адамса-Башфорта")
plt.xlabel("x")
plt.ylabel("Похибка")
plt.yscale("log")
plt.grid(True)
plt.legend()
plt.show()
