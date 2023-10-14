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
import os 
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
    cwd             = os.getcwd()
    ExcelDocument   = Excel.load_workbook(cwd+'\TP3\Distancias.xlsx')
    Sheet           = ExcelDocument.get_sheet_by_name('PorRuta')

# Variable Globales
Ciudades_Cercanas = []  # [Id_Ciudad_Inicial  1 | Id_Ciudad_Cercana 1 | Distancia 1], [Id_Ciudad_Inicial  1 | Id_Ciudad_Cercana 2 | Distancia 2], [Id_Ciudad_Inicial  1 | Id_Ciudad_Cercana 3 | Distancia 3]
                        # [Id_Ciudad_Inicial  2 | Id_Ciudad_Cercana 1 | Distancia 1], [Id_Ciudad_Inicial  2 | Id_Ciudad_Cercana 2 | Distancia 2], [Id_Ciudad_Inicial  2 | Id_Ciudad_Cercana 3 | Distancia 3]
                        # [Id_Ciudad_Inicial  3 | Id_Ciudad_Cercana 1 | Distancia 1], [Id_Ciudad_Inicial  3 | Id_Ciudad_Cercana 2 | Distancia 2], [Id_Ciudad_Inicial  3 | Id_Ciudad_Cercana 3 | Distancia 3]
                        # ...
                        # [Id_Ciudad_Inicial 23 | Id_Ciudad_Cercana 1 | Distancia 1], [Id_Ciudad_Inicial 23 | Id_Ciudad_Cercana 2 | Distancia 2], [Id_Ciudad_Inicial 23 | Id_Ciudad_Cercana 3 | Distancia 3]
    
Ciudades_Disponibles            = []
Ciudades_Disponibles_Restantes  = []
Distancia_Recorrida             = 0
Descripcion_Recorrido           = ''
Contador_Ciudades               = 0
Recorridos                      = []

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
    Constant.ExcelDocument.close()

# Pienso que aca hay que hacer según las diapositivas un "Branch and Bound" que limite las busqueda de combinaciones solo a las N ciudades mas cercanas a la ciudad en estudio.
# Quizas 3 sea lo mejorcito porque ya vi que con 4 se pudre bastante, creo que esto se conoce como "podar las ramas del arbol"
def Exhaustivo(N): 
    system("cls")
    print('Exhaustivo')
    print('')
    Cantidad_Combinaciones = N^23
    for i in range(1,23):
        Ciudades_Disponibles.append(Constant.CIUDADES[i-1][0])
        Ciudades_Cercanas.append(N_Ciudades_Cercanas(N,i))

    # Test para visualizar armado de Lista Ciudades_Cercanas : Está OK
    '''for i in range(len(Ciudades_Cercanas)): 
        print(Ciudades_Cercanas[i])'''

    Recorridos = []
    for i in range(1,23):
        Ciudades_Disponibles_Restantes = Ciudades_Disponibles.copy()
        Ciudades_Disponibles_Restantes.pop(i-1)
        Contador_Ciudades     = 0
        Distancia_Recorrida   = 0
        Descripcion_Recorrido = ''
        Viajar_a(N,i,i)
    for Recorrido in Recorridos:
        print(Recorrido)

def N_Ciudades_Cercanas(N,Ciudad_Inicial):
    N_Ciudades_Cercanas = [] # Id_Ciudad_Inicial | Id_Ciudad_Cercana | Distancia
    for i in range(1,23):
        if i != Ciudad_Inicial:
            if len(N_Ciudades_Cercanas) <  N :
                N_Ciudades_Cercanas.append([Ciudad_Inicial, int(Constant.CIUDADES[i-1][0]), Constant.Sheet.cell(row=Ciudad_Inicial,column=i).value])           
            if len(N_Ciudades_Cercanas) >= N :
                DistanciaMayor = 0
                for j in range(len(N_Ciudades_Cercanas)):
                    if N_Ciudades_Cercanas[j][2] > DistanciaMayor:
                        DistanciaMayor = N_Ciudades_Cercanas[j][2]
                        CiudadMasLejana = j
                if Constant.Sheet.cell(row=Ciudad_Inicial,column=i).value < DistanciaMayor:
                    N_Ciudades_Cercanas.pop(CiudadMasLejana)
                    N_Ciudades_Cercanas.append([Ciudad_Inicial, int(Constant.CIUDADES[i-1][0]), Constant.Sheet.cell(row=Ciudad_Inicial,column=i).value])
    return N_Ciudades_Cercanas
                
def Viajar_a(N,Id_Ciudad_Partida,Id_Ciudad_Actual):
    for i in range(N):
        Id_Ciudad_Destino       = int((Ciudades_Cercanas[Id_Ciudad_Actual-1][i])[1])
        Contador_Ciudades       = Contador_Ciudades + 1
        Distancia_Recorrida     = Distancia_Recorrida   + Constant.Sheet.cell(row=Id_Ciudad_Actual,column=Id_Ciudad_Destino).value
        Descripcion_Recorrido   = Descripcion_Recorrido + Constant.CIUDADES[Id_Ciudad_Actual-1][0] + '->'
        if Contador_Ciudades <  23:
            if Id_Ciudad_Destino in Ciudades_Disponibles_Restantes:
                Ciudades_Disponibles_Restantes.pop(Id_Ciudad_Destino-1)
                Viajar_a(N,Id_Ciudad_Partida,Id_Ciudad_Destino)
        if Contador_Ciudades == 23:
            Distancia_Recorrida     = Distancia_Recorrida   + Constant.Sheet.cell(row=Id_Ciudad_Actual,column=Id_Ciudad_Partida).value
            Descripcion_Recorrido   = Descripcion_Recorrido + Constant.CIUDADES[Id_Ciudad_Partida-1][0]
            Recorridos.append([Descripcion_Recorrido,Distancia_Recorrida])

    
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



    