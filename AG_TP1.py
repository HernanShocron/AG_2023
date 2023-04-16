import numpy as np
import matplotlib as plt
import os
import math
import random as r

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

def evaluar(x):
    return (x/Constant.COEF)**2

def correr(conjunto_solucion,cant_corridas):
    subconjunto_poblacion = poblacion_inicial()
    maximos = []
    minimos = []
    promedios = []
    for i in range(cant_corridas):
        resultado = []
        for j in range(len(subconjunto_poblacion)):
            resultado[j] = evaluar(subconjunto_poblacion[j])
        maximos.append(np.max(resultado))
        minimos.append(np.min(resultado))
        promedios.append(np.average(resultado))

def decimal_a_binario(decimal):
    if decimal <= 0:
        return "0"
    # Aquí almacenamos el resultado
    binario = ""
    # Mientras se pueda dividir...
    while decimal > 0:
        # Saber si es 1 o 0
        residuo = int(decimal % 2)
        # E ir dividiendo el decimal
        decimal = int(decimal / 2)
        # Ir agregando el número (1 o 0) a la izquierda del resultado
        binario = str(residuo) + binario
    print(f"El número {decimal} es {binario} en binario")
    return binario

def binario_a_decimal(binario):
    posicion = 0
    decimal = 0
    # Invertir la cadena porque debemos recorrerla de derecha a izquierda
    binario = binario[::-1]
    for digito in binario:
        # Elevar 2 a la posición actual
        multiplicador = 2**posicion
        decimal += int(digito) * multiplicador
        posicion += 1
    return decimal

def main():
    #binario_COEF = decimal_a_binario(Constant.COEF)
    #cant_Genes = len(binario_COEF)
    print("Hola mundo")
    print(poblacion_inicial())

if __name__ == "__main__":
    main()