import numpy as np
from scipy import signal
import soundfile as sf

def filtro(ir):
    '''
    Genera filtros de cada frecuencia centra de la respuesta al impulso.
    Genera un archivo wav por cada frecuencia filtada.

    Nota: si los archivos wav ya existen, serán reemplazadas.

    Parámetros
    ----------
    ir: Ruta
        Ruta donde se encuentra la respuesta al impulso en formato wav.
    return: Lista
        Lista con los arrays correspondientes a los filtros por banda de octava.
    '''
    # Lista donde se guardan las señales filtradas
    filtros = []

    # Bandas por octava
    bandasOctava = [ 
        31.25,
        62.5,
        125,
        250,
        500,
        1000,
        2000,
        4000,
        8000
    ]

    # Se ingresa la respuesta al impulso como archivo wav
    audio, fs = sf.read(f'{ir}')

    for fi in bandasOctava:
        #Selección de octava - G = 1.0/2.0 / 1/3 de Octava - G=1.0/6.0
        G = 1.0/2.0
        fo = 0
        factor = np.power(2, G)
        centerFrequency_Hz = fi 

        #Calculo los extremos de la banda a partir de la frecuencia central
        lowerCutoffFrequency_Hz=centerFrequency_Hz/factor;
        upperCutoffFrequency_Hz=centerFrequency_Hz*factor;

        #print('Frecuencia de corte inferior: ', round(lowerCutoffFrequency_Hz), 'Hz')
        #print('Frecuencia de corte superior: ', round(upperCutoffFrequency_Hz), 'Hz')

        # El orden del filtro varía con la frecuencia central

        # Orden 8 para frecuencias menores a 200Hz
        if fi <= 200:
            fo = 8
        # Orden 6 para frecuencias entre 200Hz y 1kHz
        if fi > 200 and fi < 1000:
            fo = 6
        # Orden 4 para frecuencias mayores a 1kHz
        if fi >= 1000:
            fo = 4

        # Extraemos los coeficientes del filtro 
        b,a = signal.iirfilter(fo, [2*np.pi*lowerCutoffFrequency_Hz,2*np.pi*upperCutoffFrequency_Hz],
                                    rs=60, btype='band', analog=True,
                                    ftype='butter') 

        # para aplicar el filtro es más óptimo
        sos = signal.iirfilter(fo, [lowerCutoffFrequency_Hz,upperCutoffFrequency_Hz],
                                    rs=60, btype='band', analog=False,
                                    ftype='butter', fs=fs, output='sos') 

        w, h = signal.freqs(b,a)

        # Aplicando filtro al audio
        filt = signal.sosfilt(sos, audio)

        # Se guarda la señal filtrada en una lista
        filtros.append(filt)

        # Se genera un archivo .wav correspondiente a la señal filtrada en fi
        sf.write(f'filtro_{fi}Hz.wav',filt,fs)

    return filtros
