#Actividad Avanzada: Gestión Detallada del Inventario de Frutas Instrucciones:
#1. Utiliza los siguientes datos para crear varias listas relacionadas que representen el inventario detallado de frutas de una tienda.
#2. Luego, realiza varias operaciones sobre estas listas para gestionar el inventario y calcular métricas específicas. Datos:
# Nombres de Frutas: "Manzana", "Banana", "Naranja", "Pera", "Uva"
# Precios de las Frutas (en dólares por kilogramo): 2.50, 1.80, 1.20, 3.00, 2.75
# Cantidades de Frutas Disponibles (en kilogramos): 10, 15, 8, 12, 20
# Frutas Vendidas Hoy (en kilogramos): 3, 5, 2, 4, 6
# Precios de Compra de las Frutas (en dólares por kilogramo): 1.80, 1.20, 0.90, 2.50, 2.00 Actividad:
#1. Crea las listas nombres_frutas, precios_venta, cantidades_disponibles, frutas_vendidas y precios_compra con los datos proporcionados.
#2. Calcula y muestra el valor total del inventario actual de frutas (en dólares).
#3. Calcula y muestra el valor total de las frutas vendidas hoy (en dólares).
#4. Calcula y muestra el margen de beneficio total obtenido hoy (diferencia entre el valor total de ventas y el valor total de compra).
#5. Actualiza la lista de cantidades disponibles restando las frutas vendidas hoy.
#6. Muestra el nombre de la fruta que tiene el mayor margen de beneficio por kilogramo (diferencia entre precio de venta y precio de compra).
#7. Ordena las listas de frutas por precio de venta de forma descendente.
#8. Muestra las frutas que tienen un precio de venta mayor a 2.00 dólares por kilogramo.

#Datos
nombres_frutas = ["Manzana", "Banana", "Naranja", "Pera", "Uva"]
precios_venta = [2.50, 1.80, 1.20, 3.00, 2.75]
cantidades_disponibles = [10, 15, 8, 12, 20]
frutas_vendidas = [3, 5, 2, 4, 6]
precios_compra = [1.80, 1.20, 0.90, 2.50, 2.00]

#2. Calcular y mostrar el valor total del inventario actual de frutas (en dólares)
valor_inventario_actual = sum([cantidades_disponibles[i] * precios_venta[i] for i in range(len(nombres_frutas))])
print(f"El valor total del inventario actual de frutas es: ${valor_inventario_actual:.2f}")

#3. Calcular y mostrar el valor total de las frutas vendidas hoy (en dólares)
valor_frutas_vendidas_hoy = sum([frutas_vendidas[i] * precios_venta[i] for i in range(len(nombres_frutas))])
print(f"El valor total de las frutas vendidas hoy es: ${valor_frutas_vendidas_hoy:.2f}")

#4. Calcular y mostrar el margen de beneficio total obtenido hoy
costo_frutas_vendidas_hoy = sum([frutas_vendidas[i] * precios_compra[i] for i in range(len(nombres_frutas))])
margen_beneficio_hoy = valor_frutas_vendidas_hoy - costo_frutas_vendidas_hoy
print(f"El margen de beneficio total obtenido hoy es: ${margen_beneficio_hoy:.2f}")

#5. Actualizar la lista de cantidades disponibles restando las frutas vendidas hoy
cantidades_disponibles_actualizadas = [cantidades_disponibles[i] - frutas_vendidas[i] for i in range(len(nombres_frutas))]
print(f"Las cantidades disponibles actualizadas son: {cantidades_disponibles_actualizadas}")

#6. Mostrar el nombre de la fruta que tiene el mayor margen de beneficio por kilogramo
margenes_beneficio = [precios_venta[i] - precios_compra[i] for i in range(len(nombres_frutas))]
max_margen_beneficio = max(margenes_beneficio)
indice_max_margen = margenes_beneficio.index(max_margen_beneficio)
fruta_max_margen = nombres_frutas[indice_max_margen]
print(f"La fruta con mayor margen de beneficio por kilogramo es: {fruta_max_margen}")

#7. Ordenar las listas de frutas por precio de venta de forma descendente
frutas_ordenadas = sorted(zip(precios_venta, nombres_frutas, cantidades_disponibles_actualizadas, frutas_vendidas, precios_compra), reverse=True, key=lambda x: x[0])
precios_venta_ordenados, nombres_frutas_ordenados, cantidades_disponibles_ordenadas, frutas_vendidas_ordenadas, precios_compra_ordenados = zip(*frutas_ordenadas)

print(f"Frutas ordenadas por precio de venta (descendente): {list(nombres_frutas_ordenados)}")

#8. Mostrar las frutas que tienen un precio de venta mayor a 2.00 dólares por kilogramo
frutas_precio_mayor_2 = [nombres_frutas[i] for i in range(len(nombres_frutas)) if precios_venta[i] > 2.00]
print(f"Las frutas con un precio de venta mayor a 2.00 dólares por kilogramo son: {frutas_precio_mayor_2}")
