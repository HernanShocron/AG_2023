import random as r

def seleccion(resultados,fitness,cantidad_poblacion):
    print("*** Seleccion_ruleta ***")
    cromosomas = []
    for i in range(cantidad_poblacion):                 # Se tiene que generar una nueva población igual en tamaño a la población inicial a partir de los resultados anteriores obtenidos
        seleccion = r.random()                          # Devuelve un valor entre 0 y 1 y se almacena en una variable de selección
        for j in range(len(fitness)):                   # Recorre la colección de firness
            if seleccion <= fitness[j]:                 # Si el numero aleatorio es menor ó igual al fitness actual, quiere decir que cayó en su rango
                cromosomas.append(resultados[j])        # Se agrega el cromosoma relacionado en la coleccion resultado a la nueva población de cromosomas
                break
            else:
                seleccion -= fitness[j]                 # De lo contrario se reduce el valor del número aleatorio de selección para evaluarlo en el siguiente fitness
    return cromosomas                                   # NOTA: Lo desarrollé de esta manera para que se pueda obtener el nuevo conjunto de cromosomas independientemente del tamaño de la población


# Prueba de ejecución (se puede borrar)
# cromosomas = []
# resultados = ['00000','00001','00010','00011','00100']
# fitness = [0.1,0.05,0.3,0.15,0.35]
# cromosomas = seleccion(resultados,fitness,5)
# print(cromosomas)