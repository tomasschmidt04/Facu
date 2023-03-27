import csv

def cuantas_materias(filas,cuatri):
    materias_a_cursar = []
    for fila in filas:
        if fila[0] == cuatri:
            materias_a_cursar.append(fila[1])
    return materias_a_cursar



with open ("cronograma_sugerido.csv",encoding= "UTF-8") as texto:
    filas = csv.reader(texto)
    n  = input("Escriba el cuatrimestre: ")
    while 2 >= int(n) or int(n) >= 9:
        n = input("El cuarimestre ingresado no existe; Intente nuevamente : ")
    cant_materias = cuantas_materias(filas,n)

print(f"La cant. de materia a cursar en el cuatri {n} son {cant_materias}")



dias_ingles={
    "lunes" : "monday",
    "martes": "tuesday"
}
print(dias_ingles["lunes"])
dias_ingles["mier"] = "Wednesday"
print(dias_ingles["mier"])
print(dias_ingles)
#EJERCICIO DE REGISTROS

def materias_cuatrimestre(lista,n):
    lista_materias = [] #Lo debo devolver en una LISTA de diccionarios
    for fila in lista:
        if fila[0] == n:
            lista_materias.append(fila)
    return lista_materias



def registros():
    lista = []
    with open("cronograma_sugerido.csv", 'rt') as f:
        filas = csv.reader(f)
        encabezado = next(filas)
        for fila in filas:
            registro = dict(zip(encabezado,fila)) # armo el diccionario de cada fila # El encabezado tiene 3 elementos y luego cada fila tiene 3 eementos. Entonces cada encabezado le correponde un elemento.
            lista.append(registro) # lo agrego a la lista
    return lista

n = input("Cuatrimestre a cursar: ")
print(f"Las materias a cursar en el cuatr{n} son : {materias_cuatrimestre(registros(),n)}")




