import numpy as np
import matplotlib.pyplot as plt

# ============================================================
# a) x(t) = 1 + 2cos(8πt), fs = 6 Hz
# ============================================================
fs_a = 6
f_dc = [0, 6, 12]; a_dc = [1, 1, 1]
f_4 = [2, 4, 8, 10, 14]; a_4 = [2, 2, 2, 2, 2]
freqs_a = np.array(f_dc + f_4)
amps_a = np.array(a_dc + a_4)
idx = np.argsort(freqs_a)
freqs_a, amps_a = freqs_a[idx], amps_a[idx]

plt.figure(figsize=(12, 8))

plt.subplot(3, 1, 1)
plt.stem(freqs_a, amps_a, linefmt='b-', markerfmt='bo', basefmt='k-')
plt.stem(-freqs_a, amps_a, linefmt='b-', markerfmt='bo', basefmt='k-')
plt.title('2.a) x(t) muestreada a fs = 6 Hz')
plt.ylabel('Amplitud')
plt.xlim(-15, 15)
plt.grid(True)
# ============================================================
# b) y(t) = 4 + 4 sinc²(4t), fs = 6 Hz
# ============================================================
fs_b = 6
f = np.linspace(-15, 15, 2000)

def triangulo(f, centro, ancho_base=8):
    return np.maximum(0, 1 - np.abs(f - centro) / (ancho_base / 2))

espectro_b = np.zeros_like(f)
for k in range(-3, 4):
    espectro_b += triangulo(f, k * fs_b)
for k in range(-2, 3):
    idx = np.argmin(np.abs(f - k * fs_b))
    espectro_b[idx] += 4

plt.subplot(3, 1, 2)
plt.plot(f, espectro_b, 'b-', linewidth=1.5)
plt.title('2.b) y(t) muestreada a fs = 6 Hz')
plt.ylabel('Amplitud')
plt.xlim(-15, 15)
plt.grid(True)

# ============================================================
# c) x(t) = 1 + 2cos(8πt), fs = 4 Hz
# ============================================================
fs_c = 4
freqs_c = np.array([0, 4, 8, 12])
amps_c = np.array([3, 3, 3, 3])

plt.subplot(3, 1, 3)
plt.stem(freqs_c, amps_c, linefmt='r-', markerfmt='ro', basefmt='k-')
plt.stem(-freqs_c, amps_c, linefmt='r-', markerfmt='ro', basefmt='k-')
plt.title('2.c) x(t) muestreada a fs = 4 Hz')
plt.xlabel('Frecuencia (Hz)')
plt.ylabel('Amplitud')
plt.xlim(-15, 15)
plt.grid(True)

plt.tight_layout()
plt.show()