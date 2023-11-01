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
import random as r

Ciudades_Disponibles = []
Distancia_Recorrida = 0
Descripcion_Recorrido = ''
Id_Ciudad_Actual = 0
Id_Ciudad_Cercana = 0

cwd             = os.getcwd()
FileName        = 'Distancias_Ruta.xlsx'
ExcelDocument   = Excel.load_workbook(cwd+'\ '.strip() +FileName)  # Strip es para quitar los espacios en blanco, python no me deja poner la barra invertida al final de la cadena
Sheet           = ExcelDocument.get_sheet_by_name('PorRuta')


class Constant : 
    CIUDADES = np.array((
        ['A','Córdoba'                               ],
        ['B','Corrientes'                            ],
        ['C','Formosa'                               ],
        ['D','La Plata'                              ],
        ['E','La Rioja'                              ],
        ['F','Mendoza'                               ],
        ['G','Neuquén'                               ],
        ['H','Paraná'                                ],
        ['I','Posadas'                               ],
        ['J','Rawson'                                ],
        ['K','Resistencia'                           ],
        ['L','Río Gallegos'                          ],
        ['M','San Fernando del Valle de Catamarca'   ],
        ['N','San Miguel de Tucumán'                 ],
        ['O','Salta'                                 ],
        ['P','San Juan'                              ],
        ['Q','San Luis'                              ],
        ['R','San Salvador de Jujuy'                 ],
        ['S','Santa Fe'                              ],
        ['T','Santa Rosa'                            ],
        ['U','Santiago del Estero'                   ],
        ['V','Ushuaia'                               ],
        ['W','Viedma'                                ]))
    

def main():
    global cwd
    global FileName
    global ExcelDoc1ument1
    global Sheet

    ExcelDocument   = Excel.load_workbook(cwd+'\ '.strip() +FileName)  # Strip es para quitar los espacios en blanco, python no me deja poner la barra invertida al final de la cadena
    Sheet           = ExcelDocument.get_sheet_by_name('PorRuta')
    
    OPC = 0
    while OPC == 0:
        system("cls")
        print('Problema del viajante')
        print(' 1- Método Heurístico')
        print(' 2- Algorítmo Genético')
        print('')
        OPC = int(input('OPCIÓN: '))
        if OPC > 2 or OPC < 0:
            print('Opción Incorrecta, vuelva a intentar...')
            OPC = 0
    match OPC:
        case 1:
            OPC2 = 0
            while OPC2 == 0:
                system("cls")
                print('Método Heurístico')
                print(' 1 - Con ciudad inicial')
                print(' 2 - Sin ciudad inicial')
                print('')
                OPC2 = int(input('OPCIÓN: '))
                if OPC2 > 2 or OPC2 < 0:
                    print('Opción Incorrecta, vuelva a intentar...')
                    OPC2 = 0
            match OPC2:
                case 1:
                    OPC3 = 0
                    while OPC3 == 0:
                        system("cls")
                        print('Seleccione Ciudad Inicial:')
                        print('')
                        ContCiudad = 0
                        for Ciudad in Constant.CIUDADES:
                            ContCiudad+=1
                            print(str(ContCiudad)+' - '+Ciudad[1])
                        print('')
                        OPC3 = int(input('Seleccione Opción: '))
                        if OPC3 > 23 or OPC3 < 0:
                            print('Opción Incorrecta, vuelva a intentar...')
                            OPC3 = 0
                        else:
                            Heuristico_Con_Ciudad(OPC3)
                            ExcelDocument.save(Constant.CIUDADES[Id_Ciudad_Actual-1][1]+'_'+FileName)
                            ExcelDocument.close()                          
                case 2:
                    Heuristico_Sin_Ciudad()
                    ExcelDocument.save(Constant.CIUDADES[Id_Ciudad_Actual-1][1]+'_'+FileName)
                    ExcelDocument.close()
        case 2:
            Algoritmo_Genetico()
    Volver_Menu()

def Volver_Menu():
    OPC = 0
    while OPC == 0:
        print('¿ Desea volver al menú ?')
        print('    1-SI   2-NO')
        OPC = int(input('OPCIÓN: '))
        if OPC > 2 or OPC < 0:
            print('Opción Incorrecta, vuelva a intentar...')
            OPC = 0
    match OPC:
        case 1:
            main()
        case 2:
            system("cls")
            print('Ejecución Finalizada!')

def Heuristico_Con_Ciudad(Id_Ciudad_Seleccionada):
    system("cls")
    print('Heuristico_Con_Ciudad')
    print('')
    print('Id_Ciudad_Seleccionada = '+str(Id_Ciudad_Seleccionada)+' - '+Constant.CIUDADES[Id_Ciudad_Seleccionada-1][1])
    Heuristica(Id_Ciudad_Seleccionada)

def Heuristico_Sin_Ciudad():
    system("cls")
    print('Heuristico_Sin_Ciudad')
    print('')
    Id_Ciudad_Random = r.randint(1,23)
    
    print('Id_Ciudad_Random = '+str(Id_Ciudad_Random)+' - '+Constant.CIUDADES[Id_Ciudad_Random-1][1])
    Heuristica(Id_Ciudad_Random)    

def Heuristica(Id_Ciudad_Inicial):
    global Ciudades_Disponibles
    global Id_Ciudad_Actual
    global Id_Ciudad_Cercana
    global Descripcion_Recorrido
    global Distancia_Recorrida

    Distancia_Recorrida = 0
    Descripcion_Recorrido = ''
    my_red      = Excel.styles.colors.Color(rgb='00FF0000')
    my_green    = Excel.styles.colors.Color(rgb='0000FF00')
    fillRed     = Excel.styles.fills.PatternFill(patternType='solid', fgColor=my_red)
    fillGreen   = Excel.styles.fills.PatternFill(patternType='solid', fgColor=my_green)

    for i in range(23):
        Ciudades_Disponibles.append(i+1)
    Ciudades_Disponibles.remove(Id_Ciudad_Inicial)
    Distancia_Recorrida   = 0
    Descripcion_Recorrido = ''
    Id_Ciudad_Actual = Id_Ciudad_Inicial
    Id_Ciudad_Cercana = Ciudad_Cercana_Disponible(Id_Ciudad_Actual)
    for i in range(22):
        Distancia_Recorrida     += Sheet.cell(row=Id_Ciudad_Actual,column=Id_Ciudad_Cercana).value
        #print('PINTAR ROJO'+str(Id_Ciudad_Actual)+ '-' + str(Id_Ciudad_Cercana))
        Sheet.cell(row=Id_Ciudad_Actual,column=Id_Ciudad_Cercana).fill = fillRed
        Descripcion_Recorrido   += '('+Constant.CIUDADES[Id_Ciudad_Actual-1][0]+') ' + Constant.CIUDADES[Id_Ciudad_Actual-1][1] + ' -> '
        Id_Ciudad_Actual = Id_Ciudad_Cercana
        Id_Ciudad_Cercana = Ciudad_Cercana_Disponible(Id_Ciudad_Actual)
    Id_Ciudad_Cercana = Id_Ciudad_Inicial
    Ciudades_Disponibles.append(Id_Ciudad_Inicial)
    #print('Viajes de regreso------------------> '+str(Id_Ciudad_Cercana))
    #print(Ciudades_Disponibles)
    Distancia_Recorrida     += Sheet.cell(row=Id_Ciudad_Actual,column=Id_Ciudad_Cercana).value
    Sheet.cell(row=Id_Ciudad_Actual,column=Id_Ciudad_Cercana).fill = fillRed
    Descripcion_Recorrido   += '('+Constant.CIUDADES[Id_Ciudad_Actual-1][0]+') ' + Constant.CIUDADES[Id_Ciudad_Actual-1][1] + ' -> '
    Id_Ciudad_Actual = Id_Ciudad_Inicial
    Descripcion_Recorrido   += '('+Constant.CIUDADES[Id_Ciudad_Actual-1][0]+') ' + Constant.CIUDADES[Id_Ciudad_Actual-1][1]
    #print('PINTAR VERDE '+str(Id_Ciudad_Inicial)+ '-' + str(Id_Ciudad_Inicial))
    Sheet.cell(row=Id_Ciudad_Inicial,column=Id_Ciudad_Inicial).fill = fillGreen
    print('RECORRIDO: '+Descripcion_Recorrido)
    print('')
    print('TOTAL KMS Recorridos: '+str(Distancia_Recorrida)+' Kms')
    print('')

def Algoritmo_Genetico():
    system("cls")
    print('Algoritmo_Genetico')
    print('')
    # Acá a diferencia de los TPs anteriores, en donde usabamos 1 o 0, vamos a tener que orientar el algoritmo a cromosomas del tipo ABCDEFGHIJKLMNOPQRSTUVW 
    # (23 LETRAS, Una para cada ciduad) ya que es importante saber el orden de como visita las ciudades

def Ciudad_Cercana_Disponible(Ciudad_Inicial):
    global Ciudades_Disponibles
    Distancia_Menor = 10000000
    Ciudad_Mas_Cercana = 0
    #print('La ciduad Inicial es '+str(Ciudad_Inicial))
    for Ciudad in Ciudades_Disponibles:
        #print('La ciudad '+str(Ciudad)+' se encuentra disponible')
        Distancia = Sheet.cell(row = Ciudad_Inicial, column = Ciudad).value
        if Distancia < Distancia_Menor:
            Distancia_Menor = Distancia
            Ciudad_Mas_Cercana = Ciudad
   # print('remove '+str(Ciudad_Mas_Cercana))
    if Ciudad_Mas_Cercana != 0 :
        Ciudades_Disponibles.remove(Ciudad_Mas_Cercana)
    #print('Para '+str(Ciudad_Inicial)+' la ciudad más cercana es '+str(Ciudad_Mas_Cercana)+' con una distancia de '+str(Distancia_Menor)+' Kms')
    return Ciudad_Mas_Cercana

if __name__ == "__main__":
    main()
    