import numpy as np
import soundfile as sf
import sounddevice as sd

def grabador(fs=44100):
    '''
    Reproduce un sine-sweep y registra el audio tomado por el dispositivo 
    seleccionado por el usuario en el tiempo elegido. El registro
    se guarda en el archivo 'grabacion.wav'

    Nota: si 'grabacion.wav' existe, este será sobreescrito.

    Parámetros
    ----------

    fs: int
        Frecuencia de muestreo a la que se quiere grabar.
    return: Numpy Array
        Array de la grabación.
    '''
    ## Selección del dispositivo de audio

    sentinela = ""

    while sentinela != "s":

        # Imprime los dispositivos disponibles
        print(f"\n{sd.query_devices()}")

        # Ingreso de los dispositivos i/o del usuario
        entrada = int(input("\nSeleccione el dispositivo de entrada: "))
        salida = int(input("Seleccione el dispositivo de salida: "))
        sd.default.device = (entrada,salida)  # type: ignore

        # Se imprimen los dispositivos seleccionados
        print(f"\n{sd.query_devices()}")
        
        # Confirmación de los datos
        sentinela = str(input("\n¿Desea guardar los cambios? [S/n]: ")).lower()

    ## Grabador y reproductor

    # Carga del audio del sweep
    sweep, fs = sf.read('sweep.wav')

    # Grabación y reproducción
    grabacion = sd.playrec(sweep,channels=2)
    sd.wait()

    # Se guarda la grabación en un archivo 'grabacion.wav'
    sf.write('grabacion.wav',grabacion,fs)
