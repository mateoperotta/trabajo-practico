import from utils.sweep sweep
import from utils.grabadorplayRec,  playRec

sweep, fs = sf.read('sweep.wav')
grabacion, fs = sf.read('grabacion.wav')

visualizar_dominio_temporal(sweep, fs)
visualizar_dominio_temporal(grabacion, fs)
