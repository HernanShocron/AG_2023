import numpy as np
import matplotlib as plt
import os
import math
import random as r
import mutacion 
import torneo
import Fitness
import Ruleta
import CrossOver
import Elitismo

class Constant:
    P_CROSSOVER         = 0.75
    P_MUTACION          = 0.05
    POBLACION_INICIAL   = 10
    CICLOS_PROGRAMA     = 20
    COEF                = (2**30) -1
    APLICA_ELT          = False # determina si el codigo aplicara elitismo o no, falta aplicarlo en el main

def poblacion_inicial():
    array_poblacion_inicial = []
    for i in range(Constant.POBLACION_INICIAL):
        randInt = r.randint(0,Constant.COEF)
        array_poblacion_inicial.append(randInt)
    return array_poblacion_inicial

def funcion_objetivo(x): #se cambio el nombre para no confundir con la funcion fitnes que va a ser usada en la ruleta
    return (x/Constant.COEF)**2

if __name__ == "__main__":
    poblacion = poblacion_inicial()  #llamada a la funcion que crea poblacion inicial  
    maximos = []
    minimos = []
    promedios = []
    binario_COEF = np.binary_repr(Constant.COEF,0)
    cant_Genes = len(binario_COEF) #largo de los genes
    print(cant_Genes)
    for i in range(Constant.CICLOS_PROGRAMA):
        resultados = [] #lista de las funciones objetivos de la poblacion actual
        for j in range(len(poblacion)):
            resultados.append(funcion_objetivo(poblacion[j]))
        maximos.append(np.max(resultados))
        minimos.append(np.min(resultados))
        promedios.append(np.average(resultados))
        poblacion = Ruleta.seleccion(poblacion,Fitness.Fitness(resultados),Constant.POBLACION_INICIAL) #poblacion,fitnes_de_pob,cant_selecciones -> poblacionseleccionada
        print(CrossOver.CrossOver(poblacion, Constant.P_CROSSOVER, cant_Genes))#pob_selec,cost,largo_gen -> poblacion_hijos en binario
        break 