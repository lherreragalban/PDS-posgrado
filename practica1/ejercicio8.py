import numpy as np
import matplotlib.pyplot as plt

def coef_fourier(A, K):
    """
    A: nivel de saturación (0 < A < 1)
    K: número máximo de armónicos (calcula de -K a K)
    """
    k_vals = np.arange(-K, K+1)
    X = np.zeros(len(k_vals), dtype=float)
    
    for i, k in enumerate(k_vals):
        if k == 0:
            X[i] = 0
        elif k % 2 == 0:
            X[i] = 0
        else:
            t = np.linspace(0, 1, 10000)
            x_t = np.where(np.abs(np.cos(2*np.pi*t)) <= A,
                           np.cos(2*np.pi*t),
                           np.where(np.cos(2*np.pi*t) > A, A, -A))
            integrand = x_t * np.cos(2*np.pi*k*t)
            
            if hasattr(np, 'trapezoid'):
                X[i] = 2 * np.trapezoid(integrand, t)
            else:
                X[i] = 2 * np.trapz(integrand, t)
    return k_vals, X

# inciso c

K = 10
plt.figure(figsize=(14, 4))

for i, A in enumerate([0.9, 0.5, 0.1]):
    k_vals, X = coef_fourier(A, K)
    plt.subplot(1, 3, i+1)
    plt.stem(k_vals, X, 'b', markerfmt='bo', basefmt='k-')
    plt.title(f'A = {A}')
    plt.xlabel('k')
    plt.ylabel('X^S[k]')
    plt.grid(True)
    plt.xlim(-K-0.5, K+0.5)

plt.tight_layout()
plt.show()

# inciso d

for A in [0.9, 0.5, 0.1]:
    k_vals, X = coef_fourier(A, K)
    idx1 = np.where(k_vals == 1)[0][0]
    P1 = X[idx1]**2
    print(f"A = {A}:")
    for k in range(2, 11):
        idxk = np.where(k_vals == k)[0][0]
        if P1 > 0:
            ratio = X[idxk]**2 / P1
            print(f"   k = {k:2d}  ->  {ratio:.6f}")
    print()

# inciso e

A = 0.5
K_max = 9
k_vals, X = coef_fourier(A, K_max)

t = np.linspace(-2, 2, 1000)
x_t = np.where(np.abs(np.cos(2*np.pi*t)) <= A,
               np.cos(2*np.pi*t),
               np.where(np.cos(2*np.pi*t) > A, A, -A))

plt.figure(figsize=(12, 6))
plt.plot(t, x_t, 'k', linewidth=2, label='x(t) original')

for K_trunc in [1, 3, 5, 7, 9]:
    x_hat = np.zeros_like(t)
    for k in range(1, K_trunc+1, 2):  
        idxk = np.where(k_vals == k)[0][0]
        x_hat += 2 * X[idxk] * np.cos(2*np.pi*k*t)
    plt.plot(t, x_hat, '--', label=f'K = {K_trunc}')

plt.title('Aproximaciones truncadas de x(t) para A = 0.5')
plt.xlabel('t')
plt.ylabel('x(t)')
plt.legend()
plt.grid(True)
plt.show()