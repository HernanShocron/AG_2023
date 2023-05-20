#la funcion acepta como parametro la poblacion y el nro de cromosomas que seran
#elegidos para la siguiente generacion y devuelve el array con esos cromosomas
def elitismo(poblacion, nroElitismo):
    poblacion.sort(reverse = True)
    elite = []
    for i in range(nroElitismo):
        elite[i] = poblacion[i]
    return elite

