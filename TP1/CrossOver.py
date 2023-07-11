import numpy as py
import random as r

def CrossOver(poblacion, probabilidad, cant_gen):

    listaBinario = []
    lista =[]

    for i in range(len(poblacion)):
        listaBinario.append(py.binary_repr(poblacion[i],cant_gen)) #pasa los genes a binaro

    for i in range(0,len(poblacion),2):
        if r.random() <= probabilidad:
            posicion = r.randint(1,cant_gen-1) #punto de corte
            hijo1 = listaBinario[i][0:posicion] + listaBinario[i+1][posicion:cant_gen]
            hijo2 = listaBinario[i+1][0:posicion] + listaBinario[i][posicion:cant_gen]
            listaBinario[i] = hijo1
            listaBinario[i+1] = hijo2
           
    for i in range(len(poblacion)): #pasa los gennes a decimal
        lista.append(int(listaBinario[i],2))
    return lista