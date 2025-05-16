import numpy as np
import soundfile as sf
import sounddevice as sd

def playRec():
    '''
    Reproduce un archivo .wav y registra el audio tomado por el dispositivo 
    seleccionado seleccionado por el usuario en el tiempo elegido.
    
    Parámetros
    ----------

    t:

    signal:

    device:

    fs:

    returns:

    '''

    # Selección del dispositivo de audio

    print(sd.query_devices())

    sentinela = ""

    while sentinela != "s":
        print(f"\n{sd.query_devices()}")

        entrada = int(input("\nSeleccione el dispositivo de entrada: "))
        salida = int(input("Seleccione el dispositivo de salida: "))

        sd.default.device = (entrada,salida)  # type: ignore

        print(f"\n{sd.query_devices()}")
        
        sentinela = str(input("\nDesea guardar los cambios? [S/n]: ")).lower()

    # Grabador-reproductor

























    


playRec()
