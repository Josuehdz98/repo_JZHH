import numpy as np  # El mejor amigo de los cálculos científicos
from src.utils.grapher import continuous_plotter  # Nuestro artista visual de señales

def frecuencia_flotante(des_freq):

    initial_time = 0
    end_time = 5
    frequency = float(des_freq)
    amplitude = 1
    number_of_points = 1000
    time = np.linspace(initial_time, end_time, number_of_points)
    xt = amplitude * np.sin(2 * np.pi * frequency * time)

    continuous_plotter(
        time, xt,
        'Señal Sinusoidal Continua',
        'Señal de la onda',
        'Tiempo',
        'Amplitud'
    )

#este bloque se ejecuta si el archivo se corre desde la terminal
if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        try:
            frecuencia = float(sys.argv[1])
            frecuencia_flotante(frecuencia)
        except ValueError:
            print("Se necesita ese numero para la frecuencia. Ejemplo: 2")
    else:
        print("python tarea_2.py frecuencia")
        print("ejemplo: python tarea_2.py 2 para una onda de 2Hz")
