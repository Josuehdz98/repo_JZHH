#librerias a utilizar
import numpy as np
import matplotlib.pyplot as plt
#se importa la variable de continuous_plotter, detro del archivo de graper
from src.utils.grapher import continuous_plotter

#señal seno
def send_sinusoidal(t, f=2):
    return np.sin(2 * np.pi * f * t) #para poder gerar ese seno de frecuencia 2

#señal exponencial
def send_exponencial(t):
    return np.exp(-2 * t) * (t >= 0) #lo que es el termio de t >= 0 actua como escaln unitario

#señal triangular
def send_triangular(t, f=2):
    #se combina lo que es el valor absoluto y el modulo para costruir la froma triangular de la señal
    return f * (1 - 2 * f * np.abs(np.mod(t - 1 / (4 * f), 1 / f) - 1 / (2 * f))) - 1

#señal cudratica
def send_cuadrada(t, f=2):
    #se alterna entre los valores de 1 y -1 para la señal, dependiendo del valor del modulo dentro del periodo
    return np.where(np.mod(t, 1 / f) < 1 / (2 * f), 1, -1)

def graficar_senales():
    #valor de tiempo generado desde -1 a 5 segundoscon un numero de 1000 muestras
    t = np.linspace(-1, 5, 1000)
    ts = 0.035 #periodo de muestreo
    n = np.arange(-1 / ts, 5 / ts) #se generan esos numeros necesarios para poder construir los puntos en el tiempo discreto
    #aqui el tiempo discreto se calcula a partir del periodo de muestreo
    t_discreto = n * ts

    #lista de señales a graficar, cada elemento tine, nombre, funcion que genra la señal y su respectiva ecuancion
    señales = [
        ("Sinusoidal", send_sinusoidal, r"$\sin(2\pi ft)$"),
        ("Exponencial", send_exponencial, r"$e^{-2t} \cdot u(t)$"),
        ("Triangular", send_triangular, "tri(t, f=2)"),
        ("Cuadrada", send_cuadrada, "sq(t, f=2)")
    ]

    for nombre, funcion, ecuacion in señales: #se ajustan los parametros de las señales en las graficas
        plt.figure(figsize=(10, 5)) #tamaño de la figura

        #genera la linea de la señal continua en mi cazo azul
        plt.plot(t, funcion(t), 'b-', linewidth=2, label='Señal continua')
        #genera esos puntos para la señal discreta, recorriendo la señal cotinua
        plt.plot(t_discreto, funcion(t_discreto), 'r.', markersize=6,
                 label='Muestras discretas')

        #configuracion de las graficas para entenderlas mejor
        plt.title(f"Señal {nombre} (Continua y Discreta)") #titulo de la Figura
        plt.xlabel("Tiempo [s]") #comentario en X
        plt.ylabel("Amplitud") #comentario en Y
        plt.grid(True, linestyle='--', alpha=0.6) #se acitva la cuadricula punteada
        plt.legend(loc='upper right') #muestra la "leyenda" en la esquina de arriba a la derecha
        plt.ylim(-1.2, 1.2) #ajusta el limite de Y

        plt.tight_layout() #esta funcion ajusta los margenes de la grafica
        plt.show()

if __name__ == "__main__":
    import sys
    graficar_senales()