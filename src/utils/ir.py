import numpy as np
import soundfile as sf
import matplotlib.pyplot as plt

def ir():
    '''
    '''
    
    # Se cargan los archivos de audio del sweep en el recinto y el filtro inverso
    k, fs = sf.read('./filtro_inverso.wav')
    y, fs = sf.read('./mediciones/Toma_n3_a-03.wav')

    # Se aplica la transformada de Fourier en ámbas señales
    n = len(y) + len(k) - 1
    K = np.fft.fft(k,n=n)
    Y = np.fft.fft(y,n=n)

    # Se multiplican las señales
    H = Y * K

    # Tranformada inversa de Fourier de h
    h = np.fft.ifft(H)
    h = np.real(h)

    # Se obtiene el valor máximo de h
    h_max = np.argmax(abs(h))

    # Recortá una ventana desde el pico, por ejemplo 3 segundos
    duracion_segundos = 30
    muestras = int(fs * duracion_segundos)
    inicio = h_max 
    fin = h_max + muestras

    # Asegurate de no salirte del array
    h = h[inicio:fin] if fin < len(h) else h[inicio:]
    
    # Normalización y formato float32
    h /= np.max(np.abs(h))
    h = h.astype(np.float32)

    sf.write('impulse_response.wav',h,fs)

    return h
    
h = ir()
print(h)
plt.plot(h)
plt.title("Respuesta al Impulso")
plt.xlabel("Muestras")
plt.ylabel("Amplitud")
plt.grid()
plt.show()

