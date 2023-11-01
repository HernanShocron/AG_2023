import numpy as py

def decimal_a_binario(poblacionDecimal, cant_gen):
    poblacionBinaria = []
    for i in range(len(poblacionDecimal)):
        poblacionBinaria.append(py.binary_repr(poblacionDecimal[i],cant_gen))
    return poblacionBinaria    

def binario_a_decimal(poblacionBinaria):
    poblacionDecimal = []
    for i in range(len(poblacionBinaria)):
        poblacionDecimal.append(int(poblacionBinaria[i], 2))
    return poblacionDecimal