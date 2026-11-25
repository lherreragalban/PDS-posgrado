import numpy as np
import matplotlib.pyplot as plt

n = np.arange(-5, 35)

# --- Caso a) ---
x_a = 2 * ((n >= 0) & (n < 15))
y_a = np.zeros_like(n, dtype=float)
for i, ni in enumerate(n):
    if ni == 0:
        y_a[i] = x_a[i] - 0
    elif ni > 0:
        y_a[i] = x_a[i] - x_a[i-1]

# --- Caso b) ---
x_b = np.zeros_like(n, dtype=float)
for i, ni in enumerate(n):
    if 0 <= ni < 10:
        x_b[i] = ni
    elif 10 <= ni < 25:
        x_b[i] = 25 - ni
y_b = np.zeros_like(n, dtype=float)
for i, ni in enumerate(n):
    if ni == 0:
        y_b[i] = x_b[i] - 0
    elif ni > 0:
        y_b[i] = x_b[i] - x_b[i-1]

# --- Caso c) ---
x_c = np.zeros_like(n, dtype=float)
for i, ni in enumerate(n):
    if 0 <= ni < 25:
        x_c[i] = np.sin(np.pi * ni / 25)
y_c = np.zeros_like(n, dtype=float)
for i, ni in enumerate(n):
    if ni == 0:
        y_c[i] = x_c[i] - 0
    elif ni > 0:
        y_c[i] = x_c[i] - x_c[i-1]

# --- Gráficos ---
plt.figure(figsize=(14, 10))

# Caso a)
plt.subplot(3, 2, 1)
plt.stem(n, x_a, 'b', markerfmt='bo', label='x[n]')
plt.title('Caso a): x[n] = 2(u[n]-u[n-15])')
plt.xlabel('n'); plt.ylabel('x[n]'); plt.grid(); plt.legend()

plt.subplot(3, 2, 2)
plt.stem(n, y_a, 'r', markerfmt='ro', label='y[n]')
plt.title('Caso a): Salida y[n] = x[n]-x[n-1]')
plt.xlabel('n'); plt.ylabel('y[n]'); plt.grid(); plt.legend()

# Caso b)
plt.subplot(3, 2, 3)
plt.stem(n, x_b, 'b', markerfmt='bo', label='x[n]')
plt.title('Caso b): x[n] triangular')
plt.xlabel('n'); plt.ylabel('x[n]'); plt.grid(); plt.legend()

plt.subplot(3, 2, 4)
plt.stem(n, y_b, 'r', markerfmt='ro', label='y[n]')
plt.title('Caso b): Salida y[n]')
plt.xlabel('n'); plt.ylabel('y[n]'); plt.grid(); plt.legend()

# Caso c)
plt.subplot(3, 2, 5)
plt.stem(n, x_c, 'b', markerfmt='bo', label='x[n]')
plt.title('Caso c): x[n] = sen(πn/25)')
plt.xlabel('n'); plt.ylabel('x[n]'); plt.grid(); plt.legend()

plt.subplot(3, 2, 6)
plt.stem(n, y_c, 'r', markerfmt='ro', label='y[n]')
plt.title('Caso c): Salida y[n]')
plt.xlabel('n'); plt.ylabel('y[n]'); plt.grid(); plt.legend()

plt.tight_layout()
plt.show()
