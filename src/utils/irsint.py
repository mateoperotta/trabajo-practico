import numpy as np
import soundfile as sf

def irsint(frecuencias,fs=44100):
    '''
    Recibe un diccionario con frecuencias de banda de octava y sus
    respectivos T60 para generar la calcular la respuesta al impulso
    y generar un archivo 'ir.wav'.
    
    Parámetros
    ----------
    frecuencias: dictionary
        Diccionario que contenga como keys las frecuencias centrales y como values sus respectivos T60.
    fs: int
        Frecuencia de muestreo deseada.
    return: Numpy Array
        Sintetiza la respuesta al impulso de un recinto conocido.
    '''
    # Lista que contendrá los impulsos de cada frecuencia
    arrays = []

    # Arrays de IR de fi
    for fi, t60 in frecuencias.items():
        tau = -(np.log(10**(-3))) / t60
        muestras = int(t60*fs)

        # Array de tiempo
        t = np.linspace(0,t60,num=muestras,endpoint=False)

        # Respuesta al impulso
        y = (np.exp(-tau*t)) * (np.cos(2*np.pi*fi*t))

        # Se agrega la señal a la lista
        arrays.append(y)

    # Se completan con ceros los arrays más cortos para que todos tengan la misma logitud
    maxLen = max(len(arr) for arr in arrays)
    arraysEmparejados = []
    for arr in arrays:
        pad_width = maxLen - len(arr)
        arr_padded = np.pad(arr, (0, pad_width), mode='constant', constant_values=0)
        arraysEmparejados.append(arr_padded)
    arrays = np.vstack(arraysEmparejados)

    # Suma de frecuencias centrales
    ir = np.sum(arrays,axis=0)
    t = np.linspace(0,np.size(ir)/fs,np.size(ir),endpoint=False)
    ir /= np.max(abs(ir))

    # Generación del .wav de la respuesta al impulso
    sf.write('ir.wav',ir,fs)

    return ir
