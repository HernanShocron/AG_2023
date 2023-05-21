import random
import Fitness

"""a = 6
b = "1010"
c = ["100110","0111001","110110"]"""

def intABin(num):
    binario = ""
    if num == 0:
        binario= "0"
    else:
        while num != 1:
            binario= str(num%2) + binario
            num=num//2
        binario= "1" + binario
    return binario

def binAInt(num):
    entero=0
    posicion = len(num)-1
    for x in num:
        entero+= int(x) * 2 ** posicion
        posicion-= 1
    return entero

def torneo(array_pobl, array_fitn):   #pide como parametro la poblacion inicial y su correspondiente valor en fitness
    nuevoarray = []
    for i in range(len(array_pobl)):
        nro1 = random.randint(0,len(array_pobl)-1)
        nro2 = random.randint(0,len(array_pobl)-1)
        if array_fitn[nro1] > array_fitn[nro2]:
            nuevoarray.append(array_pobl[nro1])
            buffer = array_fitn[i]      # se mueve el valor del fitness en el array para mantener la correspondencia con el array de retorno
            array_fitn[i] = array_fitn[nro1]
            array_fitn[nro1] = buffer
        else:
            nuevoarray.append(array_pobl[nro2])
            buffer = array_fitn[i]
            array_fitn[i] = array_fitn[nro2]
            array_fitn[nro2] = buffer
        print(str(array_pobl[nro1]) + " - " + str(array_pobl[nro2]) + " => " + str(nuevoarray[i]))
    print()
    return nuevoarray

"""print(intABin(a))
print(binAInt(b))
print(torneo(c))"""