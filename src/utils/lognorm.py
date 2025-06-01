import numpy as np

def lognorm(señal):
    '''
    '''

    r = np.log10(señal / np.max(señal))

    return r
