import matplotlib.pyplot as plt
import numpy as np

def MAX_MIN_PROM(maximos, minimos, promedios):
    x = np.arange(0, len(maximos), 1, int)
    plt.figure("Máximos, mínimos y promedio")
    plt.title("Máximos, mínimos y promedio")
    plt.xlabel("N-ésima corrida")
    plt.ylabel("f(x)")
    plt.plot(x, maximos, 'g-')
    plt.plot(x, minimos, 'r-')
    plt.plot(x, promedios, 'b-')
    plt.show()

def Tabla(crom_max, maximos, minimos, promedios):
    print("Nro_iteracion \t Comosoma \t Máximo \t\t Mínimo \t \t Promedio")
    for i in range(len(crom_max)):
        print((i+1), ' ',crom_max[i] ,' ', maximos[i], ' ', minimos[i],' ', promedios[i])