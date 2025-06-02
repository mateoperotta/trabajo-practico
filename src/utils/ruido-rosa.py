import numpy as np
import pandas as pd
import soundfile as sf

def ruidoRosa(t,fs=44100,ncols=16):
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
    returns: Numpy Array
        Devuelve el array correspondiente al ruido rosa.
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
    ruido = filled.sum(axis=1)

    # Centrado de el array en 0.
    ruido -= ruido.mean()
    
    # Normalizado de la señal.
    valor_max = max(abs(max(ruido)),abs(min(ruido)))
    ruido = ruido / valor_max

    # Generación del archivo 'ruidoRosa.wav'.
    sf.write('ruido_rosa.wav',ruido,fs)
    
    return ruido
