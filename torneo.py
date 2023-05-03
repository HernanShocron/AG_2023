import random
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

def torneo(array):
    nuevoarray = []
    for i in range(len(array)):
        nro1 = random.randint(0,len(array)-1)
        nro2 = random.randint(0,len(array)-1)
        if array[nro1] > array[nro2]:
            nuevoarray.append(array[nro1])
        else:
            nuevoarray.append(array[nro2])
        print(str(array[nro1]) + " - " + str(array[nro2]) + " => " + str(nuevoarray[i]))
    print()
    return nuevoarray

"""print(intABin(a))
print(binAInt(b))
print(torneo(c))"""