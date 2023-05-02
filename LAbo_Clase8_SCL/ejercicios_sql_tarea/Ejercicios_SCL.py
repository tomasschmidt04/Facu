# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import pandas as pd
from inline_sql import sql, sql_val
import numpy as np

def imprimirEjercicio(consigna, listaDeDataframesDeEntrada, consultaSQL):
    
    print("# -----------------------------------------------------------------------------")
    print("# Consigna: ", consigna)
    print("# -----------------------------------------------------------------------------")
    print()
    for i in range(len(listaDeDataframesDeEntrada)):
        print("# Entrada 0",i,sep='')
        print("# -----------")
        print(listaDeDataframesDeEntrada[i])
        print()
    print("# SQL:")
    print("# ----")
    print(consultaSQL)
    print()
    print("# Salida:")
    print("# -------")
    print(sql^ consultaSQL)
    print()
    print("# -----------------------------------------------------------------------------")
    print("# -----------------------------------------------------------------------------")
    print()
    print()



casos      = pd.read_csv("casos.csv")    
depto      = pd.read_csv("departamento.csv")     
grupoetario = pd.read_csv("grupoetario.csv")    
provincia   = pd.read_csv("provincia.csv")    
tipo_evento = pd.read_csv("tipoevento.csv")    


consigna    = "ej 1 Listar sólo los nombres de todos los departamentos que hay en la tabla departamento (dejando los registros repetidos)."
consultaSQL = """
                SELECT  descripcion 
                FROM depto;
               """
imprimirEjercicio(consigna, [depto], consultaSQL) 

consigna    = "ej 2 Listar sólo los nombres de todos los departamentos que hay en la tabla departamento (SIN dejar los registros repetidos)."
consultaSQL = """
                SELECT DISTINCT descripcion 
                FROM depto;
               """
imprimirEjercicio(consigna, [depto], consultaSQL) 

consigna    = "ej 3 Listar sólo los códigos de departamento y sus nombres de todos los departamentos que hay en la tabla departamento."
consultaSQL = """
                SELECT DISTINCT id, descripcion 
                FROM depto;
               """
imprimirEjercicio(consigna, [depto], consultaSQL) 

consigna    = "ej 4 Listar TODAS las columnas de la tabla departamentos"
consultaSQL = """
                SELECT DISTINCT * 
                FROM depto;
               """
imprimirEjercicio(consigna, [depto], consultaSQL) 

consigna    = "ej 5 Listar los códigos de departamento y nombres de todos los departamentos que hay en la tabla departamento. Utilizar los siguientes alias para las columnas: codigo_depto, nombre_depto"
consultaSQL = """
                SELECT DISTINCT id as codigo_depto,descripcion as nombre_depto
                FROM depto;
               """
imprimirEjercicio(consigna, [depto], consultaSQL) 

consigna    = "ej 6 Listar los códigos de departamento y sus nombres, ordenados por sus nombres de manera descendentes (de la Z a la A). En caso de empate, desempatar por código de departamento de manera ascendente."
consultaSQL = """
                SELECT DISTINCT id as codigo_depto,descripcion as nombre_depto
                FROM depto
                ORDER BY descripcion DESC 
              
               
               """
imprimirEjercicio(consigna, [depto], consultaSQL) 
#!!!!!MAAAAAAL
#No se como poner dos condiciones(CASE tal vez)
consigna    = "ej g Listar los registros de la tabla departamento cuyo código de provincia es igual a 54"
consultaSQL = """
                SELECT DISTINCT descripcion, id_provincia
                FROM depto
                WHERE id_provincia = 54
               
               """
imprimirEjercicio(consigna, [depto], consultaSQL)

consigna    = "ej h Listar los registros de la tabla departamento cuyo código de provincia es igual a 22, 78 u 86"
consultaSQL = """
                SELECT DISTINCT descripcion, id_provincia
                FROM depto
                WHERE id_provincia = 22 or id_provincia = 78 or id_provincia = 86               
               """
imprimirEjercicio(consigna, [depto], consultaSQL)

consigna    = "ej i Listar los registros de la tabla departamento cuyos códigos de provincia se encuentren entre el 50 y el 59 (ambos valores inclusive)"
consultaSQL = """
                SELECT DISTINCT descripcion, id_provincia
                FROM depto
                WHERE id_provincia >= 22  and id_provincia <= 86               
               """
imprimirEjercicio(consigna, [depto], consultaSQL)

consigna    = "ej j Listar los registros de la tabla provincia cuyos nombres comiencen con la letra M."
consultaSQL = """
                SELECT DISTINCT descripcion, id
                FROM provincia
                WHERE descripcion LIKE 'M%'           
               """
imprimirEjercicio(consigna, [depto], consultaSQL)



onsigna    = "ej k LListar los registros de la tabla provincia cuyos nombres comiencen con la letra S y su quinta letra sea una letra A."
consultaSQL = """
                SELECT DISTINCT descripcion, id
                FROM provincia
                WHERE descripcion LIKE 'S%' and descripcion LIKE '_____a%'             
               """
imprimirEjercicio(consigna, [depto], consultaSQL)

consigna    = "ej l Listar los registros de la tabla provincia cuyos nombres terminan con la letra A"
consultaSQL = """
                SELECT DISTINCT descripcion, id
                FROM provincia
                WHERE descripcion LIKE '%A' or  descripcion LIKE '%a'  
               """
imprimirEjercicio(consigna, [depto], consultaSQL)

consigna    = "ej m Listar los registros de la tabla provincia cuyos nombres tengan exactamente 5 letras."
consultaSQL = """
                SELECT DISTINCT descripcion, id
                FROM provincia
                WHERE len(descripcion) = 5        
               """
imprimirEjercicio(consigna, [depto], consultaSQL)

consigna    = "ej n Listar los registros de la tabla provincia cuyos nombres tengan ”do” en alguna parte de su nombre."
consultaSQL = """
                SELECT DISTINCT descripcion, id
                FROM provincia
                WHERE descripcion LIKE '%do%'
              """
imprimirEjercicio(consigna, [depto], consultaSQL)

consigna    = "ej o. Listar los registros de la tabla provincia cuyos nombres tengan ”do” en alguna parte de su nombre y su código sea menor a 30. "
consultaSQL = """
                SELECT DISTINCT descripcion, id
                FROM provincia
                WHERE descripcion LIKE '%do%' and id < 30     
               """
imprimirEjercicio(consigna, [depto], consultaSQL)

consigna    = "ej p. Listar los registros de la tabla departamento cuyos nombres  tengan ”san” en alguna parte de su nombre. Listar sólo id y descripcion. Utilizar los siguientes alias para las columnas: codigo_depto y nombre_depto, respectivamente. El resultado debe estar ordenado por sus nombres de manera descendentes (de la Z a la A)."
consultaSQL = """
                SELECT DISTINCT descripcion as nombre_depto , id as codigo_depto
                FROM depto
                WHERE descripcion LIKE '%san%' or  descripcion LIKE '%San%'
                ORDER BY descripcion DESC
               """
#imprimirEjercicio(consigna, [depto], consultaSQL)
#B. Consultas multitabla (INNER JOIN)
#a. Devolver una lista con los código y nombres de departamentos, asociados al nombre de la provincia al que pertenecen.
#b. Devolver una lista con los código y nombres de departamentos, asociados al nombre de la provincia al que pertenecen. Ordenar el resultado por nombre de provincia de manera ascendente, y dentro de cada una de ellas por nombre de departamento, también de manera ascendente. c. Devolver los casos registrados en la provincia de “Chaco”. 
#d. Devolver aquellos casos de la provincia de “Buenos Aires” cuyo campo cantidad supere los 10 casos.
#e. Devolver aquellos casos de las provincias cuyo nombre terminen con la letra a y el campo cantidad supere 10. Mostrar: nombre de provincia, nombre de departamento, año, semana epidemiológica, descripción de grupo etario y cantidad. Ordenar el resultado por la cantidad (descendente), luego por el nombre de la provincia (ascendente), nombre del departamento (ascendente), año     (ascendente) y la descripción del grupo etario (ascendente).
#f. Ídem anterior, pero devolver sólo aquellas tuplas que tienen el máximo en el campo cantidad.


consigna    = "ej a. Devolver una lista con los código y nombres de departamentos, asociados al nombre de la provincia al que pertenecen."
consultaSQL = """
                SELECT DISTINCT depto.descripcion, depto.id, provincia.descripcion
                FROM depto
                JOIN provincia
                ON  depto.id_provincia = provincia.id
               """
imprimirEjercicio(consigna, [depto], consultaSQL)

consigna    = "ej b. Devolver una lista con los código y nombres de departamentos, asociados al nombre de la provincia al que pertenecen. Ordenar el resultado por nombre de provincia de manera ascendente, y dentro de cada una de ellas por nombre de departamento, también de manera ascendente. " 

consultaSQL = """
                SELECT DISTINCT depto.descripcion, depto.id, provincia.descripcion
                FROM depto
                JOIN provincia
                ON  depto.id_provincia = provincia.id  
                ORDER BY provincia.descripcion ASC, depto.descripcion ASC
               """
imprimirEjercicio(consigna, [depto], consultaSQL)

consigna    = "ej c. Devolver los casos registrados en la provincia de “Chaco”."
consultaSQL = """
                SELECT DISTINCT cantidad, id_provincia, depto.id_provincia, provincia.descripcion
                FROM provincia
                INNER JOIN depto
                ON  depto.id_provincia = provincia.id
                INNER JOIN casos
                ON depto.id = casos.id_depto
                WHERE provincia.descripcion = 'Chaco'
                 
                
               """
imprimirEjercicio(consigna, [depto], consultaSQL)


consigna    = "ej d. Devolver aquellos casos de la provincia de “Buenos Aires” cuyo campo cantidad supere los 10 casos. "
consultaSQL = """
                SELECT DISTINCT casos.id , cantidad, id_provincia, depto.id_provincia, provincia.descripcion
                FROM provincia
                INNER JOIN depto
                ON  depto.id_provincia = provincia.id
                INNER JOIN casos
                ON depto.id = casos.id_depto
                WHERE provincia.descripcion = 'Buenos Aires' and cantidad >10
                 
                
               
               """
imprimirEjercicio(consigna, [depto], consultaSQL)

consigna    = "ej e. Devolver aquellos casos de las provincias cuyo nombre terminen con la letra a y el campo cantidad supere 10. Mostrar: nombre de provincia, nombre de departamento, año, semana epidemiológica, descripción de grupo etario y cantidad. Ordenar el resultado por la cantidad (descendente), luego por el nombre de la provincia (ascendente), nombre del departamento (ascendente), año     (ascendente) y la descripción del grupo etario (ascendente)."
consultaSQL = """
                SELECT DISTINCT provincia.descripcion , depto.descripcion, anio, semana_epidemiologica, grupoetario.descripcion, cantidad 
                FROM provincia
                INNER JOIN depto
                ON  depto.id_provincia = provincia.id
                INNER JOIN casos
                ON depto.id = casos.id_depto
                INNER JOIN grupoetario
                ON casos.id_grupoetario =  grupoetario.id
                WHERE provincia.descripcion LIKE '%a'  and cantidad > 10
                ORDER BY cantidad DESC, provincia.descripcion ASC, depto.descripcion ASC, anio ASC, grupoetario.descripcion ASC
                
               """
imprimirEjercicio(consigna, [depto,provincia,casos], consultaSQL)

#C. Consultas multitabla (OUTER JOIN)
#a. Devolver un listado con los nombres de los departamentos que no  ienen ningún caso asociado.
#b. Devolver un listado con los tipos de evento que no tienen ningún caso asociado.


consigna    = "ej a. Devolver un listado con los nombres de los departamentos que no  ienen ningún caso asociado."
consultaSQL = """
                SELECT DISTINCT  *
                FROM depto
                 INNER  JOIN casos
                ON depto.id = casos.id_depto
                
               """
#NINGUNO PORQUE INNER JOIN TIENE TODOS LOS ELEMENTOS DE LA LISTA AMS GARNDE, POR LO QUE SIEMPRE HAY RELACION
imprimirEjercicio(consigna, [depto,casos], consultaSQL)


consigna    = "ej b. Devolver un listado con los tipos de evento que no tienen ningún caso asociado."
consultaSQL = """
                SELECT DISTINCT * 
                FROM tipo_evento
                LEFT OUTER  JOIN casos
                ON tipo_evento.id = casos.id_tipoevento 
                where tipo_evento.id =2 or tipo_evento.id =3 
     """          """
imprimirEjercicio(consigna, [depto], consultaSQL)
a. Calcular la cantidad total de casos que hay en la tabla casos.
b. Calcular la cantidad total de casos que hay en la tabla casos para cada año y cada tipo de caso. Presentar la información de la siguiente manera: descripción del tipo de caso, año y cantidad. Ordenarlo por tipo de caso (ascendente) y año (ascendente).
c. Misma consulta que el ítem anterior, pero sólo para el año 2019.
d. Calcular la cantidad total de departamentos que hay por provincia. Presentar la información ordenada por código de provincia.
e. Listar los departamentos con menos cantidad de casos en el año 2019.
f. Listar los departamentos con más cantidad de casos en el año 2020.
g. Listar el promedio de cantidad de casos por provincia y año.
h. Listar, para cada provincia y año, cuáles fueron los departamentos que más cantidad de casos tuvieron.
i. Mostrar la cantidad de casos total, máxima, mínima y promedio que tuvo la provincia de Buenos Aires en el año 2019.
j. Misma consulta que el ítem anterior, pero sólo para aquellos casos en que la cantidad total es mayor a 1000 casos.
k. Listar los nombres de departamento (y nombre de provincia) que tienenmediciones tanto para el año 2019 como para el año 2020. Para cada uno de ellos devolver la cantidad de casos promedio. Ordenar por nombre de provincia (ascendente) y luego por nombre de departamento (ascendente).
l. Devolver una tabla que tenga los siguientes campos: descripción de tipo de evento, id_depto, nombre de departamento, id_provincia, nombre de
 provincia, total de casos 2019, total de casos 2020
"""
#D. Consultas resumen
consigna    = "ej  a. Calcular la cantidad total de casos que hay en la tabla casos."
consultaSQL = """
                SELECT count(*) as casos_totales
                FROM casos
                
               """

imprimirEjercicio(consigna, [casos], consultaSQL)
consigna    = "ej  b. Calcular la cantidad total de casos que hay en la tabla casos para cada año y cada tipo de caso. Presentar la información de la siguiente manera: descripción del tipo de caso, año y cantidad. Ordenarlo por tipo de caso (ascendente) y año (ascendente)."
consultaSQL = """
                SELECT anio, id_tipoevento, count(*) as casos_totales
                FROM casos
                GROUP BY anio, id_tipoevento
                ORDER BY anio ASC
                
               """

imprimirEjercicio(consigna, [casos], consultaSQL)

consigna    = "ej  c. Misma consulta que el ítem anterior, pero sólo para el año 2019."

consultaSQL = """
                SELECT anio, id_tipoevento, count(*) as casos_totales
                FROM casos
                GROUP BY anio, id_tipoevento
                HAVING anio = 2019
                ORDER BY anio ASC
              
                
               """

imprimirEjercicio(consigna, [casos], consultaSQL)

consigna    = "ej  d. Calcular la cantidad total de departamentos que hay por provincia. Presentar la información ordenada por código de provincia."

consultaSQL = """
                SELECT provincia.id, provincia.descripcion , count(*) as casos_totales
                FROM provincia
                INNER JOIN depto
                ON provincia.id = id_provincia
                GROUP BY provincia.descripcion, provincia.id
                ORDER BY provincia.id
                
               """

imprimirEjercicio(consigna, [casos], consultaSQL)
consigna    = "ej  e. Listar los departamentos con menos cantidad de casos en el año 2019."


consultaSQL = """
                SELECT  depto.id , anio, SUM(cantidad) as casos_totales
                FROM casos
                INNER JOIN depto
                ON depto.id= casos.id_depto
                GROUP BY depto.id,anio
                HAVING anio = 2019
                ORDER BY casos_totales ASC
                
                
               """

imprimirEjercicio(consigna, [casos], consultaSQL)

consigna    = "ej  f. Listar los departamentos con más cantidad de casos en el año 2020."


consultaSQL = """
                SELECT  depto.id , anio, SUM(cantidad) as casos_totales
                FROM casos
                INNER JOIN depto
                ON depto.id= casos.id_depto
                GROUP BY depto.id,anio
                HAVING anio = 2020
                ORDER BY casos_totales DESC
                
                
               """

imprimirEjercicio(consigna, [casos], consultaSQL)

consigna    = "ej  g. Listar el promedio de cantidad de casos por provincia y año."


consultaSQL = """
                SELECT  provincia.descripcion, anio, AVG(cantidad) as promedio_casos
                FROM casos
                INNER JOIN depto
                ON depto.id= casos.id_depto
                INNER JOIN provincia
                ON  provincia.id = depto.id_provincia
                GROUP BY provincia.descripcion,anio
                
                
               """

imprimirEjercicio(consigna, [casos], consultaSQL)

consigna    = "ej  h. Listar, para cada provincia y año, cuáles fueron los departamentos que más cantidad de casos tuvieron."


consultaSQL = """
                SELECT  provincia.descripcion, anio, depto.id, SUM(cantidad) as casos_totales
                FROM casos
                INNER JOIN depto
                ON depto.id= casos.id_depto
                INNER JOIN provincia
                ON  provincia.id = depto.id_provincia
                GROUP BY provincia.descripcion,anio,depto.id
                
                
               """

imprimirEjercicio(consigna, [casos], consultaSQL)

consigna    = "ej  i. Mostrar la cantidad de casos total, máxima, mínima y promedio que tuvo la provincia de Buenos Aires en el año 2019. "


consultaSQL = """
                SELECT  provincia.descripcion, anio, MIN(cantidad) ,MAX(cantidad), SUM(cantidad) as casos_totales
                FROM casos
                INNER JOIN depto
                ON depto.id= casos.id_depto
                INNER JOIN provincia
                ON  provincia.id = depto.id_provincia
                GROUP BY provincia.descripcion,anio,
                HAVING provincia.descripcion = 'Buenos Aires' AND anio = 2019
                
                
               """

imprimirEjercicio(consigna, [casos], consultaSQL)

consigna    = "ej  j. Misma consulta que el ítem anterior, pero sólo para aquellos casos en que la cantidad total es mayor a 1000 casos. "


consultaSQL = """
                SELECT  provincia.descripcion, anio, MIN(cantidad) ,MAX(cantidad), SUM(cantidad) as casos_totales
                FROM casos
                INNER JOIN depto
                ON depto.id= casos.id_depto
                INNER JOIN provincia
                ON  provincia.id = depto.id_provincia
                GROUP BY provincia.descripcion,anio
                HAVING casos_totales >1000
                
                
               """
consigna    = "ej  k. Listar los nombres de departamento (y nombre de provincia) que tienen mediciones tanto para el año 2019 como para el año 2020. Para cada uno de ellos devolver la cantidad de casos promedio. Ordenar por nombre de provincia (ascendente) y luego por nombre de departamento (ascendente)."


ejk = """
                SELECT casos_por_depto2019.descripcion,barrio_2019, a_2019,casos_totales_2019, a_2020, casos_totales_2020
                FROM casos_por_depto2019 
                INNER JOIN  casos_por_depto2020
                ON barrio_2020 =  barrio_2019
                
    """
imprimirEjercicio(consigna, [casos], consultaSQL)
ejk = sql^ ejk
    
    
casos_por_depto2019 = """
                        SELECT  provincia.descripcion, depto.descripcion as barrio_2019,anio as a_2019,  SUM(cantidad) as casos_totales_2019
                        FROM casos
                        INNER JOIN depto
                        ON depto.id= casos.id_depto
                        INNER JOIN provincia
                        ON  provincia.id = depto.id_provincia
                        GROUP BY provincia.descripcion,anio,depto.descripcion
                        HAVING anio = 2019 and casos_totales_2019> 1
    
    
    
    """
casos_por_depto2019 = sql^ casos_por_depto2019 
casos_por_depto2020 = sql^ casos_por_depto2020
imprimirEjercicio(consigna, [casos], casos_por_depto2019)
                 
casos_por_depto2020 = """
                        SELECT  provincia.descripcion,depto.descripcion barrio_2020, anio as a_2020,  SUM(cantidad) as casos_totales_2020
                        FROM casos
                        INNER JOIN depto
                        ON depto.id= casos.id_depto
                        INNER JOIN provincia
                        ON  provincia.id = depto.id_provincia
                        GROUP BY provincia.descripcion,anio,depto.descripcion
                        HAVING anio = 2020 and casos_totales_2020 > 1
    
    
    
    """

imprimirEjercicio(consigna, [casos], casos_por_depto2020)

"""
E. Subconsultas (ALL, ANY)
a. Devolver el departamento que tuvo la mayor cantidad de casos sin hacer uso de MAX, ORDER BY ni LIMIT.
b. Devolver los tipo de evento que tienen casos asociados. (Utilizando ALL o
ANY).
F. Subconsultas (IN, NOT IN)
a. Devolver los tipo de evento que tienen casos asociados (Utilizando IN, NOT
IN).
b. Devolver los tipo de evento que NO tienen casos asociados (Utilizando IN,
NOT IN).
G. Subconsultas (EXISTS, NOT EXISTS)
a. Devolver los tipo de evento que tienen casos asociados (Utilizando EXISTS,
NOT EXISTS).
b. Devolver los tipo de evento que NO tienen casos asociados (Utilizando IN,
NOT IN).
H. Subconsultas correlacionadas
a. Listar las provincias que tienen una cantidad total de casos mayor al
promedio de casos del país. Hacer el listado agrupado por año.
b. Por cada año, listar las provincias que tuvieron una cantidad total de casos
mayor a la cantidad total de casos que la provincia de Corrientes.
"""
consigna    = "ej  a. Devolver el departamento que tuvo la mayor cantidad de casos sin hacer uso de MAX, ORDER BY ni LIMIT."


consultaSQL = """
                SELECT  depto.descripcion, SUM(cantidad) as casos_totales
                FROM casos
                INNER JOIN depto
                ON depto.id = casos.id_depto
                GROUP BY depto.descripcion
                WHERE casos_totales = ALL
                (SELECT  SUM(cantidad) as casos_totales
                FROM casos
                INNER JOIN depto
                ON depto.id = casos.id_depto
                GROUP BY depto.descripcion
                    )
                
                
               """

imprimirEjercicio(consigna, [casos], consultaSQL)

consigna    = "ej  b. Devolver los tipo de evento que tienen casos asociados. (Utilizando ALL o ANY). "


consultaSQL = """
                SELECT  provincia.descripcion, anio, MIN(cantidad) ,MAX(cantidad), SUM(cantidad) as casos_totales
                FROM casos
                INNER JOIN depto
                ON depto.id= casos.id_depto
                INNER JOIN provincia
                ON  provincia.id = depto.id_provincia
                GROUP BY provincia.descripcion,anio,
                HAVING provincia.descripcion = 'Buenos Aires' AND anio = 2019
                
                
               """

imprimirEjercicio(consigna, [casos], consultaSQL)
consigna    = "ej  i. Mostrar la cantidad de casos total, máxima, mínima y promedio que tuvo la provincia de Buenos Aires en el año 2019. "


consultaSQL = """
                SELECT  provincia.descripcion, anio, MIN(cantidad) ,MAX(cantidad), SUM(cantidad) as casos_totales
                FROM casos
                INNER JOIN depto
                ON depto.id= casos.id_depto
                INNER JOIN provincia
                ON  provincia.id = depto.id_provincia
                GROUP BY provincia.descripcion,anio,
                HAVING provincia.descripcion = 'Buenos Aires' AND anio = 2019
                
                
               """

imprimirEjercicio(consigna, [casos], consultaSQL)



def imprimirEjercicio(consigna, listaDeDataframesDeEntrada, consultaSQL):
    
    print("# -----------------------------------------------------------------------------")
    print("# Consigna: ", consigna)
    print("# -----------------------------------------------------------------------------")
    print()
    for i in range(len(listaDeDataframesDeEntrada)):
        print("# Entrada 0",i,sep='')
        print("# -----------")
        print(listaDeDataframesDeEntrada[i])
        print()
    print("# SQL:")
    print("# ----")
    print(consultaSQL)
    print()
    print("# Salida:")
    print("# -------")
    print(sql^ consultaSQL)
    print()
    print("# -----------------------------------------------------------------------------")
    print("# -----------------------------------------------------------------------------")
    print()
    print()

