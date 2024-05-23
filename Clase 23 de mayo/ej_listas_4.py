#Actividad: Gestión de Notas de Estudiantes
#Instrucciones:
#1. Utiliza los siguientes datos para representar las notas de los estudiantes en dos parciales y el final.
#2. Realiza varios cálculos sobre estas notas para obtener métricas específicas y clasificar a los estudiantes.
#Datos:
# Notas de los estudiantes en Parcial 1: 15, 18, 12, 20, 14, 16, 19, 13, 17, 11
# Notas de los estudiantes en Parcial 2: 14, 16, 17, 13, 15, 18, 12, 19, 20, 11
# Notas de los estudiantes en el Final: 18, 16, 15, 14, 17, 19, 12, 20, 13, 11
# Límite de aprobación: 12 (en cada examen)
#Actividad:
#1. Calcula y muestra el promedio de notas de cada estudiante en el Parcial 1.
#2. Calcula y muestra el promedio de notas de cada estudiante en el Parcial 2.
#3. Calcula y muestra el promedio de notas de cada estudiante en el Final.
#4. Identifica y muestra al estudiante con el mayor promedio general.
#5. Identifica y muestra al estudiante con el menor promedio general.
#6. Identifica y muestra al estudiante con el promedio general intermedio.
#7. Identifica y muestra a los estudiantes que desaprobaron al menos uno de los exámenes.
#8. Identifica y muestra a los estudiantes que se inscribieron en el primer llamado (aprobados en ambos parciales).
#9. Identifica y muestra a los estudiantes que se inscribieron en el segundo llamado (desaprobados en algún parcial).

#Datos
notas_parcial1 = [15, 18, 12, 20, 14, 16, 19, 13, 17, 11]
notas_parcial2 = [14, 16, 17, 13, 15, 18, 12, 19, 20, 11]
notas_final = [18, 16, 15, 14, 17, 19, 12, 20, 13, 11]
limite_aprobacion = 12

#1. Calcular y mostrar el promedio de notas de cada estudiante en el Parcial 1
promedio_parcial1 = sum(notas_parcial1) / len(notas_parcial1)
print(f"El promedio de notas del Parcial 1 es: {promedio_parcial1:.2f}")

#2. Calcular y mostrar el promedio de notas de cada estudiante en el Parcial 2
promedio_parcial2 = sum(notas_parcial2) / len(notas_parcial2)
print(f"El promedio de notas del Parcial 2 es: {promedio_parcial2:.2f}")

#3. Calcular y mostrar el promedio de notas de cada estudiante en el Final
promedio_final = sum(notas_final) / len(notas_final)
print(f"El promedio de notas del Final es: {promedio_final:.2f}")

#Calcular el promedio general de cada estudiante
promedios_generales = [(notas_parcial1[i] + notas_parcial2[i] + notas_final[i]) / 3 for i in range(len(notas_parcial1))]

#4. Identificar y mostrar al estudiante con el mayor promedio general
max_promedio = max(promedios_generales)
indice_max_promedio = promedios_generales.index(max_promedio)
print(f"El estudiante con el mayor promedio general es el estudiante {indice_max_promedio + 1} con un promedio de {max_promedio:.2f}")

#5. Identificar y mostrar al estudiante con el menor promedio general
min_promedio = min(promedios_generales)
indice_min_promedio = promedios_generales.index(min_promedio)
print(f"El estudiante con el menor promedio general es el estudiante {indice_min_promedio + 1} con un promedio de {min_promedio:.2f}")

#6. Identificar y mostrar al estudiante con el promedio general intermedio
promedios_ordenados = sorted(promedios_generales)
promedio_intermedio = promedios_ordenados[len(promedios_ordenados) // 2]
indice_promedio_intermedio = promedios_generales.index(promedio_intermedio)
print(f"El estudiante con el promedio general intermedio es el estudiante {indice_promedio_intermedio + 1} con un promedio de {promedio_intermedio:.2f}")

#7. Identificar y mostrar a los estudiantes que desaprobaron al menos uno de los exámenes
desaprobados = [i + 1 for i in range(len(notas_parcial1)) if notas_parcial1[i] < limite_aprobacion or notas_parcial2[i] < limite_aprobacion or notas_final[i] < limite_aprobacion]
print(f"Los estudiantes que desaprobaron al menos uno de los exámenes son: {desaprobados}")

#8. Identificar y mostrar a los estudiantes que se inscribieron en el primer llamado (aprobados en ambos parciales)
primer_llamado = [i + 1 for i in range(len(notas_parcial1)) if notas_parcial1[i] >= limite_aprobacion and notas_parcial2[i] >= limite_aprobacion]
print(f"Los estudiantes que se inscribieron en el primer llamado son: {primer_llamado}")

#9. Identificar y mostrar a los estudiantes que se inscribieron en el segundo llamado (desaprobados en algún parcial)
segundo_llamado = [i + 1 for i in range(len(notas_parcial1)) if notas_parcial1[i] < limite_aprobacion or notas_parcial2[i] < limite_aprobacion]
print(f"Los estudiantes que se inscribieron en el segundo llamado son: {segundo_llamado}")