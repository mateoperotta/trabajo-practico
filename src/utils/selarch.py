from tkinter import Tk
from tkinter.filedialog import askopenfilename

def selarch():
    '''
    Abre una ventana para seleccionar un archivo.

    return: Ruta
        Devuelve la ruta del archivo en forma de variable.
    '''
    Tk().withdraw() 
    ruta = askopenfilename() 

    return ruta
