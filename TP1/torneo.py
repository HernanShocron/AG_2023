import random
import Fitness

def torneo(array_pobl, array_fitn, cantSelecciones):   # pide como parametro la poblacion inicial y su correspondiente valor en fitness
    nuevoarray = []
    for i in range(cantSelecciones):
        nro1 = random.randint(0,len(array_pobl)-1)
        nro2 = random.randint(0,len(array_pobl)-1)
        if array_fitn[nro1] > array_fitn[nro2]:
            nuevoarray.append(array_pobl[nro1])
        else:
            nuevoarray.append(array_pobl[nro2])
    return nuevoarray