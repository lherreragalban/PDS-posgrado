import numpy as np
import scipy.io as sio

def shift(register, feedback, output):
    """Simula un registro de desplazamiento de 10 bits"""
    # Salida: XOR de las posiciones de salida
    out = [register[i-1] for i in output]
    out = sum(out) % 2 if len(out) > 1 else out[0]
    
    # Realimentación: XOR de las posiciones de realimentación
    fb = sum([register[i-1] for i in feedback]) % 2
    
    # Desplazar a la derecha
    for i in reversed(range(len(register[1:]))):
        register[i+1] = register[i]
    
    # Poner la realimentación en la primera posición
    register[0] = fb
    return out

def generar_secuencia_gps(sat_id):
    """Genera la secuencia C/A para un satélite GPS (1 al 32)"""
    # Registros iniciales (todos unos)
    G1 = [1] * 10
    G2 = [1] * 10
    
    # Tabla de selección de fase para G2 (del estándar GPS)
    # Para satélites 1 y 2: Sat 1 -> 2⊕6, Sat 2 -> 3⊕7
    if sat_id == 1:
        G2_taps = [2, 6]
    elif sat_id == 2:
        G2_taps = [3, 7]
    else:
        raise ValueError("Este script solo genera los satélites 1 y 2")
    
    secuencia = []
    for _ in range(1023):
        # Realimentación para G1: posiciones 3 y 10
        shift(G1, [3, 10], [10])
        # Realimentación para G2: posiciones 2,3,6,8,9,10
        shift(G2, [2, 3, 6, 8, 9, 10], [10])
        
        # Salida: G1 XOR (G2 taps XOR)
        g1_out = G1[9]  # Última posición
        g2_out = G2[G2_taps[0]-1] ^ G2[G2_taps[1]-1]
        secuencia.append(g1_out ^ g2_out)
    
    return np.array(secuencia)

# Generar secuencias para satélites 1 y 2
x1 = generar_secuencia_gps(1)
x2 = generar_secuencia_gps(2)

# Convertir a formato +1/-1 (como suele usarse en GPS)
x1 = 2 * x1 - 1
x2 = 2 * x2 - 1

# Guardar como gold.mat
sio.savemat('gold.mat', {'x1': x1, 'x2': x2})
print("Archivo 'gold.mat' generado con éxito.")
print(f"Longitud de x1: {len(x1)}, Longitud de x2: {len(x2)}")