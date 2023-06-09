# For Commenting press CTRL + k + c
# For Uncomment press CTRL + k + u

import numpy as np

class Constant :
    OBJETOS = np.array((
        [1, 150,    20],
        [2, 325,    40],
        [3, 600,    50],
        [4, 805,    36],
        [5, 430,    25],
        [6, 1200,   64],
        [7, 770,    54],
        [8, 60,     18],
        [9, 930,    46],
        [10,353,    28]))
    CANTIDAD_OBJETOS    = 10
    CANTIDAD_CASOS      = 2**CANTIDAD_OBJETOS
    VOLUMEN_MAXIMO      = 4200 

def busquedaExaustiva(OBJETOS,CANTIDAD_OBJETOS,CANTIDAD_CASOS):
    CasosValidos = []
    MejorCaso = []
    for i in range(0,CANTIDAD_CASOS):
        CasoBinario = np.binary_repr(i,CANTIDAD_OBJETOS)
        evaluar(OBJETOS,Constant.VOLUMEN_MAXIMO,CasoBinario,CasosValidos)
    print('Se encontraron '+str(len(CasosValidos))+' casos válidos')
    MayorValor = 0
    for i in range(0,len(CasosValidos)):
        if CasosValidos[i][3] == MayorValor:
            MejorCaso.append(CasosValidos[i])
        if CasosValidos[i][3] > MayorValor:
            MayorValor = CasosValidos[i][3]
            MejorCaso.clear()
            MejorCaso.append(CasosValidos[i])   
    return MejorCaso

def evaluar(OBJETOS,VOLUMEN_MAXIMO,CasoBinario,CasosValidos = []):
    SumaVolumen = 0
    SumaValor = 0
    pos = 0
    # CasosNoValidos = []
    for i in CasoBinario:
        if i == '1':
            SumaVolumen += OBJETOS[pos][1]
            SumaValor += OBJETOS[pos][2]
            if SumaVolumen > VOLUMEN_MAXIMO:
                break
        pos+=1
    if SumaVolumen < VOLUMEN_MAXIMO:
        CasosValidos.append([int(CasoBinario,2),CasoBinario,SumaVolumen,SumaValor])
        print(str([int(CasoBinario,2),CasoBinario,SumaVolumen,SumaValor]))
    # else:
    #     CasosNoValidos.append([int(CasoBinario,2),CasoBinario,SumaVolumen,SumaValor])
    #     print(str([int(CasoBinario,2),CasoBinario,SumaVolumen,SumaValor]))
    
    return CasosValidos

def main():
    MejorCaso = busquedaExaustiva(Constant.OBJETOS,Constant.CANTIDAD_OBJETOS,Constant.CANTIDAD_CASOS)
    
    for item in MejorCaso:
        print("El Mejor Caso es: "+str(item))


if __name__ == '__main__':
    main()