import numpy as np
import matplotlib.pyplot as plt

a1 = -0.8
a2 = 0.64
b0 = 0.84

N = 50
h = np.zeros(N)
h[0] = b0  

for n in range(1, N):
    h[n] = -a1*h[n-1] - a2*h[n-2]
    
plt.figure(figsize=(10, 4))
plt.stem(range(N), h, 'b', markerfmt='bo', label='h[n]')
plt.title('Respuesta impulsional h[n] (0 ≤ n ≤ 49)')
plt.xlabel('n'); plt.ylabel('h[n]'); plt.grid(); plt.legend()
plt.show()

print("Primeros 10 valores de h[n]:", h[:10])

# inciso c

N = 101
x = np.ones(N)  
y1 = np.zeros(N)

y1[0] = b0 * x[0] 
if N > 1:
    y1[1] = -a1*y1[0] + b0*x[1]

for n in range(2, N):
    y1[n] = -a1*y1[n-1] - a2*y1[n-2] + b0*x[n]

plt.figure(figsize=(10, 4))
plt.stem(range(N), y1, 'b', markerfmt='bo', label='y1[n]')
plt.title('Respuesta al escalón y1[n] (0 ≤ n ≤ 100)')
plt.xlabel('n'); plt.ylabel('y1[n]'); plt.grid(); plt.legend()
plt.show()

print("Valor final de y1[n]:", y1[-1])

# inciso d

h_fir = np.zeros(N)
h_fir[:21] = h[:21]  
y2 = np.convolve(np.ones(N), h_fir)[:N]

plt.figure(figsize=(10, 4))
plt.stem(range(N), y1, 'b', markerfmt='bo', label='y1[n] (IIR completa)')
plt.stem(range(N), y2, 'r', markerfmt='ro', label='y2[n] (FIR truncada)')
plt.title('Comparación y1[n] vs y2[n]')
plt.xlabel('n'); plt.ylabel('y[n]'); plt.grid(); plt.legend()
plt.show()

# inciso e
theta = np.linspace(-np.pi, np.pi, 500)
H = b0 / (1 + a1*np.exp(-1j*theta) + a2*np.exp(-1j*2*theta))

plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
plt.plot(theta, np.abs(H), 'b')
plt.title('Módulo de H_f(θ)')
plt.xlabel('θ (rad)'); plt.ylabel('|H_f(θ)|'); plt.grid()

plt.subplot(1, 2, 2)
plt.plot(theta, np.angle(H), 'r')
plt.title('Fase de H_f(θ)')
plt.xlabel('θ (rad)'); plt.ylabel('∠H_f(θ) (rad)'); plt.grid()

plt.tight_layout()
plt.show()

# inciso f

# Coeficientes
a1 = -0.8
a2 = 0.64
b0 = 0.84

# Rango de n
N = 101
n = np.arange(N)

# Entrada
x = np.cos(2 * np.pi * n / 10)

# Salida recursiva
y = np.zeros(N)
y[0] = b0 * x[0]  # y[-1] = y[-2] = 0
if N > 1:
    y[1] = -a1*y[0] - a2*0 + b0*x[1]  # y[-1]=0
for k in range(2, N):
    y[k] = -a1*y[k-1] - a2*y[k-2] + b0*x[k]

# Respuesta en frecuencia en θ = 0.2π
theta = 0.2 * np.pi
H = b0 / (1 + a1*np.exp(-1j*theta) + a2*np.exp(-1j*2*theta))
magH = np.abs(H)
phaseH = np.angle(H)

print(f"H_f(0.2π) = {H}")
print(f"|H| = {magH:.6f}")
print(f"∠H = {phaseH:.6f} rad = {np.degrees(phaseH):.4f}°")

# Salida en régimen permanente teórica
y_ss = magH * np.cos(0.2*np.pi*n + phaseH)

# Gráficos
plt.figure(figsize=(12, 6))

plt.subplot(2, 1, 1)
plt.stem(n, x, 'b', markerfmt='bo', label='x[n] = cos(2πn/10)')
plt.title('Entrada x[n]')
plt.xlabel('n'); plt.ylabel('x[n]'); plt.grid(); plt.legend()

plt.subplot(2, 1, 2)
plt.stem(n, y, 'r', markerfmt='ro', label='y[n] (salida completa)')
plt.plot(n, y_ss, 'k--', label='y_ss[n] (régimen permanente teórico)')
plt.title('Salida y[n] y régimen permanente')
plt.xlabel('n'); plt.ylabel('y[n]'); plt.grid(); plt.legend()

plt.tight_layout()
plt.show()
