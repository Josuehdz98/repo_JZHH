import sys
#Se importan las actividades que se estubieron haciendo para poder ejecutarlas
from src.actividad_1 import continuous_sine, discrete_sine
from src.actividad_2 import understanding_freq
from src.tarea_1 import graficar_senales

def main(options):
    if options[1] == "act_1":
        continuous_sine()
        discrete_sine()
    elif options[1] == "act_2":
        if len(options) > 2:
            understanding_freq(options[2])
        else:
            print("Por favor ingresa una frecuencia. Ejemplo: python main.py act_2 2")
    elif options[1] == "tarea_1": #Para poder correr la tarea_1 desde la terminal, en mi caso PowerShell
        graficar_senales()
    else:
        print("opción no válida")

#Si se corre el archivo directamente, esto se asegura que el codigo se pueda ejecutar
if __name__ == '__main__':
    args = sys.argv
    if len(args) > 1:
        main(args)
    else:
        print("Por favor ingresa un argumento")
        print("Ejemplo (actividad 1): python main.py act_1")
        print("Ejemplo (actividad 2): python main.py act_2 1")
        print("Ejemplo (tarea 1): python main.py tarea_1")