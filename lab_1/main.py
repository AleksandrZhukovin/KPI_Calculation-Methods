import numpy as np
import sympy as sp


x = sp.Symbol('x')
f = 2*x**3 - 4*x**2 - x + 2
intervals = [(-0.5, -0.1), (-0.09, 1.44), (1.45, 2.5)]


def bi(f, x0, x1):
    a, b = x0, x1
    for _ in range(100):
        f_x0, f_x1 = f.subs(x, x0), f.subs(x, x1)
        print(f"{'Бісекція':-^15}\nПроміжок ({a}, {b})\nІтерація {_}\nКорінь {x1}\n" + "="*10)
        if abs(f_x1) < 0.0001:
            return x1

        x_new = x1 - f_x1 * (x1 - x0) / (f_x1 - f_x0)

        if abs(x_new - x1) < 0.0001:
            return x_new

        x0, x1 = x1, x_new

    return x1


roots_secant = [bi(f, a, b) for a, b in intervals]
print(roots_secant)


def newton(f, df, x0, a, b):
    for _ in range(100):
        f_x0 = f.subs(x, x0)
        df_x0 = df.subs(x, x0)
        print(f"{'Ньютон':-^15}\nПроміжок ({a}, {b})\nІтерація {_}\nКорінь {x0}\n" + "=" * 10)
        if abs(f_x0) < 0.0001:
            return x0

        if df_x0 == 0:
            raise ValueError("df = 0")

        x_new = x0 - f_x0 / df_x0

        if abs(x_new - x0) < 0.0001:
            return x_new

        x0 = x_new

    return x0


df = sp.diff(f, x)
roots_newton = [newton(f, df, (a + b) / 2, a, b) for a, b in intervals]
print(roots_newton)
