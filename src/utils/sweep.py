import numpy as np
import soundfile as sf

def sweepGen(T,w1=20,w2=20000,fs=44100):
    '''
    Genera un sine-sweep logarítmico y su filtro invertido 
    con la duración que le indique el usuario.

    Nota: si 'sweep.wav' y 'filtInv.wav' ya existen, serán sobreescritos.

    Parámetros
    ----------

    T: float Duración ingresada por el usuario de la señal.
    w1: int
        Frecuencia inicial del sweep.
    w2: int
        Frecuencia final del sweep.
    fs: int
        Frecuencia de muestre.
    returns: Numpy Array, Numpy Array
        Se devuelven los arrays correspondientes al sine-sweep y el filtro invertido.
    '''
    # Parámetros del sweep
    r = np.log(w2/w1)
    l = T / r
    k = (T / r) * 2 * np.pi * w1
    t = np.linspace(0,T,T*fs)

    # Sweep
    sweep = np.sin(k*((np.e**(t/l)) - 1))

    # Modulación
    w = (k * np.e**(t/l)) / l
    modulacion = w1 / (2*np.pi*w)
    
    # Filtro inverso
    sweepInv = np.flip(sweep)
    filtro = np.multiply(modulacion,sweepInv)

    # Normalización
    sweep /= np.max(np.abs(sweep))
    filtro /= np.max(np.abs(filtro))

    # Escalado a 16 bits
    #sweep *= 32767
    #k *= 32767

    # Generación de los archivos .wav
    sf.write('sweep.wav',sweep,fs)
    sf.write('filtro_invertido.wav',filtro,fs)

    return sweep, filtro

sweep = sweepGen(30)
