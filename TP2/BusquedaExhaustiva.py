import numpy as np
import time

class Constant :
   OBJETOS = np.array((
        [1, 1800,   72],
        [2, 600,    36],
        [3, 1200,   60]))
   CANTIDAD_CASOS      = 2 ** len(OBJETOS) 
   MAXIMO      = 3000

# class Constant :
#     OBJETOS = np.array((
#         [1, 150,    20],
#         [2, 325,    40],
#         [3, 600,    50],
#         [4, 805,    36],
#         [5, 430,    25],
#         [6, 1200,   64],
#         [7, 770,    54],
#         [8, 60,     18],
#         [9, 930,    46],
#         [10,353,    28]))
#     CANTIDAD_CASOS      = 2**len(OBJETOS) 
#     MAXIMO      = 4200 

def busquedaExhaustiva(OBJETOS,CANTIDAD_OBJETOS,CANTIDAD_CASOS):
    CasosValidos = []
    MejorCaso = []
    for i in range(0,CANTIDAD_CASOS):
        CasoBinario = np.binary_repr(i,CANTIDAD_OBJETOS)
        evaluar(OBJETOS,Constant.MAXIMO,CasoBinario,CasosValidos)
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

def evaluar(OBJETOS,MAXIMO,CasoBinario,CasosValidos = []):
    SumaVolumen = 0
    SumaValor = 0
    pos = 0
    # CasosNoValidos = []
    for i in CasoBinario:
        if i == '1':
            SumaVolumen += OBJETOS[pos][1]
            SumaValor += OBJETOS[pos][2]
            if SumaVolumen > MAXIMO:
                break
        pos+=1
    if SumaVolumen < MAXIMO:
        CasosValidos.append([int(CasoBinario,2),CasoBinario,SumaVolumen,SumaValor])
        print(str([int(CasoBinario,2),CasoBinario,SumaVolumen,SumaValor]))
    # else:
    #     CasosNoValidos.append([int(CasoBinario,2),CasoBinario,SumaVolumen,SumaValor])
    #     print(str([int(CasoBinario,2),CasoBinario,SumaVolumen,SumaValor]))
    
    return CasosValidos

def main():
    start = time.time()
    MejorCaso = busquedaExhaustiva(Constant.OBJETOS,len(Constant.OBJETOS),Constant.CANTIDAD_CASOS)
    end = time.time()
    print(f"Tiempo de ejecucion {end-start}") 
    for item in MejorCaso:
        print("El Mejor Caso es: "+str(item))

if __name__ == '__main__':
    main()