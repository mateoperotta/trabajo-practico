import numpy as np
from scipy.signal import medfilt

def moving_average(signal,window):

    ma = medfilt(signal,window)
    ## Señal 1/L
    #L = np.ones(int(window)) / window

    ## Convolución
    #ma = np.convolve(signal,L,mode='same')

    return ma
