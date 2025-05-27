import numpy as np
import soundfile as sf

def irsint(diccionario):
    '''
    Recibe un diccionario con frecuencias de banda de octava y sus
    respectivos T60 para generar la calcular la respuesta al impulso
    y generar un archivo 'ri.wav'.
    '''




t60 = { 31.5:1,
        63.0:1,
        125.0:1,
        250.0:1,
        500.0:1,
        1000.0:1,
        2000.0:1,
        4000.0:1,
        8000.0:1,
        16000.0:1
}

irsint(t60)

