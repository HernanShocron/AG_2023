import numpy as np
#import matplotlib as plt
import os
import math
import random as r

class Constant:
    P_CROSSOVER         = 0.75
    P_MUTACION          = 0.05
    POBLACION_INICIAL   = 10
    CICLOS_PROGRAMA     = 20
    COEF                = (2**30) -1
    
def mutacion(binarioList):
    for i in range(len(binarioList)):
        if r.random()< 0.05: 
            binarioList[i] = str(1 - int(binarioList[i]))
    return(binarioList)
    
def mutar_poblacion(poblacion):
    poblacion_final=[]
    for i in range(len(poblacion)):
        cromosoma_binario=list(np.binary_repr(poblacion[i],30)) #pasa el cormosoma a binario
        mutacion(cromosoma_binario)
        cromosoma_decimal=int(''.join(cromosoma_binario),2)#pasa el cromosoma a decimal
        poblacion_final.append(cromosoma_decimal)#agrega el cromosoma a la nueva poblacion
    print((poblacion_final))

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
    mutar_poblacion(a)

if __name__ == "__main__":
    main()