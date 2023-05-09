import numpy as np
import random as r
def mutacion(binarioList,p_mutacion):
    for i in range(len(binarioList)):
        if r.random()< p_mutacion: 
            binarioList[i] = str(1 - int(binarioList[i]))
    return(binarioList)
    
def mutar_poblacion(poblacion,p_mutacion):
    poblacion_final=[]
    for i in range(len(poblacion)):
        cromosoma_binario=list(np.binary_repr(poblacion[i],30)) #pasa el cormosoma a binario
        mutacion(cromosoma_binario,p_mutacion)
        cromosoma_decimal=int(''.join(cromosoma_binario),2)#pasa el cromosoma a decimal
        poblacion_final.append(cromosoma_decimal)#agrega el cromosoma a la nueva poblacion
    print((poblacion_final))