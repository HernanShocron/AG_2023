import numpy as np
import matplotlib as plt
import os
import math
import random as r
import mutacion 
from torneo import torneo, intABin, binAInt

class Constant:
    P_CROSSOVER         = 0.75
    P_MUTACION          = 0.05
    POBLACION_INICIAL   = 10
    CICLOS_PROGRAMA     = 20
    COEF                = (2**30) -1
    


def poblacion_inicial():
    array_poblacion_inicial = []
    for i in range(Constant.POBLACION_INICIAL):
        randInt = r.randint(0,Constant.COEF)
        array_poblacion_inicial.append(randInt)
    return array_poblacion_inicial

def funcion_objetivo(x):#se cambio el nombre para no confundir con la funcion fitnes que va a ser usada en la ruleta
    return (x/Constant.COEF)**2

def correr(conjunto_solucion,cant_corridas):
    subconjunto_poblacion = poblacion_inicial()
    maximos = []
    minimos = []
    promedios = []
    for i in range(cant_corridas):
        resultado = []
        for j in range(POBLACION_INICIAL):
            resultado[j] = funcion_objetivo(subconjunto_poblacion[j])
        maximos.append(np.max(resultado))
        minimos.append(np.min(resultado))
        promedios.append(np.average(resultado))

def main():
    #binario_COEF = decimal_a_binario(Constant.COEF)
    #cant_Genes = len(binario_COEF)
    a=poblacion_inicial()
    print(a)
    mutacion.mutar_poblacion(a,0.05)
    pob = poblacion_inicial()
    print(pob)
    print()
    print(torneo(pob))


if __name__ == "__main__":
    main()