import numpy as np
import scipy.io as sio
import matplotlib.pyplot as plt

# inciso a
data = sio.loadmat('gold.mat')
x1 = data['x1'].flatten()
x2 = data['x2'].flatten()

print("Longitud de x1:", len(x1))
print("Longitud de x2:", len(x2))


def corr(x, y):
    rxy = np.convolve(x, np.conjugate(y[::-1]), 'full')
    L = y.size
    N = (L - 1) // 2
    rxyp = rxy[L:2*L]
    return np.hstack((rxyp[N:], rxyp[0:N-1])), np.arange(-N, N)


# inciso b 

ac1, lags1 = corr(x1, x1)
ac2, lags2 = corr(x2, x2)
ic, lags_ic = corr(x1, x2)


L1 = min(len(lags1), len(ac1))
L2 = min(len(lags2), len(ac2))
L3 = min(len(lags_ic), len(ic))

plt.figure(figsize=(14, 10))

plt.subplot(3, 1, 1)
plt.plot(lags1[:L1], np.real(ac1[:L1]), 'b')
plt.title('Autocorrelación de x1 (Satélite 1)')
plt.xlabel('Retardo'); plt.ylabel('R_x1x1'); plt.grid(True)

plt.subplot(3, 1, 2)
plt.plot(lags2[:L2], np.real(ac2[:L2]), 'r')
plt.title('Autocorrelación de x2 (Satélite 2)')
plt.xlabel('Retardo'); plt.ylabel('R_x2x2'); plt.grid(True)

plt.subplot(3, 1, 3)
plt.plot(lags_ic[:L3], np.real(ic[:L3]), 'g')
plt.title('Intercorrelación entre x1 y x2')
plt.xlabel('Retardo'); plt.ylabel('R_x1x2'); plt.grid(True)

plt.tight_layout()
plt.show()

#  inciso c

D1 = 499
D2 = 449

s1 = np.hstack((x1[D1:], x1, x1, x1, x1, x1[:D1]))
s2 = np.hstack((x2[D2:], x2, x2, x2, x2, x2[:D2]))

np.random.seed(42)
r = s1 + s2 + 10 * np.random.normal(size=s1.size)

print("Longitud de r:", len(r))


# inciso d

x1_5 = np.tile(x1, 5)
x2_5 = np.tile(x2, 5)

corr1, lags1 = corr(r, x1_5)
corr2, lags2 = corr(r, x2_5)

L1 = min(len(lags1), len(corr1))
L2 = min(len(lags2), len(corr2))

plt.figure(figsize=(14, 8))

plt.subplot(2, 1, 1)
plt.plot(lags1[:L1], np.real(corr1[:L1]), 'b')
plt.title('Intercorrelación de r con 5 períodos de x1')
plt.xlabel('Retardo'); plt.ylabel('R_r,x1'); plt.grid(True)
plt.axvline(D1, color='r', linestyle='--', label=f'D1={D1}')
plt.legend()

plt.subplot(2, 1, 2)
plt.plot(lags2[:L2], np.real(corr2[:L2]), 'r')
plt.title('Intercorrelación de r con 5 períodos de x2')
plt.xlabel('Retardo'); plt.ylabel('R_r,x2'); plt.grid(True)
plt.axvline(D2, color='b', linestyle='--', label=f'D2={D2}')
plt.legend()

plt.tight_layout()
plt.show()


pico1 = lags1[np.argmax(np.abs(corr1[:L1]))]
pico2 = lags2[np.argmax(np.abs(corr2[:L2]))]
print(f"Pico de correlación con x1 en retardo: {pico1}")
print(f"Pico de correlación con x2 en retardo: {pico2}")