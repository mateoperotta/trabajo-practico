import numpy as np
import matplotlib.pyplot as plt

def grafico1(señal,titulo,fs=44100):
    '''
    Grafica la señal ingresada en el tiempo.

    Parámetros:
    ----------
    señal: Numpy Array
        Señal que desea graficar.
    titulo: string
        Titulo del gráfico.
    fs: int
        Frecuencia de muestreo.
    return: Plot
        Grafica la señal ingresada en el tiempo.
    '''
    # Calcula el tiempo correspondiente a cada valor de la señal
    tiempo = np.arange(len(señal)) / fs

    # Crea la gráfica
    plt.figure(figsize=(10, 6))  # Ajusta el tamaño de la figura si lo deseas
    plt.plot(tiempo, señal)

    # Agrega etiquetas y título
    plt.xlabel("Tiempo (s)")
    plt.ylabel("Amplitud")
    plt.title(titulo)

    # Agrega una malla (opcional)
    plt.grid(True)

    # Muestra la gráfica
    plt.show()

def grafico2(señal1, señal2, etiqueta1, etiqueta2, titulo, fs=44100):
    '''
    Grafica dos señales superpuestas en el dominio del tiempo.

    Parámetros:
    ----------
    señal1: Numpy Array
        Primera señal a graficar.
    señal2: Numpy Array
        Segunda señal a graficar.
    etiqueta1: string
        Etiqueta de la primera señal (para la leyenda).
    etiqueta2: string
        Etiqueta de la segunda señal.
    titulo: string
        Título del gráfico.
    fs: int
        Frecuencia de muestreo.
    '''
    # Tiempo para el eje x (usa el largo máximo entre ambas señales)
    n = max(len(señal1), len(señal2))
    tiempo = np.arange(n) / fs

    # Crear gráfico
    plt.figure(figsize=(10, 6))
    plt.plot(tiempo, señal1, label=etiqueta1, color='blue')
    plt.plot(tiempo, señal2, label=etiqueta2, color='red')


    # Etiquetas y título
    plt.xlabel("Tiempo (s)")
    plt.ylabel("Amplitud")
    plt.ylim(-100,0)
    plt.title(titulo)
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()

def grafico3(t,señal1,señal2,titulo1,titulo2,x='Tiempo (s)',y='Amplitud (dB)'):
    '''
    Grafica una o dos señales en el tiempo.

    Parámetros:
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
    return: Matplotlib plot
        Gráficos de las señales en el tiempo.
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
    plt.show()
