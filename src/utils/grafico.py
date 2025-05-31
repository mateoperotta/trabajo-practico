import numpy as np
import matplotlib.pyplot as plt

def grafico2(t,señal1,señal2,titulo1,titulo2,x,y):
    '''
    Grafica una o dos señales en el tiempo.

    Parámetros
    ----------
    
    t: float
        Duración de la señal.
    señal1: Numpy Array
        Señal que se desea graficar.
    señal2: int
        Puede igresarse una segunda señal para graficarla en el mismo dominio de tiempo.
    titulo1: string
        Titulo de la primer señal.
    titulo2: string
        Titulo de la segunda señal.
    x: string
        Nombre de la variable del eje x.
    y: string
        Nombre de la variable del eje y.
    returns: Matplotlib plot
        Gráfico/s de la/s señal/es en el tiempo.
    '''
    # Gráfico de dos señales
    fig, axs = plt.subplots(2, sharex=True)
    axs[0].set_title(titulo1)
    axs[0].set_ylabel(y)
    axs[1].set_title(titulo2)
    axs[1].set_xlabel(x)
    axs[1].set_ylabel(y)
    axs[0].plot(t,señal1)
    axs[1].plot(t,señal2)

    fig, axs = plt.subplots(2, sharex=True)

    axs[0].set_title(titulo1)
    axs[0].set_ylabel(y)
    axs[0].plot(t,señal1)

    axs[1].set_title(titulo2)
    axs[1].set_ylabel(y)
    axs[1].set_xlabel(x)
    axs[1].plot(t,señal2)

    plt.show()


