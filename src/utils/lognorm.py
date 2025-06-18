import numpy as np

def lognorm(signal):
    '''
    Convierte la señal ingresada en escala logarítmica.

    Parámetros
    ----------
    señal: Numpy Array
        Array correspondiente a la señal que se desea convertir.
    return: Numpy Array
        Devuelve la señal en escala logarítmica.
    '''
    # Señal con valores absolutos
    signal_abs = np.abs(signal)

    # Valor máximo de la señal
    signal_max = np.max(np.abs(signal))

    # Si la energía de la señal es nula
    if signal_max == 0:
        return np.full_like(signal, -np.inf)

    # Cociente entre el valor absoluto y el máximo
    signal_norm = signal_abs / signal_max
    signal_norm_segura = np.clip(signal_norm, 1e-12, None)

    # Transformación a escala logarítmica
    r = 20 * np.log10(signal_norm_segura)
    
    return r
