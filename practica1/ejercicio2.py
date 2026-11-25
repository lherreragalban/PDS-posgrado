import numpy as np

def decimate(x, M, n0):
    
    start = (-n0) % M       
    y = x[start::M]     
    
    n0_y = -(n0 + start) // M
    
    return y, n0_y

import matplotlib.pyplot as plt

n = np.arange(-50, 51)
n0 = n[0]  

# Caso I 
x1 = np.sin(0.125 * np.pi * n)
y1, n0_y1 = decimate(x1, 4, n0)

# CasoII
x2 = np.sin(0.5 * np.pi * n)
y2, n0_y2 = decimate(x2, 4, n0)

plt.figure(figsize=(14, 8))

# Caso I
plt.subplot(2, 2, 1)
plt.stem(n, x1, 'b', markerfmt='bo', label='x1[n]')
plt.title('Caso I: x1[n] = sen(0.125πn)')
plt.xlabel('n'); plt.ylabel('x1[n]'); plt.grid(); plt.legend()

plt.subplot(2, 2, 2)
n_y1 = np.arange(n0_y1, n0_y1 + len(y1))
plt.stem(n_y1, y1, 'r', markerfmt='ro', label='y1[n] diezmada M=4')
plt.title('Caso I: y1[n] = x1[4n]')
plt.xlabel('n'); plt.ylabel('y1[n]'); plt.grid(); plt.legend()

# Caso II
plt.subplot(2, 2, 3)
plt.stem(n, x2, 'b', markerfmt='bo', label='x2[n]')
plt.title('Caso II: x2[n] = sen(0.5πn)')
plt.xlabel('n'); plt.ylabel('x2[n]'); plt.grid(); plt.legend()

plt.subplot(2, 2, 4)
n_y2 = np.arange(n0_y2, n0_y2 + len(y2))
plt.stem(n_y2, y2, 'r', markerfmt='ro', label='y2[n] diezmada M=4')
plt.title('Caso II: y2[n] = x2[4n]')
plt.xlabel('n'); plt.ylabel('y2[n]'); plt.grid(); plt.legend()

plt.tight_layout()
plt.show()