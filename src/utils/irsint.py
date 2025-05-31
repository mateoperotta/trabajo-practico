import numpy as np
import soundfile as sf
import matplotlib.pyplot as plt

def irsint(frecuencias,fs=48000):
    '''
    Recibe un diccionario con frecuencias de banda de octava y sus
    respectivos T60 para generar la calcular la respuesta al impulso
    y generar un archivo 'ri.wav'.
    '''

    arrays = []
    # Arrays de IR de fi
    for fi, t60 in frecuencias.items():
        tau = -(np.log(10**(-3))) / t60
        muestras = int(t60*fs)

        # Array de tiempo
        t = np.linspace(0,t60,num=muestras,endpoint=False)

        # Respuesta al impulso
        y = (np.exp(-tau*t)) * (np.cos(2*np.pi*fi*t))

        arrays.append(y)


    # Relleamos con ceros los arrays más cortos para que todos tengan la misma logitud
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

# York Guildhall Council Chamber

t60 = { 
    31.25:7.54,
    62.5:8.14,
    125:7.85,
    250:8.29,
    500:8.4,
    1000:7.71,
    2000:6.03,
    4000:4.03,
    8000:2,
    16000:18.86
}

# 
irsint(t60)

