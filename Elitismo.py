# la funcion acepta como parametro la poblacion, su fitness y el nro de cromosomas que seran
# elegidos para la siguiente generacion y devuelve el array con esos cromosomas
def elitismo(poblacion, pobl_fit, nroElitismo):
    # creo otra variable para no modificar la poblacion
    poblacion_ordenada = poblacion.copy()
    for i in range(len(poblacion)-1):
        for j in range(i, len(poblacion)):
            if (pobl_fit[i] < pobl_fit[j]):
                buffer = poblacion_ordenada[i]
                poblacion_ordenada[i] = poblacion_ordenada[j]
                poblacion_ordenada[j] = buffer
                buffer = pobl_fit[i]
                pobl_fit[i] = pobl_fit[j]
                pobl_fit[j] = buffer
    elite = []
    for i in range(nroElitismo):
        elite[i] = poblacion_ordenada[i]
    return elite
