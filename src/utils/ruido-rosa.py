import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import soundfile as sf
import sounddevice as sd

def ruidoRosa_voss(t,fs=44100,ncols=16):
    """
    Genera ruido rosa utilizando el algoritmo de Voss-McCartney (https://www.dsprelated.com/showabstract/3933.php).
    
    Nota: si 'ruidoRosa.wav' existe, este será sobreescrito.
    
    Parámetros
    ----------
    t: float
        Valor temporal en segundos, este determina la duración del ruido generado.
    fs: int
        Frecuencia de muestreo en Hz de la señal. Por defecto el valor es 44100 Hz.
    ncols: int
        Determina el número de fuentes a aleatorias a agregar.
    returns: NumPy array
        Datos de la señal generada.
    """
    # Generación del array con contenido aleatorio.
    array = np.full((fs*t, ncols), np.nan)
    array[0, :] = np.random.random(ncols)
    array[:, 0] = np.random.random(fs*t)
    n = fs*t
    cols = np.random.geometric(0.5, n)
    cols[cols >= ncols] = 0
    rows = np.random.randint(fs*t, size=n)
    array[rows, cols] = np.random.random(n)
 
    # Se reemplaza los valores vacios con contenido.
    df = pd.DataFrame(array)
    filled = df.ffill()
    total = filled.sum(axis=1)

    # Centrado de el array en 0.
    total -= total.mean()
    
    # Normalizado de la señal.
    valor_max = max(abs(max(total)),abs(min(total)))
    total = total / valor_max

    # Generación del archivo 'ruidoRosa.wav'.
    sf.write('ruidoRosa.wav',total,fs)
    
    return total, fs

def ruidoPlot(señal, fs):
    """
    Visualiza una señal en el dominio temporal.

    Parámetros
    ----------
    señal: Numpy Array 
        Correspondiente a la señal del ruido rosa.
    fs: int
        Frecuencia de muestreo en la que fue generada la señal.
    returns: Plot
        Grafica el ruido rosa en en función del tiempo.
    """
    # Calcula el tiempo correspondiente a cada valor de la señal
    tiempo = np.arange(len(señal)) / fs

    # Crea la gráfica
    plt.figure(figsize=(10, 6))  # Ajusta el tamaño de la figura si lo deseas
    plt.plot(tiempo, señal)

    # Agrega etiquetas y título
    plt.xlabel("Tiempo (s)")
    plt.ylabel("Amplitud")
    plt.title("Señal en el Dominio Temporal")

    # Agrega una malla (opcional)
    plt.grid(True)

    # Muestra la gráfica
    plt.show()

# Guardamos el contenido del ruido y del sample rate en una variable.
ruidoRosa, fs = ruidoRosa_voss(10)

# Se grafica en el dominio temporal el ruido rosa.
ruidoPlot(ruidoRosa,fs)

# Se lee el .wav generado y se reproduce.
audio, fs = sf.read('ruidoRosa.wav')
sd.play(audio,fs)
