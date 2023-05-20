import numpy as np
import random as r


def mutacion(binarioList, p_mutacion):
    if r.random() < p_mutacion:
        i = r.randrange(len(binarioList))
        binarioList[i] = str(1 - int(binarioList[i]))
    return (binarioList)


def mutar_poblacion(poblacion, p_mutacion):
    poblacion_final = []
    for i in range(len(poblacion)):
        # pasa el cormosoma a binario
        cromosoma_binario = list(np.binary_repr(poblacion[i], 30))
        mutacion(cromosoma_binario, p_mutacion)
        # pasa el cromosoma a decimal
        cromosoma_decimal = int(''.join(cromosoma_binario), 2)
        # agrega el cromosoma a la nueva poblacion
        poblacion_final.append(cromosoma_decimal)

    return poblacion_final
