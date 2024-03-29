import numpy as np
import matplotlib as plt
import os
import math
import random as r
import Geneticomutacion as mutacion
import Geneticotorneo as torneo
import GeneticoFitness as Fitness
import GeneticoRuleta as Ruleta
import GeneticoCrossOver as CrossOver
import GeneticoElitismo as Elitismo
import GeneticoGraficar as Graficar

class Constant:
    P_CROSSOVER = 0.75
    P_MUTACION = 0.05
    POBLACION_INICIAL = 10
    CICLOS_PROGRAMA = 100
    COEF = (2**30) - 1
    ELIT = 2

def poblacion_inicial():
    array_poblacion_inicial = []
    for i in range(Constant.POBLACION_INICIAL):
        randInt = r.randint(0, Constant.COEF)
        array_poblacion_inicial.append(randInt)
    return array_poblacion_inicial


# se cambio el nombre para no confundir con la funcion fitnes que va a ser usada en la ruleta
def funcion_objetivo(x):
    return (x/Constant.COEF)**2


if __name__ == "__main__":
    poblacion = poblacion_inicial()  # llamada a la funcion que crea poblacion inicial
    maximos = []
    crom_max = []
    minimos = []
    promedios = []
    elit =[]
    binario_COEF = np.binary_repr(Constant.COEF, 0)
    cant_Genes = len(binario_COEF)  # largo de los genes
    #print(cant_Genes)
    for i in range(Constant.CICLOS_PROGRAMA):
        resultados = []  # lista de las funciones objetivos de la poblacion actual
        for j in range(len(poblacion)):
            resultados.append(funcion_objetivo(poblacion[j]))

        #calcula max, min y promedio
        crom_max.append(poblacion[resultados.index(np.max(resultados))])
        maximos.append(np.max(resultados))
        minimos.append(np.min(resultados))
        promedios.append(np.average(resultados))
        #print(poblacion)
        
        # poblacion, fitnae_pob, cant_elit ->elit
        elit= Elitismo.elitismo(poblacion, Fitness.Fitness( resultados), Constant.ELIT) 
        #print(poblacion)
        # poblacion,fitnes_de_pob,cant_selecciones -> poblacionseleccionada
        
        # poblacion = Ruleta.seleccion(poblacion, Fitness.Fitness(resultados), Constant.POBLACION_INICIAL - Constant.ELIT)
        poblacion = torneo.torneo(poblacion, Fitness.Fitness(resultados), Constant.POBLACION_INICIAL - Constant.ELIT)

        # pob_selec,const_cross,largo_gen -> poblacion_hijos
        poblacion = CrossOver.CrossOver( poblacion, Constant.P_CROSSOVER, cant_Genes)      

        # poblacion,const_mut,largo_gen -> poblacion final
        poblacion = mutacion.mutar_poblacion(
            poblacion, Constant.P_MUTACION, cant_Genes)
        
        #Agrega a la poblacion seleccionada los cromosomas elites
        poblacion=poblacion+elit

    Graficar.Tabla(crom_max,maximos,minimos,promedios)
    Graficar.MAX_MIN_PROM(maximos,minimos,promedios)   
