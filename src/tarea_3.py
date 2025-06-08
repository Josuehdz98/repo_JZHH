import numpy as np
import matplotlib.pyplot as plt

def generar_senal_continua(amplitud, frecuencia, fase, tiempo_inicio=0, tiempo_fin=5, puntos=1000):
    tiempo = np.linspace(tiempo_inicio, tiempo_fin, puntos)
    señal = amplitud * np.sin(2 * np.pi * frecuencia * tiempo + fase)
    return tiempo, señal

def generar_senal_discreta(amplitud, frecuencia, fase, muestras=50):
    n = np.arange(muestras)
    señal = amplitud * np.sin(2 * np.pi * frecuencia * n / 10 + fase)
    return n, señal

#Aqui se comparan esas dos señales, la modificada y una señal de referencia
def graficar_comparativa(t, señal, params, es_discreta=False):
    gen_senal = generar_senal_discreta if es_discreta else generar_senal_continua
    t_ref, señal_ref = gen_senal(1.0, 1.0, 0.0)  #valores fijos para la señal

    plt.figure(figsize=(10, 5))
    title = 'Comparación de señal' + (' Discreta' if es_discreta else ' Continua')
    x_label = 'Muestras' if es_discreta else 'Tiempo [s]'

    if es_discreta:
        #se grafica esa señal discreta modificada
        markerline, stemlines, _ = plt.stem(t, señal, 'b-', markerfmt='bo',
            label=f'Modificada: A={params["amplitud"]}, f={params["frecuencia"]}Hz, φ={params["fase"]}rad')
        plt.setp(stemlines, 'linewidth', 2)
        plt.setp(markerline, 'markersize', 5)

        #se grafica la señal discreta de referencia
        markerline_ref, stemlines_ref, _ = plt.stem(t_ref, señal_ref, 'r--', markerfmt='ro',
            label='Referencia: A=1, f=1Hz, φ=0rad')
        plt.setp(stemlines_ref, 'linewidth', 1.5)
        plt.setp(markerline_ref, 'markersize', 5, 'alpha', 0.7)
    else:
        #se grafica la señal continua modificada
        plt.plot(t, señal, 'b-', linewidth=2,
            label=f'Modificada: A={params["amplitud"]}, f={params["frecuencia"]}Hz, φ={params["fase"]}rad')

        #se grafica esa señal continua de referencia
        plt.plot(t_ref, señal_ref, 'r--', linewidth=1.5,
            label='Referencia: A=1, f=1Hz, φ=0rad')

    #para las etiquetas, leyenda y rejilla
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel('Amplitud')
    plt.legend()
    plt.grid(True)
    plt.show()

#esta funcion aqui llama a las funciones flotanes para generar y graficar las señales continua y discreta
def ejecutar_tarea_3(amplitud_str, frecuencia_str, fase_str):
    try:
        #se convierten lo que son losd parametros a numeros para poder operar con ellos
        params = {
            "amplitud": float(amplitud_str),
            "frecuencia": float(frecuencia_str),
            "fase": float(fase_str)
        }

        #se genera la señal continua con los parametros indicados
        t, señal_cont = generar_senal_continua(**params)

        #se genera la señal discreta con los mismos parametros de la continua
        n, señal_disc = generar_senal_discreta(**params)

        #se grafican ambas señales comparandolas con la señal de referencia
        graficar_comparativa(t, señal_cont, params)
        graficar_comparativa(n, señal_disc, params, es_discreta=True)

    except ValueError:
        #si hay error en la conversion en los parametros flotantes, se muestran estos mensjaes
        print("\nERROR: Parámetros deben ser números válidos")
        print("uso: python main.py tarea_3 amplitud frecuencia fase")
        print("ejemplo: python main.py tarea_3 1.5 2.0 0.785\n")

#se ejecuta si el archivo se corre desde la terminal
if __name__ == "__main__":
    import sys
    if len(sys.argv) == 4:
        ejecutar_tarea_3(*sys.argv[1:4])
    else:
        print("usando valores por defecto (1.5, 2.0, 0.785)")
        ejecutar_tarea_3("1.5", "2.0", "0.785")
