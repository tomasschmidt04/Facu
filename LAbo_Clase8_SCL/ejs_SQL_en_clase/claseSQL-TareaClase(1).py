# -*- coding: utf-8 -*-
"""
Materia: Laboratorio de datos - FCEyN - UBA
Clase  : Clase SQL. Script clase.
Autor  : Pablo Turjanski
Fecha  : 2023-03-07
"""

# Importamos bibliotecas
import pandas as pd
from inline_sql import sql, sql_val

def main():

    print()
    print("# =============================================================================")
    print("# Creamos los datasets que vamos a utilizar en este programa")
    print("# =============================================================================")
    
    # Ejercicios AR-PROJECT, SELECT, RENAME
    empleado       = get_empleado()
    # Ejercicios AR-UNION, INTERSECTION, MINUS
    alumnosBD      = get_alumnosBD()
    alumnosTLeng   = get_alumnosTLeng()
    # Ejercicios AR-CROSSJOIN
    persona        = get_persona_ejemploCrossJoin()
    nacionalidades = get_nacionalidades()
    # Ejercicios ¿Mismos Nombres?
    se_inscribe_en=get_se_inscribe_en_ejemploMismosNombres()
    materia       =get_materia_ejemploMismosNombres()
    # Ejercicio JOIN múltiples tablas
    vuelo      = pd.read_csv("vuelo.csv")    
    aeropuerto = pd.read_csv("aeropuerto.csv")    
    pasajero   = pd.read_csv("pasajero.csv")    
    reserva    = pd.read_csv("reserva.csv")    
    # Ejercicio JOIN tuplas espúreas
    empleadoRol= pd.read_csv("empleadoRol.csv")    
    rolProyecto= pd.read_csv("rolProyecto.csv")    
    # Ejercicios funciones de agregación, LIKE, Elección, Subqueries y variables de Python
    examen     = pd.read_csv("examen.csv")
    # Ejercicios de manejo de valores NULL
    examen03 = pd.read_csv("examen03.csv")
    
 #%%
    print()
    print("# =============================================================================")
    print("# Ejercicios 1 AEROPUERTO")
    print("# =============================================================================")
    
    consigna    = "Retornar codigo y nombre de los aeropuuertos de londres"
    consultaSQL = """
                   SELECT DISTINCT codigo, nombre
                   FROM aeropuerto;
                  """
    imprimirEjercicio(consigna, [aeropuerto], consultaSQL)    

        
    print()
    print("# =============================================================================")
    print("# Ejercicios 2 AEROPUERTO")
    print("# =============================================================================")
    
    consigna    = "Listar las ciudades como city cuyo codigo sea ORY o CDG"
    consultaSQL = """
                   SELECT DISTINCT Ciudad AS city
                   FROM aeropuerto
                   WHERE codigo='ORY' or codigo='CDG';
                  """
    imprimirEjercicio(consigna, [aeropuerto], consultaSQL)    
    
    print()
    print("# =============================================================================")
    print("# Ejercicios 3 VUELO")
    print("# =============================================================================")
    
    consigna    = "Obtener los numeros de vuelo que van desde CDG hacia LHR"
    consultaSQL = """
                   SELECT DISTINCT numero
                   FROM vuelo
                   WHERE origen='CDG' and destino='LHR';
                  """
    imprimirEjercicio(consigna, [vuelo], consultaSQL)   
    
    
    print("# =============================================================================")
    print("# Ejercicios 4 VUELO")
    print("# =============================================================================")
    
    consigna    = "Obtener los numeros de vuelo que van desde CDG hacia LHR o viceversa"
    consultaSQL = """
                   SELECT DISTINCT numero
                   FROM vuelo
                   WHERE (origen='CDG' and destino='LHR') OR (destino='CDG' and origen='LHR');
                  """
    imprimirEjercicio(consigna, [vuelo], consultaSQL)    
    
    print("# =============================================================================")
    print("# Ejercicios 5 RESERVA")
    print("# =============================================================================")
    
    consigna    = "Devolver las fechas de reservas cuyos precios son mayores a $200"
    consultaSQL = """
                   SELECT DISTINCT fecha
                   FROM reserva
                   WHERE precio>200;
                  """
    imprimirEjercicio(consigna, [reserva], consultaSQL)    
    
        
    print("# =============================================================================")
    print("# Ejercicios 6 VUELO Y RESERVA")
    print("# =============================================================================")
    
    consigna    = "Devolver los codigos de vuelo (numero) que tienen reservas generadas"
    consultaSQL = """
                   SELECT DISTINCT numero 
                   FROM vuelo
                   INTERSECT
                   SELECT DISTINCT NroVuelo
                   FROM reserva
                   
                  """
    imprimirEjercicio(consigna, [reserva, vuelo], consultaSQL)    
    
    print("# =============================================================================")
    print("# Ejercicios 7 VUELO Y RESERVA")
    print("# =============================================================================")
    
    consigna    = "Devolver los codigos de vuelo (numero) que aùn no tienen reservas generadas"
    consultaSQL = """
                   SELECT DISTINCT numero 
                   FROM vuelo
                   EXCEPT
                   SELECT DISTINCT NroVuelo
                   FROM reserva
                   
                  """
    imprimirEjercicio(consigna, [reserva, vuelo], consultaSQL)  
    
    print("# =============================================================================")
    print("# Ejercicios 6 CODIGOS Y RESERVA")
    print("# =============================================================================")
    
    consigna    = "Devolver los codigos de aeropuerto de los que parten o arriban los vuelos"
    consultaSQL = """
                   SELECT DISTINCT codigo 
                   FROM aeropuerto
                   INTERSECT
                   (SELECT DISTINCT origen
                   FROM vuelo
                   UNION
                   SELECT DISTINCT destino
                   FROM vuelo
                   )
                  """
    imprimirEjercicio(consigna, [aeropuerto, vuelo], consultaSQL)    
    
    print("# =============================================================================")
    print("# Ejercicios 6 CODIGOS Y RESERVA")
    print("# =============================================================================")
    
    consigna    = "Devolver el nombre de la ciudad de partida del vuelo nùmero 165"
    consultaSQL = """
                   SELECT DISTINCT ciudad 
                   FROM vuelo
                   INNER JOIN aeropuerto 
                   ON origen = codigo
                   WHERE Numero = 165
                  """
    imprimirEjercicio(consigna, [aeropuerto, vuelo], consultaSQL)    

    print("# =============================================================================")
    print("# Ejercicios 6 CODIGOS Y RESERVA")
    print("# =============================================================================")
    
    consigna    = "Retornar el nombre de las personas que realiuzaron reservas a un valor menos a $200"
    consultaSQL = """
                   SELECT DISTINCT Nombre 
                   FROM reserva
                   INNER JOIN pasajero 
                   ON reserva.DNI = pasajero.DNI
                   WHERE precio<200
                  """
    imprimirEjercicio(consigna, [reserva, pasajero], consultaSQL)    

    print("# =============================================================================")
    print("# Ejercicios 6 CODIGOS Y RESERVA")
    print("# =============================================================================")
    
    consigna    = "Obtener nombre, fecha y destino del viaje de todos los pasajeros que vuelan desde madrid"
    consultaSQL = """
                   SELECT DISTINCT nombre, fecha, destino 
                   FROM reserva
                   INNER JOIN pasajero 
                   ON reserva.DNI = pasajero.DNI
                   INNER JOIN vuelo 
                   ON numero=NroVuelo
                   WHERE origen = 'MAD'
                  """
    imprimirEjercicio(consigna, [reserva, pasajero, vuelo], consultaSQL)    
    """
                   SELECT DISTINCT nombre, fecha, destino 
                   FROM reserva, pasajero, vuelo
                   WHERE reserva.DNI = pasajero.DNI and numero=NroVuelo and origen = 'MAD'

     """
          
    print()
    print("# =============================================================================")
    print("# Ejemplo inicial")
    print("# =============================================================================")
    
    print(empleado)

    consultaSQL = """
                   SELECT DISTINCT DNI, Salario
                   FROM empleado;
     """


    dataframeResultado = sql^ consultaSQL
    
    print(dataframeResultado)


    print()
    print("# =============================================================================")
    print("# Ejercicios AR-PROJECT <-> SELECT")
    print("# =============================================================================")
    
    consigna    = "a.- Listar DNI y Salario de empleados "
    consultaSQL = """
                   SELECT DISTINCT DNI, Salario
                   FROM empleado;
                  """
    imprimirEjercicio(consigna, [empleado], consultaSQL)    
    
    # -----------
    consigna    = "b.- Listar Sexo de empleados "
    consultaSQL = """
                    SELECT DISTINCT Sexo
                    From empleado;
                  """
    imprimirEjercicio(consigna, [empleado], consultaSQL)    

    # -----------
    consigna    = "c.- Listar Sexo de empleados (sin DISTINCT)"
    consultaSQL = """
                    SELECT Sexo
                    From empleado;
                  """
    imprimirEjercicio(consigna, [empleado], consultaSQL)    

    print()
    print("# =============================================================================")
    print("# Ejercicios AR-SELECT <-> WHERE")
    print("# =============================================================================")
    
    consigna    = "a.- Listar de EMPLEADO sólo aquellos cuyo sexo es femenino"
    consultaSQL = """
                    SELECT DNI, Nombre, Sexo, Salario
                    From empleado
                    WHERE sexo = 'F'
                  """
    imprimirEjercicio(consigna, [empleado], consultaSQL)    

    # -----------
    consigna    = "b.- Listar de EMPLEADO aquellos cuyo sexo es femenino y su salario es mayor a $15.000"
    consultaSQL = """
                    SELECT DNI, Nombre, Sexo, Salario
                    From empleado
                    WHERE sexo = 'F' and salario>1500;
                  """
    imprimirEjercicio(consigna, [empleado], consultaSQL)    
    
    
    print()
    print("# =============================================================================")
    print("# Ejercicios AR-RENAME <-> AS")
    print("# =============================================================================")
    
    consigna    = """a.- Listar DNI y Salario de EMPLEADO, y renombrarlos como id e Ingreso"""
    consultaSQL = """
                    SELECT DNI AS id, Salario AS Ingreso
                    From empleado
                  """
    
    imprimirEjercicio(consigna, [empleado], consultaSQL)    
    
#%%
    print()
    print("# =============================================================================")
    print("# Ejercicios AR-UNION, INTERSECTION, MINUS <-> UNION, INTERSECTION, EXCEPT")
    print("# =============================================================================")

    consigna    = """a1.- Listar a los alumnos que cursan BDs o TLENG"""
    
    consultaSQL = """
                    SELECT DISTINCT *
                    FROM alumnosBD
                    UNION
                    SELECT DISTINCT *
                    FROM alumnosTLeng
                  """

    imprimirEjercicio(consigna, [alumnosBD, alumnosTLeng], consultaSQL)    


    # -----------
    consigna    = """a2.- Listar a los alumnos que cursan BDs o TLENG (usando UNION ALL)"""
    
    consultaSQL = """
                    SELECT DISTINCT *
                    FROM alumnosBD
                    UNION ALL
                    SELECT DISTINCT *
                    FROM alumnosTLeng
                  """

    imprimirEjercicio(consigna, [alumnosBD, alumnosTLeng], consultaSQL)    


    # -----------
    consigna    = """b.- Listar a los alumnos que cursan simultáneamente BDs y TLENG"""
    
    consultaSQL = """
                    SELECT DISTINCT *
                    FROM alumnosBD
                    INTERSECT
                    SELECT DISTINCT *
                    FROM alumnosTLeng
                  """

    imprimirEjercicio(consigna, [alumnosBD, alumnosTLeng], consultaSQL)    

    
    # -----------
    consigna    = """c.- Listar a los alumnos que cursan BDs y no cursan TLENG """
    
    consultaSQL = """
                    SELECT DISTINCT *
                    FROM alumnosBD
                    EXCEPT
                    SELECT DISTINCT *
                    FROM alumnosTLeng
                  """

    imprimirEjercicio(consigna, [alumnosBD, alumnosTLeng], consultaSQL)    
    
    
    
    
    print("# =============================================================================")
    print("# Ejercicios AR-... JOIN <-> ... JOIN")
    print("# =============================================================================")

    consigna    = """a1.- Listar el producto cartesiano entre las tablas persona y nacionalidades"""
    
    consultaSQL = """
                    SELECT DISTINCT *
                    FROM persona
                    CROSS JOIN nacionalidades
                  """

    imprimirEjercicio(consigna, [persona, nacionalidades], consultaSQL)


    # -----------
    consigna    = """a2.- Listar el producto cartesiano entre las tablas persona y nacionalidades (sin usar CROSS JOIN)"""
    
    consultaSQL = """
                    SELECT DISTINCT *
                    FROM persona, nacionalidades
                  """

    imprimirEjercicio(consigna, [persona, nacionalidades], consultaSQL)


    # ---------------------------------------------------------------------------------------------- 
    # Carga los nuevos datos del dataframe persona para los ejercicios de AR-INNER y LEFT OUTER JOIN
    # ----------------------------------------------------------------------------------------------
    persona        = get_persona_ejemplosJoin()
    # ----------------------------------------------------------------------------------------------
    
    
    consigna    = """b1.- Vincular las tablas persona y nacionalidades a través de un INNER JOIN"""
    
    consultaSQL = """
                    SELECT DISTINCT *
                    FROM persona
                    INNER JOIN nacionalidades
                    ON nacionalidad=IDN;
                  """
# LE AVISA AL MOTOR DE BASE DE DATOS QUE ES UNA CONDICIÒN SOBRE DOS TABLAS Y ME HACE MUCHO MAS RÀPIDA LA BUSQUEDA, RECORRE UNA DE LAS TABLAS Y RECORRE CON UN INDICE PARA VER DONDE ESTA LA TUPLA Y LA TRAE
    imprimirEjercicio(consigna, [persona, nacionalidades], consultaSQL)


    # -----------
    consigna    = """b2.- Vincular las tablas persona y nacionalidades (sin usar INNER JOIN)"""
    
    consultaSQL = """
                    SELECT DISTINCT *
                    FROM persona, nacionalidades 
# Cuando a partir de un "from" escribo varios df separados con una COMA, entonces SQL interpreta que estoy haciendo un producto cartesiano(CROSS PRODUCT)
#Entonces a partir de ese prodcuto, luego le meto varios "ON's" para hacer varios inner joins.                 
                    ON nacionalidad=IDN;
                  """

    imprimirEjercicio(consigna, [persona, nacionalidades], consultaSQL)


    # -----------
    consigna    = """c.- Vincular las tablas persona y nacionalidades a través de un LEFT OUTER JOIN"""
    
    consultaSQL = """
                    SELECT DISTINCT *
                    FROM persona
                    LEFT OUTER JOIN nacionalidades
                    ON nacionalidad=IDN;
                  """

    imprimirEjercicio(consigna, [persona, nacionalidades], consultaSQL)
    

    print("# =============================================================================")
    print("# Ejercicios SQL - ¿Mismos Nombres?")
    print("# =============================================================================")

    consigna    = """a.- Vincular las tablas Se_inscribe_en y Materia. Mostrar sólo LU y Nombre de materia"""
    
    consultaSQL = """
                    SELECT DISTINCT i.LU, m.Nombre
                    FROM se_inscribe_en AS i
                    INNER JOIN materia AS m
                    ON i.codigo_materia = m.codigo_materia;
                  """

    imprimirEjercicio(consigna, [se_inscribe_en, materia], consultaSQL)
 #                   """
 #                   SELECT DISTINCT LU, Nombre
 #                   FROM se_inscribe_en 
 #                   INNER JOIN materia 
 #                   ON se_inscribe_en.codigo_materia = materia.codigo_materia;
#                  """
    
    print("# =============================================================================")
    print("# Ejercicios SQL - Join de varias tablas en simultáneo")
    print("# =============================================================================")

    consigna    = """a.- Vincular las tablas Reserva, Pasajero y Vuelo. Mostrar sólo Fecha de reserva, hora de salida del vuelo y nombre de pasajero."""
    
    consultaSQL = """

                  """

    imprimirEjercicio(consigna, [reserva, pasajero, vuelo], consultaSQL)

    
    print("# =============================================================================")
    print("# Ejercicios SQL - Tuplas espúreas") 
# una de las dos columnas con las que haces el join tiene que ser superclave; (para que no se creen "datos espureos" osea datos falsos)
    # esta mal dividoda la tabla, si uno separa asì, pierde informaciòn
    print("# =============================================================================")

    consigna    = """a.- Vincular (JOIN)  EmpleadoRol y RolProyecto para obtener la tabla original EmpleadoRolProyecto"""
    
    consultaSQL = """
                    SELECT DISTINCT empleado,empleadoRol.rol,proyecto
                    FROM empleadoRol
                    INNER JOIN rolProyecto
                    ON empleadoRol.rol=rolProyecto.rol;
                  """


    imprimirEjercicio(consigna, [empleadoRol, rolProyecto], consultaSQL)

    print("# =============================================================================")
    print("# Ejercicios SQL - Funciones de agregación")
    print("# =============================================================================")

    consigna    = """a.- Usando sólo SELECT contar cuántos exámenes fueron rendidos (en total)"""
    
    consultaSQL = """
                     select count(*) AS cantidadExamenes
                     from  examen
                  """

    imprimirEjercicio(consigna, [examen], consultaSQL)


    # -----------
    consigna    = """b1.- Usando sólo SELECT contar cuántos exámenes fueron rendidos en cada Instancia"""
    
    consultaSQL = """
                     select Instancia, count(*) AS asistieron
                     from  examen
                     GROUP BY  Instancia
                  """

    imprimirEjercicio(consigna, [examen], consultaSQL)


    # -----------
    consigna    = """b2.- Usando sólo SELECT contar cuántos exámenes fueron rendidos en cada Instancia (ordenado por instancia)"""
    
    consultaSQL = """
                     select Instancia, count(*) AS asistieron
                     from  examen
                     GROUP BY  Instancia
                     Order by Instancia
                  """

    imprimirEjercicio(consigna, [examen], consultaSQL)


    # -----------
    consultaSQL = """
                     select Instancia, count(*) AS asistieron
                     from  examen
                     GROUP BY  Instancia
                     HAVING Asistieron < 4
                     Order by Instancia
                  """


    imprimirEjercicio(consigna, [examen], consultaSQL)


    # -----------
    consigna    = """c.- Mostrar el promedio de edad de los estudiantes en cada instancia de examen"""
    
    consultaSQL = """
                     select Instancia,AVG(Edad) AS PromedioEdad
                     from  examen
                     GROUP BY  Instancia
                     Order by Instancia
                  """


    imprimirEjercicio(consigna, [examen], consultaSQL)

    imprimirEjercicio(consigna, [examen], consultaSQL)


    print("# =============================================================================")
    print("# Ejercicios SQL - LIKE")
    print("# =============================================================================")

    consigna    = """a1.- Mostrar cuál fue el promedio de notas en cada instancia de examen, sólo para instancias de parcial."""
    
    consultaSQL = """
                     select Instancia,AVG(Nota) AS PromedioNota
                     from  examen
                     GROUP BY  Instancia
                     HAVING Instancia  LIKE  'Parcial %'
                     Order by Instancia
                  """
# having instancia = 'parcial%'
    imprimirEjercicio(consigna, [examen], consultaSQL)


    # -----------
    consigna    = """a2.- Mostrar cuál fue el promedio de notas en cada instancia de examen, sólo para instancias de parcial. Esta vez usando LIKE."""
    
    consultaSQL = """

                  """
# El "LIKE" reconoce patrones para seleccionar varias columnas a la vez. Utiliza siempre un "%" y lurgo un codigo  para indicar el patron a respetar.  
    imprimirEjercicio(consigna, [examen], consultaSQL)


    print("# =============================================================================")
    print("# Ejercicios SQL - Eligiendo")
    print("# =============================================================================")

    consigna    = """a1.- Listar a cada alumno que rindió el Parcial-01 y decir si aprobó o no (se aprueba con nota >=4)."""
    
    consultaSQL = """
                     SELECT Nombre,Nota,Instancia,
                         CASE WHEN Nota>=4
                         THEN 'APROBÓ'
                         ELSE 'NO APROBÓ'
                         END AS Estado
                     FROM examen
                     WHERE Instancia='Parcial-01'
                     ORDER BY Nombre;
                  """

    imprimirEjercicio(consigna, [examen], consultaSQL)


    # -----------
    consigna    = """a2.- Modificar la consulta anterior para que informe cuántos estudiantes aprobaron/reprobaron en cada instancia."""
    
    consultaSQL = """
                     SELECT Instancia, 
                         CASE WHEN Nota>=4
                         THEN 'APROBÓ'
                         ELSE 'NO APROBÓ'
                         END AS Estado,
                         count(*) as Cantidad
                    FROM examen
                    GROUP BY Instancia, Estado
                    ORDER BY Instancia, Estado;
                  """

    imprimirEjercicio(consigna, [examen], consultaSQL)


    print("# =============================================================================")
    print("# Ejercicios SQL - Subqueries")
    print("# =============================================================================")

    consigna    = """a.- Listar los alumnos que en cada instancia obtuvieron una nota mayor al promedio de dicha instancia"""
    
    consultaSQL = """

                  """


    imprimirEjercicio(consigna, [examen], consultaSQL)


    # -----------
    consigna    = """b.- Listar los alumnos que en cada instancia obtuvieron la mayor nota de dicha instancia"""
    
    consultaSQL = """

                  """

    imprimirEjercicio(consigna, [examen], consultaSQL)


    # -----------
    consigna    = """c.- Listar el nombre, instancia y nota sólo de los estudiantes que no rindieron ningún Recuperatorio"""
    
    consultaSQL = """

                  """

    imprimirEjercicio(consigna, [examen], consultaSQL)


    print("# =============================================================================")
    print("# Ejercicios SQL - Integrando variables de Python")
    print("# =============================================================================")

    consigna    = """a.- Mostrar Nombre, Instancia y Nota de los alumnos cuya Nota supera el umbral indicado en la variable de Python umbralNota"""
    
    umbralNota = 7
    
    consultaSQL = """

                  """

    print(sql^ consultaSQL)
    # imprimirEjercicio(consigna, [examen], consultaSQL)


    print("# =============================================================================")
    print("# Ejercicios SQL - Manejo de NULLs")
    print("# =============================================================================")

    consigna    = """a.- Listar todas las tuplas de Examen03 cuyas Notas son menores a 9"""
    
    consultaSQL = """

                  """


    imprimirEjercicio(consigna, [examen03], consultaSQL)


    # -----------
    consigna    = """b.- Listar todas las tuplas de Examen03 cuyas Notas son mayores o iguales a 9"""
    
    consultaSQL = """

                  """


    imprimirEjercicio(consigna, [examen03], consultaSQL)


    # -----------
    consigna    = """c.- Listar el UNION de todas las tuplas de Examen03 cuyas Notas son menores a 9 y las que son mayores o iguales a 9"""
    
    consultaSQL = """

                  """


    imprimirEjercicio(consigna, [examen03], consultaSQL)


    # -----------
    consigna    = """d1.- Obtener el promedio de notas"""
    
    consultaSQL = """

                  """


    imprimirEjercicio(consigna, [examen03], consultaSQL)


    # -----------
    consigna    = """d2.- Obtener el promedio de notas (tomando a NULL==0)"""
    
    consultaSQL = """

                  """


    imprimirEjercicio(consigna, [examen03], consultaSQL)

    print("# =============================================================================")
    print("# Ejercicios SQL - Desafío")
    print("# =============================================================================")

    consigna    = """a.- Mostrar para cada estudiante las siguientes columnas con sus datos: Nombre, Sexo, Edad, Nota-Parcial-01, Nota-Parcial-02, Recuperatorio-01 y , Recuperatorio-02"""
    
    # ... Paso 1: Obtenemos los datos de los estudiantes
    consultaSQL = """

                  """

    datosEstudiantes = sql^ consultaSQL
    
    # ... Paso 2: Agregamos las notas del Parcial-01
    consultaSQL = """

                  """

    datosHastaParcial01 = sql^ consultaSQL

    # ... Paso 3: Agregamos las notas del Parcial-02
    consultaSQL = """

                  """

    datosHastaParcial02 = sql^ consultaSQL

    # ... Paso 4: Agregamos las notas del Recuperatorio-01
    consultaSQL = """

                  """

    datosHastaRecuperatorio01 = sql^ consultaSQL

    # ... Paso 5: Agregamos las notas del Recuperatorio-02
    consultaSQL = """

                  """

    datosHastaRecuperatorio02 = sql^ consultaSQL

    desafio_01 = datosHastaRecuperatorio02

    imprimirEjercicio(consigna, [examen], consultaSQL)


    # -----------
    consigna    = """b.- Agrega al ejercicio anterior la columna Estado, que informa si el alumno aprobó la cursada (APROBÓ/NO APROBÓ). Se aprueba con 4."""
    
    consultaSQL = """

                  """

    desafio_02 = sql^ consultaSQL
    
    imprimirEjercicio(consigna, [examen], consultaSQL)

#%%
# =============================================================================
# FUNCIONES PARA LA GENERACIÓN DE DATAFRAMES 
# =============================================================================
def get_empleado():
    # Genera el dataframe "empleado" que contiene las siguientes columnas 
    # (en el orden mencionado):
        # 1. DNI
        # 2. Nombre
        # 3. Sexo
        # 4. Salaro
        
    # ... Creamos el dataframe vacío (sólo con los nombres de sus columnas)
    empleado = pd.DataFrame(columns = ['DNI', 'Nombre', 'Sexo', 'Salario'])
    # ... Agregamos cada una de las filas al dataFrame
    empleado = pd.concat([empleado,pd.DataFrame([
        {'DNI' : 20222333, 'Nombre' : 'Diego' , 'Sexo' : 'M', 'Salario' : 20000.0},
        {'DNI' : 33456234, 'Nombre' : 'Laura' , 'Sexo' : 'F', 'Salario' : 25000.0},
        {'DNI' : 45432345, 'Nombre' : 'Marina', 'Sexo' : 'F', 'Salario' : 10000.0}
                                                ])
                        ])
    return empleado


def get_alumnosBD():
    # Genera el dataframe "alumnosBD" que contiene las siguientes columnas 
    # (en el orden mencionado):
        # 1. ID
        # 2. Nombre
        
    # ... Creamos el dataframe vacío (sólo con los nombres de sus columnas)
    alumnosBD = pd.DataFrame(columns = ['ID', 'Nombre'])
    # ... Agregamos cada una de las filas al dataFrame
    alumnosBD = pd.concat([alumnosBD,pd.DataFrame([
        {'ID' : 1, 'Nombre' : 'Diego' },
        {'ID' : 2, 'Nombre' : 'Laura' },
        {'ID' : 3, 'Nombre' : 'Marina'}
                                                    ])
                        ])
    return alumnosBD


def get_alumnosTLeng():
    # Genera el dataframe alumnosTLeng que contiene las siguientes columnas 
    # (en el orden mencionado):
        # 1. ID
        # 2. Nombre
        
    # ... Creamos el dataframe vacío (sólo con los nombres de sus columnas)
    alumnosTLeng = pd.DataFrame(columns = ['ID', 'Nombre'])
    # ... Agregamos cada una de las filas al dataFrame
    alumnosTLeng = pd.concat([alumnosTLeng,pd.DataFrame([
        {'ID' : 2, 'Nombre' : 'Laura'    },
        {'ID' : 4, 'Nombre' : 'Alejandro'}
                                                        ])
                        ])
    return alumnosTLeng


def get_persona_ejemploCrossJoin():
    # Genera el dataframe "persona" que contiene las siguientes columnas 
    # (en el orden mencionado):
        # 1. Nombre
        # 2. Nacionalidad
        
    # ... Creamos el dataframe vacío (sólo con los nombres de sus columnas)
    persona = pd.DataFrame(columns = ['Nombre', 'Nacionalidad'])
    # ... Agregamos cada una de las filas al dataFrame
    persona = pd.concat([persona,pd.DataFrame([
        {'Nombre' : 'Diego'   , 'Nacionalidad' : 'AR'    },
        {'Nombre' : 'Laura'   , 'Nacionalidad' : 'BR'    },
        {'Nombre' : 'Marina'  , 'Nacionalidad' : 'AR'    }
                                              ])
                        ])
    return persona


def get_persona_ejemplosJoin():
    # Genera el dataframe "persona" que contiene las siguientes columnas 
    # (en el orden mencionado):
        # 1. Nombre
        # 2. Nacionalidad
        
    # ... Creamos el dataframe vacío (sólo con los nombres de sus columnas)
    persona = pd.DataFrame(columns = ['Nombre', 'Nacionalidad'])
    # ... Agregamos cada una de las filas al dataFrame
    persona = pd.concat([persona,pd.DataFrame([
        {'Nombre' : 'Diego'   , 'Nacionalidad' : 'BR'    },
        {'Nombre' : 'Laura'   , 'Nacionalidad' : None    },
        {'Nombre' : 'Marina'  , 'Nacionalidad' : 'AR'    },
        {'Nombre' : 'Santiago', 'Nacionalidad' : 'UY'    }
                                              ])
                        ])
    return persona


def get_se_inscribe_en_ejemploMismosNombres():
    # Genera el dataframe "se_inscribe_en" que contiene las siguientes columnas 
    # (en el orden mencionado):
        # 1. LU
        # 2. Codigo_materia
        
    # ... Creamos el dataframe vacío (sólo con los nombres de sus columnas)
    se_inscribe_en = pd.DataFrame(columns = ['LU','Codigo_materia'])
    # ... Agregamos cada una de las filas al dataFrame
    se_inscribe_en = pd.concat([se_inscribe_en,pd.DataFrame([
        {'LU':'123/09','Codigo_materia': 1},
        {'LU':' 22/10','Codigo_materia': 1},
        {'LU':' 22/10','Codigo_materia': 2},
        {'LU':'344/09','Codigo_materia': 1}
                                              ])
                        ])
    return se_inscribe_en

def get_materia_ejemploMismosNombres():
    # Genera el dataframe "materia" que contiene las siguientes columnas 
    # (en el orden mencionado):
        # 1. Codigo_materia
        # 2. Nombre
        
    # ... Creamos el dataframe vacío (sólo con los nombres de sus columnas)
    materia = pd.DataFrame(columns = ['Codigo_materia','Nombre'])
    # ... Agregamos cada una de las filas al dataFrame
    materia = pd.concat([materia,pd.DataFrame([
        {'Codigo_materia': 1, 'Nombre':'Laboratorio de Datos'   },
        {'Codigo_materia': 2, 'Nombre':'Análisis II'   },
        {'Codigo_materia': 3, 'Nombre':'Probabilidad'   }
                                              ])
                        ])
    return materia


def get_nacionalidades():
    # Genera el dataframe "nacionalidades" que contiene las siguientes columnas 
    # (en el orden mencionado):
        # 1. IDN (Id Nacionalidad)
        # 2. Detalle
    
    # ... Creamos el dataframe vacío (sólo con los nombres de sus columnas)
    nacionalidades = pd.DataFrame(columns = ['IDN', 'Detalle'])
    # ... Agregamos cada una de las filas al dataFrame
    nacionalidades = pd.concat([nacionalidades,pd.DataFrame([
        {'IDN' : 'AR', 'Detalle' : 'Agentina'},
        {'IDN' : 'BR', 'Detalle' : 'Brasilera'},
        {'IDN' : 'CH', 'Detalle' : 'Chilena'}
                                                          ])
                        ])
    return nacionalidades

# =============================================================================
# DEFINICION DE FUNCIÓN DE IMPRESIÓN EN PANTALLA
# =============================================================================
# Imprime en pantalla en un formato ordenado:
    # 1. Consigna
    # 2. Cada dataframe de la lista de dataframes de entrada
    # 3. Query
    # 4. Dataframe de salida
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


# =============================================================================
# EJECUCIÓN MAIN
# =============================================================================

if __name__ == "__main__":
    main()