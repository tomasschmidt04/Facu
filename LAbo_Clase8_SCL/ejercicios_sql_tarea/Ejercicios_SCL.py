# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import pandas as pd
from inline_sql import sql, sql_val

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
               """
imprimirEjercicio(consigna, [depto], consultaSQL)









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

