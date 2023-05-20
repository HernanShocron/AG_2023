import numpy as py
import random as r

def CrossOver(poblacion, probabilidad, cant_gen):

    listaBinario = []

    for i in range(len(poblacion)):
        listaBinario.append(py.binary_repr(poblacion[i],cant_gen)) #pasa los genes a binaro

    for i in range(0,len(poblacion),2):
        if r.random() <= probabilidad:
            posicion = r.randint(1,cant_gen-1)
            hijo1 = listaBinario[i][0:posicion] + listaBinario[i+1][posicion:cant_gen]
            hijo2 = listaBinario[i+1][0:posicion] + listaBinario[i][posicion:cant_gen]
            listaBinario[i] = hijo1
            listaBinario[i+1] = hijo2
    return listaBinario