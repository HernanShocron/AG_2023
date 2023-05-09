import matplotlib.pyplot as plt
import numpy as np

# maximos,minimos,promedios : son arreglos numericos, todos de misma dimensión
def MAX_MIN_PROM(maximos,minimos,promedios):
    x = np.arange(0, len(maximos), 1, int)
    plt.figure("Máximos, mínimos y promedio")
    plt.title("Máximos, mínimos y promedio")
    plt.xlabel("N-ésima corrida")
    plt.ylabel("f(x)")
    plt.plot(x,maximos,'g-')
    plt.plot(x,minimos,'r-')
    plt.plot(x,promedios,'b-')
    plt.show()

# /// Prueba de ejecución (se puede borrar) ///
# maximos = [3,3,4,5,6]
# minimos = [0,1,1,1,2]
# promedios = [2.5,2,2.5,3,4]
# MAX_MIN_PROM(maximos,minimos,promedios)
# /// ///