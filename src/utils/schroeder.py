import numpy as np

def schroeder_integral(signal):
    """
    Calcula la integral de Schroeder de una señal.
    La señal debe ser unidimensional (respuesta al impulso).
    
    Parámetros:
        signal (array-like): señal de entrada (RI).
        
    Retorna:
        schroeder (np.ndarray): integral acumulada inversa (energía).
    """
    # Energía de la señal (cuadrado de la amplitud)
    energy = signal**2

    # Integral acumulativa inversa: sumamos desde el final hacia el inicio
    schroeder = np.cumsum(energy[::-1])[::-1]

    return schroeder

