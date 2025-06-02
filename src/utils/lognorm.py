import numpy as np

def lognorm(señal):
    '''
    Convierte la señal ingresada en escala logarítmica.

    Parámetros
    ----------
    señal: Numpy Array
        Array correspondiente a la señal que se desea convertir.
    return: Numpy Array
        Devuelve la señal en escala logarítmica.
    '''
    # Transformación a escala logarítmica
    r = 20 * np.log10(señal / np.max(señal))

    return r
