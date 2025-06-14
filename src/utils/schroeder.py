import numpy as np

def schroeder(signal):

    # Energía de la señal
    signal_energy = np.cumsum(np.abs(signal)**2)

    # Extremo superior de la integral
    signal_max = np.argmax(np.abs(signal))

    # Se recorta la IR hasta el extremo superior
    prepend = signal[:signal_max]

    prepend_energy = np.cumsum(np.abs(prepend)**2)

    # Rellenamos con ceros el prepend
    #relleno = np.zeros(len(signal_energy) - len(prepend_energy))
    relleno = np.ones(len(signal_energy) - len(prepend_energy))
    prepend_energy = np.concatenate([prepend_energy,relleno])

    #envelope_filt = []
    #for i in range(len(signal)):
    #    envelope_filt.append(signal[i] * [i])

    # Schroeder
    #result = signal_energy - prepend_energy

    return prepend_energy
