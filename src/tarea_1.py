#Librerias a utilizar
import numpy as np
import matplotlib.pyplot as plt
#Se importa la variable de continuous_plotter, detro del archivo de grapher
from src.utils.grapher import continuous_plotter

#Señal Seno
def send_sinusoidal(t, f=2):
    return np.sin(2 * np.pi * f * t) #Para poder gerar ese seno de frecuencia 2

#Señal Exponencial
def send_exponencial(t):
    return np.exp(-2 * t) * (t >= 0) #Lo que es el termino de t >= 0 actua como escaln unitario

#Señal Triangular
def send_triangular(t, f=2):
    #Se combina lo que es el valor absoluto y el modulo para costruir la froma triangular de la señal
    return f * (1 - 2 * f * np.abs(np.mod(t - 1 / (4 * f), 1 / f) - 1 / (2 * f))) - 1

#Señal Cudratica
def send_cuadrada(t, f=2):
    #Se alterna entre los valores de 1 y -1 para la señal, dependiendo del valor del modulo dentro del periodo
    return np.where(np.mod(t, 1 / f) < 1 / (2 * f), 1, -1)

def graficar_senales():
    #Valor de tiempo generado desde -1 a 5 segundoscon un numero de 1000 muestras
    t = np.linspace(-1, 5, 1000)
    ts = 0.035 #Periodo de Muestreo
    n = np.arange(-1 / ts, 5 / ts) #Se generan esos numeros necesarios para poder construir los puntos en el tiempo discreto
    #Aquí el tiempo discreto se calcula a partir del periodo de muestreo
    t_discreto = n * ts

    # Lista de señales a graficar, cada elemento tiene, nombre, funcion que genera la señal y su respectiva EC
    señales = [
        ("Sinusoidal", send_sinusoidal, r"$\sin(2\pi ft)$"),
        ("Exponencial", send_exponencial, r"$e^{-2t} \cdot u(t)$"),
        ("Triangular", send_triangular, "tri(t, f=2)"),
        ("Cuadrada", send_cuadrada, "sq(t, f=2)")
    ]

    for nombre, funcion, ecuacion in señales: #Se ajustan los parametros de las señales en las graficas
        plt.figure(figsize=(10, 5)) #Tamaño de la figura

        # Genera la linea de la señal continua en mi cazo azul
        plt.plot(t, funcion(t), 'b-', linewidth=2, label='Señal continua')
        # Genera esos puntos para la señal discreta, recorriendo la señal cotinua
        plt.plot(t_discreto, funcion(t_discreto), 'r.', markersize=6,
                 label='Muestras discretas')

        # Configuracion de las graficas para entenderlas mejor
        plt.title(f"Señal {nombre} (Continua y Discreta)") #Titulo de la Figura
        plt.xlabel("Tiempo [s]") #Comentario en X
        plt.ylabel("Amplitud") #Comentario en Y
        plt.grid(True, linestyle='--', alpha=0.6) # Se acitva la cuadricula punteada
        plt.legend(loc='upper right') #Muestra la "leyenda" en la esquina de arriba a la derecha
        plt.ylim(-1.2, 1.2) #Ajusta el limite de Y

        plt.tight_layout() #Esta funcion ajusta los margenes de la grafica
        plt.show()

if __name__ == "__main__":
    graficar_senales()