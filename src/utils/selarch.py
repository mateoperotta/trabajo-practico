from tkinter import Tk
from tkinter.filedialog import askopenfilename

def selarch():
    '''
    Abre una ventana para seleccionar un archivo.

    return: Archivo
        Devuelve la ruta del archivo en forma de variable.
    '''
    Tk().withdraw() 
    archivo = askopenfilename() 

    return archivo

archivo = selarch()
