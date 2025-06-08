import sys

# Se importan solo las tareas activas
from src.tarea_1 import graficar_senales
from src.tarea_2 import frecuencia_flotante
from src.tarea_3 import ejecutar_tarea_3
from src.tarea_4 import ejecutar_tarea_4

def main(options):
    if options[1] == "tarea_1":
        graficar_senales()

    elif options[1] == "tarea_2":
        if len(options) > 2:
            frecuencia_flotante(options[2])
        else:
            print("Por favor ingresa una frecuencia. Ejemplo: python main.py tarea_2 2")

    elif options[1] == "tarea_3":
        if len(options) == 5:  # tarea_3 + 3 parámetros
            ejecutar_tarea_3(options[2], options[3], options[4])
        else:
            print("Por favor ingresa amplitud, frecuencia y fase.")
            print("Ejemplo: python main.py tarea_3 1.5 2.0 0.785")

    elif options[1] == "tarea_4":
        if len(options) > 2:
            ejecutar_tarea_4(options[2])  # ✅ Ejecutar tarea 4 con número de bits como string
        else:
            print("Por favor ingresa el número de bits del DAC.")
            print("Ejemplo: python main.py tarea_4 8")

    else:
        print("Tarea no reconocida. Usa: tarea_1, tarea_2, tarea_3 o tarea_4.")

# Punto de entrada del script
if __name__ == '__main__':
    args = sys.argv
    if len(args) > 1:
        main(args)
    else:
        print("Por favor ingresa una tarea para ejecutar:")
        print("Ejemplo (tarea 1): python main.py tarea_1")
        print("Ejemplo (tarea 2): python main.py tarea_2 <frecuencia>")
        print("Ejemplo (tarea 3): python main.py tarea_3 <amplitud> <frecuencia> <fase>")
        print("Ejemplo (tarea 4): python main.py tarea_4 <n_bits>")
