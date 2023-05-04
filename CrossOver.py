import numpy as py
import random as r
import util as u

def main():
    listaBinarios =["123456","654321"]
    resul = NormalizarLongitud(listaBinarios)
    #print(resul)
    a = resul[0]
    b = resul[1]
    posicion = r.randint(0,5)
    posicion = 3
    hijo = CrossOver(a,b,posicion)
    print(hijo)

def CrossOver(a,b,posicion):
    hijo = a[0:posicion] # no inclye la ulima posicon ej 1234[0:3]=123
    hijo = hijo + b[posicion:len(b)]
    return hijo
    #genes = 30
    #r.randint(0,genes)
    #lista = "hola"
    #listaCompleta = lista.zfill(15)
    #print(listaCompleta)
    #u.funcion(5)    

def NormalizarLongitud(poblacion):
    resultado = []
    for individuo in poblacion:
        resultado.append(individuo.zfill(6))
    return resultado

if __name__ == "__main__":
    main()

''' print(bin(5))
decimal = 15
binario = py.binary_repr(decimal,2)
print(binario)
binarioToDecimal = int(binario,2)
print(binarioToDecimal)
binarioList = list(binario)
print(binarioList)
binarioList[0] = '0'
print(binarioList)
binarioString = ''.join(binarioList)
print(binarioString)
decimalReconvertido =  int(binarioString,2)
print(decimalReconvertido)

#list.insert(index,value)
#len(list)

long = len(binarioList)
while long < 8:
    binarioList.insert(0,'0')
    long = long + 1 

print(binarioList)
binarioString = ''.join(binarioList)
print(binarioString)
decimalReconvertido =  int(binarioString,2)
print(decimalReconvertido)'''



