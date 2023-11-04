import numpy as py
import random as rd


def CrossOver(poblacion, probabilidad, cant_gen):

    lista = []
    poblacionAux= []
    # convertir la poblacion de lista de string a lista de listas
    for i in range(len(poblacion)):
        poblacionAux.append(list(poblacion[i]))
    poblacion = poblacionAux
    for i in range(0, len(poblacion), 2):
        if rd.random() <= probabilidad:
            #crea los hijos con el mismo tamaño de genes
            hijo1 = ['z'] * cant_gen
            hijo2 = ['z'] * cant_gen

            current = 0
            hijo1[0] = poblacion[i][0]
            hijo2[0] = poblacion[i + 1][0]
            repite = False
            #se repite asta que encuentre un valor que ya esta en el hijo
            while repite == False:
                #si el valor no esta en el hijo
                if poblacion[i + 1][current] not in hijo1: 
                    # guarda el valor dep padre2 en la posicion que esta en el padre1   
                    hijo1[poblacion[i].index(poblacion[i + 1][current])] = poblacion[i + 1][current]
                    current = poblacion[i].index(poblacion[i + 1][current])
                else: #si el valor esta en el hijo
                    repite = True
            for j in range(len(hijo1)):
                if hijo1[j] == 'z':
                    hijo1[j] = poblacion[i + 1][j]
            
            #ahora generamaos el hijo2
            repite = False
            current = 0
            while repite == False:
                if poblacion[i][current] not in hijo2:
                    hijo2[poblacion[i + 1].index(poblacion[i][current])] = poblacion[i][current]
                    current = poblacion[i + 1].index(poblacion[i][current])
                else:
                    repite = True

            for j in range(len(hijo2)):
                if hijo2[j] == 'z':
                    hijo2[j] = poblacion[i][j]
            
            lista.append(hijo1)
            lista.append(hijo2)
    lista = ["".join(i) for i in lista]
   
    return lista

