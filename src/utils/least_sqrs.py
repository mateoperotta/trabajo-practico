import numpy as np

def regresion_lineal_iso3382(x, y):
    """
    Realiza una regresión lineal por mínimos cuadrados siguiendo las fórmulas
    típicamente encontradas en el Anexo C de ISO 3382:2008.

    Args:
        x_data (array-like): Datos de la variable independiente (e.g., tiempo).
        y_data (array-like): Datos de la variable dependiente (e.g., nivel de sonido en dB).

    Returns:
        tuple: Una tupla que contiene:
            - pendiente (float): La pendiente 'm' de la línea de regresión.
            - ordenada_origen (float): La ordenada al origen 'b' de la línea de regresión.
            - y_pred (numpy.ndarray): Los valores 'y' predichos por la línea de regresión.
    """
    #n = len(x_data)

    #if n == 0:
    #    raise ValueError("Los datos de entrada no pueden estar vacíos.")
    #if n != len(y_data):
    #    raise ValueError("x_data y y_data deben tener la misma longitud.")
    #if n < 2:
    #    raise ValueError("Se necesitan al menos 2 puntos para realizar una regresión lineal.")

    ## Convertir a arrays de NumPy para facilitar las operaciones
    #x = np.array(x_data)
    #y = np.array(y_data)

    n = len(x)

    # Calcular las sumatorias necesarias
    sum_xy = np.sum(x * y)
    sum_x = np.sum(x)
    sum_y = np.sum(y)
    sum_x_squared = np.sum(x**2)

    # Calcular la pendiente (m)
    # m = (n * sum(xi*yi) - sum(xi) * sum(yi)) / (n * sum(xi^2) - (sum(xi))^2)
    numerador_m = n * sum_xy - sum_x * sum_y
    denominador_m = n * sum_x_squared - sum_x**2

    if denominador_m == 0:
        raise ValueError("No se puede calcular la pendiente (denominador es cero). Esto puede ocurrir si todos los valores de x son iguales.")

    pendiente = numerador_m / denominador_m

    # Calcular la ordenada al origen (b)
    # b = mean(y) - m * mean(x)
    media_x = np.mean(x)
    media_y = np.mean(y)

    ordenada_origen = media_y - pendiente * media_x

    # Calcular los valores y predichos
    y_pred = pendiente * x + ordenada_origen

    return pendiente, ordenada_origen, y_pred

# --- Ejemplo de Uso ---
if __name__ == "__main__":
    # Datos de ejemplo (simulando decaimiento de sonido)
    # Tiempo en segundos
    tiempo = np.array([0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0])
    # Nivel de sonido en dB (disminuyendo)
    nivel_sonido = np.array([60, 58, 56, 55, 53, 51, 49, 48, 46, 44, 42])

    try:
        m, b, y_ajustado = regresion_lineal_iso3382(tiempo, nivel_sonido)

        print(f"Pendiente (m): {m:.4f}")
        print(f"Ordenada al origen (b): {b:.4f}")
        print("\nValores de Y ajustados (predichos):")
        for i in range(len(tiempo)):
            print(f"Tiempo: {tiempo[i]:.2f}s, Nivel real: {nivel_sonido[i]:.2f}dB, Nivel ajustado: {y_ajustado[i]:.2f}dB")

        # Opcional: Visualizar los resultados
        import matplotlib.pyplot as plt

        plt.figure(figsize=(10, 6))
        plt.scatter(tiempo, nivel_sonido, label='Datos reales', color='blue')
        plt.plot(tiempo, y_ajustado, color='red', linestyle='--', label=f'Línea de regresión: y = {m:.2f}x + {b:.2f}')
        plt.title('Regresión Lineal por Mínimos Cuadrados (ISO 3382:2008 Anexo C)')
        plt.xlabel('Tiempo (s)')
        plt.ylabel('Nivel de Sonido (dB)')
        plt.legend()
        plt.grid(True)
        plt.show()

    except ValueError as e:
        print(f"Error: {e}")

    # Ejemplo con datos que causan error (x constante)
    # try:
    #     tiempo_error = np.array([1, 1, 1, 1, 1])
    #     nivel_error = np.array([10, 20, 30, 40, 50])
    #     m_err, b_err, y_err_pred = regresion_lineal_iso3382(tiempo_error, nivel_error)
    # except ValueError as e:
    #     print(f"\nError esperado: {e}")
