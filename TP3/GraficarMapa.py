#Funcion para graficar el recorrido
from matplotlib import pyplot as plt
from matplotlib import image as img
import os 

''' [541,599],     # Buenos Aires'''
def Graficar_Reccorrido(recorrido):
    coordenadas=[[333,440],     # Córdoba
                 [543,273],     # Corrientes
                 [560,207],     # Formosa
                 [547,614],     # La Plata
                 [241,381],     # La Rioja
                 [169,527],     # Mendoza
                 [201,800],     # Neuquén
                 [479,470],     # Paraná
                 [655,279],     # Posadas
                 [316,1002],    # Rawson
                 [530,262],     # Resistencia
                 [229,1393],    # Río Gallegos
                 [265,322],     # San Fernando del Valle de Catamarca
                 [288,252],     # San Miguel de Tucumán
                 [290,129],     # Salta
                 [282,146],     # San Juan
                 [174,468],     # San Luis
                 [256,536],     # San Salvador de Jujuy
                 [464,455],     # Santa Fe
                 [335,699],     # Santa Rosa
                 [339,264],     # Santiago del Estero
                 [277,1526],    # Ushuaia
                 [377,888]]     # Viedma
    cwd     = os.getcwd()
    image   = img.imread(cwd+"\TP3\Argentina.png")
    fig     = plt.figure(1)
    ax      = fig.gca()
    plt.imshow(image)
    figure  = ax.plot(coordenadas[recorrido[0]][0], coordenadas[recorrido[0]][1], marker= "o", color= "b")
    for i in range(23):
        desde   = recorrido[i]
        hacia   = recorrido[i + 1]
        coordx  = [coordenadas[desde][0], coordenadas[hacia][0]]
        coordy  = [coordenadas[desde][1], coordenadas[hacia][1]]
        figure  = ax.plot(coordx, coordy, c= 'r')
    plt.show()