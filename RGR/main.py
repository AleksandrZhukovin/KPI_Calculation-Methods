import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation
import matplotlib


matplotlib.use('TkAgg')

alpha = 0.2
gamma = 1
D = 1.0
m0 = 1.0
n0 = 1.0

Lx, Ly = 10.0, 10.0
Nx, Ny = 100, 100
dx = Lx / (Nx - 1)
dy = Ly / (Ny - 1)

dt = 0.001
T = 1.0
Nt = int(T / dt)

x = np.linspace(0, Lx, Nx)
y = np.linspace(0, Ly, Ny)
X, Y = np.meshgrid(x, y)


n = np.exp(-((X - Lx / 2) ** 2 + (Y - Ly / 2) ** 2))


def m(n):
    return m0 * np.exp(-n / n0)


def step(n):
    n_new = n.copy()
    a = (
            (np.roll(n, -1, axis=0) - 2 * n + np.roll(n, 1, axis=0)) / dx ** 2 +
            (np.roll(n, -1, axis=1) - 2 * n + np.roll(n, 1, axis=1)) / dy ** 2
    )
    n_new += dt * (-gamma * n + alpha * m(n) * n ** 2 + D * a)
    n_new[0, :] = n_new[-1, :] = 0
    n_new[:, 0] = n_new[:, -1] = 0
    return n_new


frames = []
frames.append(n.copy())
for k in range(Nt):
    n = step(n)
    if k % 10 == 0:
        frames.append(n.copy())


fig, ax = plt.subplots()
cax = ax.imshow(frames[0], extent=[0, Lx, 0, Ly], cmap='viridis', origin='lower')
fig.colorbar(cax)


def animate(i):
    cax.set_array(frames[i])
    ax.set_title(f'{i * dt * 10:.2f}')
    return [cax]


ani = animation.FuncAnimation(fig, animate, frames=len(frames), interval=100)
# gif_path = "results/animation.gif"
# ani.save(gif_path, writer='pillow', fps=10)
# plt.close(fig)
plt.show()


fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')
n_final = frames[-1]
surf = ax.plot_surface(X, Y, n_final, cmap='viridis')
ax.set_title('Густина популяції')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('n')
fig.colorbar(surf, ax=ax, shrink=0.5, aspect=10)
plt.tight_layout()
plt.show()
