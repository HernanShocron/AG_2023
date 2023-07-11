import numpy as np

def Fitness(resultados): # resultados de funcion objetivo -> 
    fitness = []
    total = np.sum(resultados)      
    for i in range(len(resultados)):
        fitness.append(resultados[i]/total)
    return fitness