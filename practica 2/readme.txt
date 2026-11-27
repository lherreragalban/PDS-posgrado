Requisitos

Python 3.8+

Bibliotecas:

numpy matplotlib scipy

Estructura de archivos

ejercicio2.py	Espectros de amplitud de señales muestreadas (aliasing)
ejercicio3.py	Procesamiento digital vs. analógico de señales NRZ con ruido

Descripción de cada script

ejercicio2-d.py — Espectros de señales muestreadas

Analiza el espectro de amplitud bilateral de señales muestreadas, mostrando el efecto del aliasing cuando la frecuencia de muestreo no cumple el teorema de Nyquist. Los tres casos se grafican en una sola figura con tres subgráficos verticales.

a) x(t) = 1 + 2cos(8πt) muestreada a fs = 6 Hz. La componente DC se replica en 0, 6, 12 Hz, y la componente de 4 Hz se replica en 2, 4, 8, 10, 14 Hz, generando solapamiento espectral.
b) y(t) = 4 + 4·sinc²(4t) muestreada a fs = 6 Hz. El espectro triangular de sinc²(4t) (base de -4 a 4 Hz) se replica cada 6 Hz, produciendo solapamiento entre réplicas. Se añade la componente DC del término constante como picos en múltiplos de 6 Hz.
c) x(t) = 1 + 2cos(8πt) muestreada a fs = 4 Hz. La componente de 4 Hz cae exactamente sobre la frecuencia de muestreo, aliasándose a DC. Todas las réplicas caen en múltiplos de 4 Hz y se suman coherentemente, dando amplitud 3 en cada una.

Salida: una figura con 3 subgráficos de espectro bilateral (amplitud vs. frecuencia).

ejercicio3.py — Procesamiento digital vs. analógico con ruido

Simula la transmisión de una señal NRZ (bits aleatorios ±1, 100 muestras por bit, 100 bits) a través de un canal con ruido gaussiano, comparando el procesamiento analógico y el digital, incluyendo reconstrucción por retención de orden cero (ZOH) y por interpolación sinc.

a) Genera la señal NRZ x, la filtra con un sinc truncado h (filtro pasabajos) para obtener y, y añade ruido de igual potencia para obtener w. Muestrea w a 10 kHz (wd) y define el filtro digital hd.
b) Grafica la respuesta en frecuencia del filtro analógico h (magnitud en dB).
c) Calcula s(t) (filtrado sin ruido) y u(t) (filtrado con ruido).
d) Filtra wd con hd para obtener ud, y reconstruye la señal de dos formas:
    ZOH: retención de orden cero (escalera).
    Sinc: interpolación ideal con función sinc.
    Se comparan s(t), u(t), v_zoh(t) y v_sinc(t).
e) Verifica la equivalencia incrementando el ruido 10 veces (u10) y comparando con el resultado digital v_zoh.
f) Diseña un filtro anti-aliasing ha(t) (sinc truncado).
g) Filtra w con ha, repite el procesamiento digital y la reconstrucción (ZOH y sinc), y compara con las señales anteriores.

Salida: 4 gráficos (respuesta en frecuencia, comparación con ZOH y sinc, verificación con ruido 10x, resultado con anti-aliasing).