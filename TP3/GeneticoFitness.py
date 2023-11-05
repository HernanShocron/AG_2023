import numpy as np
import ProblemaViajante as viajante

def Fitness(resultados): # resultados de funcion objetivo -> 
    fitness1 = []
    fitness2 = []
    total = np.sum(resultados)      
    for i in range(len(resultados)):
        fitness1.append((total/resultados[i])) #calculamos el reciproco del fitness, de modo que las distancias menores tienen mejores valores
    total2 = np.sum(fitness1)
    for i in range(len(resultados)):
        fitness2.append((fitness1[i]/total2)) # calculamos el fitness usando los valores del fitness anterior para tener valores < 1
    #print(fitness1)
    #print(fitness2)
    #print(np.sum(fitness2))
    return fitness2

'''
resultado = []
pobl_in = viajante.Crear_Cromosomas_Iniciales(5)
for i in range(0, len(pobl_in)):
    resultado.append(viajante.Funcion_Objetivo(pobl_in[i]))
fit = Fitness([13000, 20000, 18635, 40562, 35433])
maxi = max(fit)
print(resultado)
print(fit)
'''