import numpy as np

def moving_average(signal,window):

    # Señal 1/L
    L = np.ones(int(window)) / window

    # Convolución
    ma = np.convolve(signal,L,mode='same')

    return ma
