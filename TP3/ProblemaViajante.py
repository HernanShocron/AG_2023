'''ENUNCIADO 3ER TRABAJO PRÁCTICO
El problema del viajante (también conocido como problema del viajante de comercio o por sus siglas en inglés: TSP (Traveling Salesman Problem), 
es uno de los problemas más famosos (y quizás el mejor estudiado) en el campo de la optimización combinatoria computacional.
A pesar de la aparente sencillez de su planteamiento, el TSP es uno de los más complejos de resolver.

Definición: Sean N ciudades de un territorio. La distancia entre cada ciudad viene dada por la matriz D: NxN, donde d[x,y] representa la distancia que hay entre la ciudad X y la ciudad Y.
El objetivo es encontrar una ruta que, comenzando y terminando en una ciudad concreta, pase una sola vez por cada una de las ciudades y minimice la distancia recorrida por el viajante.

Ejercicios:
1.Hallar la ruta de distancia mínima que logre unir todas las capitales de provincias de la República Argentina, utilizando un método exhaustivo. ¿Puede resolver el problema? 
Justificar de manera teórica.
2.Realizar un programa que cuente con un menú con las siguientes opciones:
    a)Permitir ingresar una provincia y hallar la ruta de distancia mínima que logre unir todas las capitales de provincias de la República Argentina 
    partiendo de dicha capital utilizando la siguiente heurística: “Desde cada ciudad ir a la ciudad más cercana no visitada.”  Recordar regresar siempre a la ciudad de partida. 
    Presentar un mapa de la República con el recorrido indicado. Además indicar la ciudad de partida, el recorrido completo y la longitud del trayecto. 
    El programa deberá permitir seleccionar la capital que el usuario desee ingresar como inicio del recorrido.
    b)Encontrar el recorrido mínimo para visitar todas las capitales de las provincias de la República Argentina siguiendo la heurística mencionada en el punto a. 
    Deberá mostrar como salida el recorrido y la longitud del trayecto.
    c)Hallar la ruta de distancia mínima que logre unir todas las capitales de provincias de la República Argentina, utilizando un algoritmo genético.

Recomendaciones para el algoritmo:
N = 50 Número de cromosomas de las poblaciones.
M = 200 Cantidad de ciclos.
Cromosomas: permutaciones de 23 números naturales del 1 al 23 donde cada gen es una ciudad.
Las frecuencias de crossover y de mutación quedan a criterio del grupo.
Se deberá usar crossover cíclico.
Comparar los resultados obtenidos  entre la resolución a través de heurísticas y con algoritmos genéticos a través de una conclusión que deberá anexarse al informe.
Agregar en el informe un apartado final denominado «Aportes Prácticos del TSP» donde se expliquen algunas aplicaciones en las que actualmente se use el problema del viajante. 
Tomar por lo menos dos y explicarlas.'''

from os import system
import numpy as np
import openpyxl as Excel

class Constant :
    CIUDADES = np.array((
        [ 1,'Córdoba'                               ],
        [ 2,'Corrientes'                            ],
        [ 3,'Formosa'                               ],
        [ 4,'La Plata'                              ],
        [ 5,'La Rioja'                              ],
        [ 6,'Mendoza'                               ],
        [ 7,'Neuquén'                               ],
        [ 8,'Paraná'                                ],
        [ 9,'Posadas'                               ],
        [10,'Rawson'                                ],
        [11,'Resistencia'                           ],
        [12,'Río Gallegos'                          ],
        [13,'San Fernando del Valle de Catamarca'   ],
        [14,'San Miguel de Tucumán'                 ],
        [15,'Salta'                                 ],
        [16,'San Juan'                              ],
        [17,'San Luis'                              ],
        [18,'San Salvador de Jujuy'                 ],
        [19,'Santa Fe'                              ],
        [20,'Santa Rosa'                            ],
        [21,'Santiago del Estero'                   ],
        [22,'Ushuaia'                               ],
        [23,'Viedma'                                ]))
    ExcelDocument = Excel.load_workbook('Distancias.xlsx')
    Sheet = ExcelDocument.get_sheet_by_name('PorRuta')
   
def main():
    OPC = 0
    while OPC == 0:
        system("cls")
        print('Problema del viajante')
        print(' 1- Método Exhaustivo')
        print(' 2- Método Heurístico')
        print(' 3- Algorítmo Genético')
        print('')
        OPC = int(input('OPCIÓN: '))
        if OPC > 3 or OPC < 0:
            OPC = 0
    match OPC:
        case 1:
            Exhaustivo(3)
        case 2:
            OPC2 = 0
            while OPC2 == 0:
                system("cls")
                print('Método Heurístico')
                print(' 1 - Con ciudad inicial')
                print(' 2 - Sin ciudad inicial')
                print('')
                OPC2 = int(input('OPCIÓN: '))
                if OPC2 > 2 or OPC2 < 0:
                    OPC2 = 0
            match OPC2:
                case 1:
                    OPC3 = 0
                    while OPC3 == 0:
                        system("cls")
                        print('Seleccione Ciudad Inicial:')
                        print('')
                        for ciudad in Constant.CIUDADES:
                            print(str(ciudad[0])+' - '+ciudad[1])
                        print('')
                        input('OPCIÓN: ')
                        OPC3 = input('Seleccione Opción: ')
                        if OPC3 > 23 or OPC3 < 0:
                            OPC3 = 0
                    Heuristico_Con_Ciudad(OPC3)
                case 2:
                    Heuristico_Sin_Ciudad()
        case 3:
            Algoritmo_Genetico()
    Constant.ExcelDocument.close

def Exhaustivo(N): # Pienso que aca hay que hacer según las diapositivas un "Branch and Bound" Limitando las busqueda de combinaciones solo a las N ciudades mas cercanas a la ciudad en estudio 
    system("cls")
    print('Exhaustivo')
    print('')

def N_Ciudades_Cercanas(N,Ciudad,Ciudades_Cercanas):
    N_Ciudades_Cercanas = []
    for i in range(1,23):
        if i != Ciudad and N_Ciudades_Cercanas.count < N:
            Ciudades_Cercanas.append(Constant.CIUDADES[i], Constant.Sheet.cell(row=Ciudad,column=i))
        else:
            Ciudades_Cercanas(i,N_Ciudades_Cercanas)

def Ciudades_Cercanas(I,Ciudad,Ciudades_Cercanas):
    Kms = Constant.Sheet.cell(row=Ciudad,column=I)
    for Ciudad_Item in Ciudades_Cercanas:
        if Ciudad_Item[1] > Kms:
            Ciudades_Cercanas

def Heuristico_Con_Ciudad(OPC):
    system("cls")
    print('Heuristico_Con_Ciudad')
    print('')

def Heuristico_Sin_Ciudad():
    system("cls")
    print('Heuristico_Sin_Ciudad')
    print('')

def Algoritmo_Genetico():
    system("cls")
    print('Algoritmo_Genetico')
    print('')

if __name__ == "__main__":
    main()



    