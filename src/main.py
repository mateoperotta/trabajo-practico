import numpy as np
from utils.irsint import irsint
from utils.ruido_rosa import ruidoRosa
from utils.hilbert import hilbert_transform
from utils.schroeder import schroeder
from utils.lognorm import lognorm
from utils.grafico import grafico1
from utils.grafico import grafico2
from utils.moving_average import moving_average

t60 = {31.25:7.54,
       62.5:8.14,
       125:7.85,
       250:8.29,
       500:8.4,
       1000:7.71,
       2000:6.03,
       4000:4.03,
       8000:2
       }

# Sintetizo la IR del recinto
ir = irsint(t60)
fs = 44100
prepend_samples = int(fs*0.05) 
ir = np.concatenate([np.zeros(prepend_samples),ir])

# Calculamos la energía de la IR sintetizada
ir_power = np.mean(ir**2)
SNR_dB = 60
noise_power = ir_power / (10**(SNR_dB / 10))

# Generamos el ruido rosa
ruido = ruidoRosa(10)

# Escalamos el ruido rosa a la potencia deseada
ruido_power = np.mean(ruido**2)
factor = np.sqrt(noise_power / ruido_power)
ruido_escalado = ruido * factor

# Extendemos IR para que dure lo mismo que el ruido
extention = np.zeros(len(ruido) - len(ir))
ir_extend = np.concatenate([ir,extention])

# Señal con ruido de fondo
ir_ruido = ir_extend + ruido_escalado

# Obtengo la envolvente de la IR
analytic = hilbert_transform(ir_ruido)
envelope = np.abs(analytic)

# Filtro la envolvente
envelope_smooth = moving_average(envelope,1000)

# Se calcula Schroeder para la envolvente
envelope_lowpass = schroeder(ir_ruido)

# Se le aplica el filtro a la envolvente

envelope_filt = []
for i in range(len(envelope)):
    envelope_filt.append(envelope_smooth[i] * envelope_lowpass[i])

envelope_filt = np.array(envelope_filt)

# Paso las señales a escala logarítmica
ir_log = lognorm(ir_ruido)
envelope_log1 = lognorm(envelope_filt)
envelope_log2 = lognorm(envelope)
envelope_log3 = lognorm(envelope_smooth)
ruido_log = lognorm(ruido)

# Grafico
grafico2(ir_log,envelope_log1,envelope_log2,envelope_log3,"IR","Schroeder","Hilbert","Moving average","T60")

grafico1(ruido_log,"RUIDO")
