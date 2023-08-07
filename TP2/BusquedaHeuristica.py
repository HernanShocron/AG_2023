import numpy as np
import operator as op
import time

class Constant :
    OBJETOS = np.array((
        [1, 1800,   72],
        [2, 600,    36],
        [3, 1200,   60]))
    Maximo      = 3000

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
#     Maximo      = 4200

def ValuarObjetos(OBJETOS):
    ObjetosValuados = []
    for Objeto in OBJETOS:
        Valor = Objeto[2]/Objeto[1]
        ObjetosValuados.append([Objeto[0],Objeto[1],Objeto[2],Valor])
        ObjetosValuados.sort(key = op.itemgetter(3),reverse = True)
    return ObjetosValuados

def main():
    start = time.time()
    ObjetosValuados = ValuarObjetos(Constant.OBJETOS)
    ObjetosSeleccionados = []
    SumaMochila = 0
    SumaValor = 0
    CasoBinario = [0] * len(Constant.OBJETOS)
    for Objeto in ObjetosValuados:
        if SumaMochila + Objeto[1] <= Constant.Maximo:
            ObjetosSeleccionados.append(Objeto)
            SumaMochila += Objeto[1]
            SumaValor += Objeto[2]
            CasoBinario[Objeto[0]-1] = 1
    for Objeto in ObjetosSeleccionados:
        print(str(Objeto))
    end = time.time()
    print(f"Tiempo de ejecucion {end-start}")
    print(CasoBinario)
    print('El valor encontrado es de '+str(SumaValor))

if __name__ == '__main__':
    main()