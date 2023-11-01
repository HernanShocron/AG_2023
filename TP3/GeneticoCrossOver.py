import numpy as py
import random as rd


def CrossOver(poblacion, probabilidad, cant_gen):

    lista = []

    # for i in range(len(poblacion)):
    #     # Convertir a lista de bits
    #     lista.append(list(np.binary_repr(poblacion[i], width=cant_gen)))

    for i in range(0, len(poblacion), 2):
        if rd.random() <= probabilidad:
            punto_inicio = 0  # Iniciamos en el índice 0 de "padre 1"
            hijo1 = [-1] * cant_gen
            hijo2 = [-1] * cant_gen
            current = punto_inicio

            # Proceso para el hijo 1
            while True:
                if hijo1[current] == -1:
                    hijo1[current] = lista[i][current]
                current = lista[i + 1].index(lista[i][current])

                if current == punto_inicio:
                    break

            # Completar los genes faltantes de hijo 1 con los de "padre 2"
            for j in range(cant_gen):
                if hijo1[j] == -1:
                    hijo1[j] = lista[i + 1][j]

            # Proceso para el hijo 2
            current = punto_inicio
            while True:
                if hijo2[current] == -1:
                    hijo2[current] = lista[i + 1][current]
                current = lista[i].index(lista[i + 1][current])

                if current == punto_inicio:
                    break

            # Completar los genes faltantes de hijo 2 con los de "padre 1"
            for j in range(cant_gen):
                if hijo2[j] == -1:
                    hijo2[j] = lista[i][j]

            lista[i] = hijo1
            lista[i + 1] = hijo2

    # # Convertir de nuevo a decimal
    # lista_decimal = [int(''.join(gen), 2) for gen in lista]
    return lista
