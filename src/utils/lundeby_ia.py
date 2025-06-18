import numpy as np
from scipy.stats import linregress

def lundeby_cutoff_time(ir, fs, margin_db=10, window_ms=10):
    """
    Aplica el método de Lundeby para determinar el tiempo útil de integración en una IR.
    
    Parámetros:
    - ir: IR con ruido
    - fs: frecuencia de muestreo
    - margin_db: margen sobre el ruido de fondo (usualmente 10 dB)
    - window_ms: tamaño de ventana de análisis en milisegundos
    
    Retorna:
    - tiempo_cruce: tiempo útil de integración en segundos
    - idx_cruce: índice de muestra correspondiente
    """
    
    ir = ir / np.max(np.abs(ir))  # Normalizar
    energy = ir**2
    window_samples = int(fs * window_ms / 1000)
    total_windows = len(energy) // window_samples

    # Calcular energía por ventana
    rms_db = []
    times = []

    for i in range(total_windows):
        start = i * window_samples
        end = start + window_samples
        window = energy[start:end]
        if len(window) == 0:
            continue
        rms = np.sqrt(np.mean(window))
        rms_db.append(10 * np.log10(rms + 1e-12))
        times.append((start + end) / 2 / fs)

    rms_db = np.array(rms_db)
    times = np.array(times)

    # Estimar ruido de fondo: promedio de últimas N ventanas
    N_noise = max(3, int(0.1 * total_windows))
    noise_db = np.mean(rms_db[-N_noise:])
    threshold_db = noise_db + margin_db

    # Buscar ventana donde el nivel baja de threshold
    idx_valid = np.where(rms_db > threshold_db)[0]

    if len(idx_valid) < 2:
        print("⚠️ No hay suficiente tramo útil para estimar Lundeby.")
        return 0.0, 0

    # Regresión lineal sobre esa parte
    t_fit = times[idx_valid]
    db_fit = rms_db[idx_valid]
    slope, intercept, *_ = linregress(t_fit, db_fit)

    # Resolver cruce con el ruido + margen
    tiempo_cruce = (threshold_db - intercept) / slope

    if tiempo_cruce < 0 or tiempo_cruce > times[-1]:
        print("⚠️ El cruce está fuera de rango. Señal muy ruidosa o muy corta.")
        return 0.0, 0

    idx_cruce = int(tiempo_cruce * fs)
    return tiempo_cruce, idx_cruce

