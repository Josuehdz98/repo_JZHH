import numpy as np
import matplotlib.pyplot as plt

# Esta funcion es la que calcula los parametros basicos del DAC
def calcular_dac(n_bits, voltaje_max=5.0):
    #Aqui de calcula el número total de niveles posibles, por ejemplo, con 3 bits son 8 niveles
    niveles = 2 ** n_bits

    #calculamos el tamaño del paso, es decir, la diferencia de voltaje entre cada nivel
    paso = voltaje_max / (niveles - 1)

    #calculamos lo que es la resolucion como ese porcentaje
    resolucion = (paso / voltaje_max) * 100

    #Devolvemos los resultados como una especie de lista con nombres, es decir para poder hacer el llamado
    #de estas funciones de una forma un poco mas simplificada
    return {
        'niveles': niveles,
        'paso': paso,
        'resolucion': resolucion,
        'v_fs': voltaje_max
    }


#con esto se dibuja la salida del DAC en una grafica
def graficar_dac(n_bits, datos):
    # Creamos lo que son esos valores de entrada digital: desde 0 hasta 2^n_bits - 1
    entradas = np.arange(0, 2 ** n_bits)

    # calculamos las salidas analogicas multiplicando cada entrada por el tamaño del paso
    salidas = entradas * datos['paso']

    #Configuracion de la grafica
    plt.figure(figsize=(8, 5))  #tamaño de la ventana de la grafica
    plt.step(entradas, salidas, where='post', color='blue')  # Grafica de una forma escalonada

    #titulos y etiquetas
    plt.title(f'DAC de {n_bits} bits\nPaso: {datos["paso"]:.4f} V - Resolución: {datos["resolucion"]:.2f}%')
    plt.xlabel('Entrada Digital')
    plt.ylabel('Salida Analógica (Voltios)')

    #agregamos lineas de cuadricula para que sea mas legible
    plt.grid(True, linestyle='--', alpha=0.5)

    plt.show()

#esta funcion es la principal, es decir la que se encarga de ejecutar la tarea_4
def ejecutar_tarea_4(n_bits_str):
    try:
        #convertimos el texto que escribio el usuario a numero
        n_bits = int(n_bits_str)

        #revisamos que el numero de bits sea positivo
        if n_bits <= 0:
            print("el número de bits debe ser mayor a cero")
            return

        #llamamos a la funcion que hace esos calculos necesaros
        resultados = calcular_dac(n_bits)

        #mostramos los resultados obtendos en la consola
        print(f"\nDAC de {n_bits} bits:")
        print(f"Niveles posibles: {resultados['niveles']}")
        print(f"Tamaño del paso: {resultados['paso']:.6f} V")
        print(f"Resolución: {resultados['resolucion']:.2f} %")

        #mostramos la grafica
        graficar_dac(n_bits, resultados)

    except ValueError:
        #si el usuario escribe letras o algo incorrecto
        print("error: Debes escribir un número entero positivo")
        print("ejemplo: python main.py tarea_4 8")


#este bloque se ejecuta si el archivo se corre desde la terminal
if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        tarea_4(sys.argv[1])
    else:
        #si no escribio nada, se comentara lo siguiente
        print("uso correcto: python main.py tarea_4 n_bits")
        print("ejemplo: python main.py tarea_4 8")
