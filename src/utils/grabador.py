import numpy as np
import soundfile as sf
import sounddevice as sd

def playRec(fs=44100):
    '''
    Reproduce un archivo .wav y registra el audio tomado por el dispositivo 
    seleccionado seleccionado por el usuario en el tiempo elegido.
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

# Se llama a la función
playRec()

