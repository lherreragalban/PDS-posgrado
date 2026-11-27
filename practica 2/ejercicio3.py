import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

np.random.seed(0)

N = 100
num_bits = 100
fs_high = 100000
fs_low = 10000
T_high = 1/fs_high
T_low = 1/fs_low
M = 150

# =================================================================
# a) Generar señales
# =================================================================
b = np.random.rand(1, num_bits)
B = 1*(b>0.5) - 1*(b<0.5)
x = np.kron(B, np.ones((1, N)))[0]
t = np.arange(0, x.size) / fs_high

n = np.arange(-150, 150)
h = np.sinc(n/50)
h = h / np.sum(h)

y = np.convolve(x, h, 'full')
y = y[M:-M+1]

r = np.random.randn(y.size)
w = y + r

wd = w[::10]
hd = 10 * h[::10]

# =================================================================
# b) Respuesta en frecuencia del filtro analógico
# =================================================================
w_freq, H = signal.freqz(h, worN=2048, fs=fs_high)
plt.figure()
plt.plot(w_freq, 20*np.log10(np.abs(H)))
plt.title('b) Respuesta en frecuencia del filtro analógico')
plt.xlabel('Frecuencia (Hz)')
plt.ylabel('Magnitud (dB)')
plt.grid()
plt.show()

# =================================================================
# c) Señales s(t) y u(t)
# =================================================================
s = np.convolve(y, h, 'full')
s = s[M:-M+1]
u = np.convolve(w, h, 'full')
u = u[M:-M+1]

# =================================================================
#  d) Filtrado digital + ZOH + reconstrucción con sinc
# =================================================================
ud = np.convolve(wd, hd, 'full')
ud = ud[M//10 : -M//10 + 1] if M//10 > 0 else ud

def zoh(ud, T_low, t_out):
    idx = np.floor(t_out / T_low).astype(int)
    idx = np.clip(idx, 0, len(ud)-1)
    return ud[idx]

def reconstruir_sinc(ud, T_low, t_out):
    x_rec = np.zeros_like(t_out)
    for n_idx, val in enumerate(ud):
        t_n = n_idx * T_low
        x_rec += val * np.sinc((t_out - t_n) / T_low)
    return x_rec

t_d = np.arange(0, wd.size) / fs_low
t_full = np.arange(0, y.size) / fs_high

v_zoh = zoh(ud, T_low, t_full)

tramo = slice(0, 2000)
v_sinc = reconstruir_sinc(ud[:200], T_low, t_full[tramo])

plt.figure()
plt.plot(t_full[:2000], s[:2000], label='s(t)')
plt.plot(t_full[:2000], u[:2000], label='u(t)')
plt.plot(t_full[:2000], v_zoh[:2000], '--', label='v_zoh(t)')
plt.plot(t_full[tramo], v_sinc, ':', label='v_sinc(t)')
plt.legend()
plt.title('c-d) Comparación con ZOH y reconstrucción sinc')
plt.xlabel('Tiempo (s)')
plt.grid()
plt.show()

# =================================================================
# e) Verificación: ruido 10x mayor
# =================================================================
r10 = np.sqrt(10) * r
w10 = y + r10
u10 = np.convolve(w10, h, 'full')
u10 = u10[M:-M+1]

plt.figure()
plt.plot(t_full[:2000], u10[:2000], label='u10(t)')
plt.plot(t_full[:2000], v_zoh[:2000], '--', label='v_zoh(t)')
plt.legend()
plt.title('e) Verificación: ruido 10x mayor vs. procesamiento digital')
plt.xlabel('Tiempo (s)')
plt.grid()
plt.show()

# =================================================================
# f) Diseño del filtro anti-aliasing ha(t)
# =================================================================
n_ha = np.arange(-150, 150)
ha = np.sinc(n_ha/50)
ha = ha / np.sum(ha)

# ==================================================================
# g) Filtrado con anti-aliasing y repetición del procesamiento
# ==================================================================
w_filt = np.convolve(w, ha, 'full')
w_filt = w_filt[M:-M+1]
wd_filt = w_filt[::10]
hd_filt = 10 * ha[::10]
ud_filt = np.convolve(wd_filt, hd_filt, 'full')
ud_filt = ud_filt[M//10 : -M//10 + 1] if M//10 > 0 else ud_filt

v_filt_zoh = zoh(ud_filt, T_low, t_full)
v_filt_sinc = reconstruir_sinc(ud_filt[:200], T_low, t_full[tramo])

plt.figure()
plt.plot(t_full[:2000], s[:2000], label='s(t)')
plt.plot(t_full[:2000], u[:2000], label='u(t)')
plt.plot(t_full[:2000], v_filt_zoh[:2000], '--', label='v_filt_zoh(t)')
plt.plot(t_full[tramo], v_filt_sinc, ':', label='v_filt_sinc(t)')
plt.legend()
plt.title('g) Con filtro anti-aliasing (ZOH y sinc)')
plt.xlabel('Tiempo (s)')
plt.grid()
plt.show()