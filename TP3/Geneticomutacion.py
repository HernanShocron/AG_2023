import numpy as np
import random as r
#import ProblemaViajante as pdv

def mutacion(cromosoma, p_mutacion):
    if r.random() < p_mutacion:
        posiciones = r.sample(range(0,23),2)
        # Syntax : random.sample(sequence, k)
        # Parameters:
        #   sequence: Can be a list, tuple, string, or set.
        #   k: An Integer value, it specify the length of a sample.
        # Returns: k length new list of elements chosen from the sequence.

        lista =  list(cromosoma)

        aux1 = lista[posiciones[0]]
        aux2 = lista[posiciones[1]]

        lista[posiciones[0]] = aux2
        lista[posiciones[1]] = aux1
        
        newString = ''.join(map(str,lista))

        return(newString)

    return cromosoma


def mutar_poblacion(poblacion, p_mutacion):
    poblacion_final = []
    for cromosoma in (poblacion):
        poblacion_final.append(mutacion(cromosoma, p_mutacion))
    return poblacion_final  

# Tests:

# poblacion = pdv.Crear_Cromosomas_Iniciales(2)
# print(poblacion)
# print(mutar_poblacion(poblacion,1))

# posiciones = r.sample(range(0,23),2)
# print(posiciones[0])
# print(posiciones[1])