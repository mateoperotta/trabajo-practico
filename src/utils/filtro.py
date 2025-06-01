import numpy as np
from scipy import signal
import soundfile as sf

def filtro():
    '''
    '''

    filtros = []

    audio, fs = sf.read('./impulse_response.wav')

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

    for fi in bandasOctava:
        #Selección de octava - G = 1.0/2.0 / 1/3 de Octava - G=1.0/6.0
        G = 1.0/2.0
        fo = 0
        factor = np.power(2, G)
        centerFrequency_Hz = fi 

        #Calculo los extremos de la banda a partir de la frecuencia central
        lowerCutoffFrequency_Hz=centerFrequency_Hz/factor;
        upperCutoffFrequency_Hz=centerFrequency_Hz*factor;

        print('Frecuencia de corte inferior: ', round(lowerCutoffFrequency_Hz), 'Hz')
        print('Frecuencia de corte superior: ', round(upperCutoffFrequency_Hz), 'Hz')

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

llamada = filtro()
