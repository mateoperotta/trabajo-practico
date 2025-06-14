import numpy as np
from scipy.signal import hilbert

def hilbert_transform(signal):

    analytic = hilbert(signal)

    return analytic

#def hilbert(signal,fs=44100):

#    n = len(signal)
#    S = np.fft.fft(signal)
#
#    H = np.zeros(n)
#
#    if n % 2 == 0:
#        H[0] = 1
#        H[1:n//2] = 2
#        H[n//2] = 1
#
#    else:
#        H[0] = 1
#        H[1:(n+1)//2] = 2
#
#    s_h = S * H
#
#    s_a = np.fft.ifft(s_h)



    


