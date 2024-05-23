#Actividad: Gestión de Inventario de Frutas Instrucciones:
#1. Utiliza los siguientes datos para crear varias listas relacionadas que representen el inventario de frutas de una tienda.
#2. Luego, muestra diferentes datos específicos de las listas utilizando índices o métodos de acceso. Datos:
# Nombres de Frutas: "Manzana", "Banana", "Naranja", "Pera", "Uva"
# Precios de las Frutas: 2.50, 1.80, 1.20, 3.00, 2.75 (en dólares)
# Cantidades de Frutas Disponibles: 10, 15, 8, 12, 20 (en kilogramos)
# Frutas Vendidas Hoy: 3, 5, 2, 4, 6 (en kilogramos)
# Precios de Compra de las Frutas: 1.80, 1.20, 0.90, 2.50, 2.00 (en dólares por kilogramo) Actividad:
#1. Crea una lista llamada nombres_frutas que contenga los nombres de las frutas proporcionadas.
#2. Crea una lista llamada precios_venta que contenga los precios de venta de las frutas.
#3. Crea una lista llamada cantidades_disponibles que contenga las cantidades de frutas disponibles en el inventario.
#4. Crea una lista llamada frutas_vendidas que contenga las cantidades de frutas vendidas hoy.
#5. Crea una lista llamada precios_compra que contenga los precios de compra de las frutas.
#6. Muestra el nombre de la fruta que tiene la mayor cantidad disponible en el inventario.
#7. Muestra el precio de venta de la "Banana".
#8. Muestra la cantidad de "Naranjas" vendidas hoy.
#9. Calcula y muestra el total de ingresos de la tienda por la venta de frutas hoy.

#Datos 
nombres_frutas = ["Manzana", "Banana", "Naranja", "Pera", "Uva"]
precios_venta = [2.50, 1.80, 1.20, 3.00, 2.75]
cantidades_disponibles = [10, 15, 8, 12, 20]
frutas_vendidas = [3, 5, 2, 4, 6]
precios_compra = [1.80, 1.20, 0.90, 2.50, 2.00]

#Mostrar el nombre de la fruta con la mayor cantidad disponible en el inventario
max_cantidad = max(cantidades_disponibles)
indice_max_cantidad = cantidades_disponibles.index(max_cantidad)
fruta_max_cantidad = nombres_frutas[indice_max_cantidad]
print(f"La fruta con mayor cantidad disponible es: {fruta_max_cantidad}")

#Mostrar el precio de venta de la "Banana"
indice_banana = nombres_frutas.index("Banana")
precio_banana = precios_venta[indice_banana]
print(f"El precio de venta de la Banana es: ${precio_banana:.2f}")

#Mostrar la cantidad de "Naranjas" vendidas hoy
indice_naranja = nombres_frutas.index("Naranja")
cantidad_naranjas_vendidas = frutas_vendidas[indice_naranja]
print(f"La cantidad de Naranjas vendidas hoy es: {cantidad_naranjas_vendidas} kg")

#Calcular y mostrar el total de ingresos por la venta de frutas hoy
ingresos_totales = sum([frutas_vendidas[i] * precios_venta[i] for i in range(len(nombres_frutas))])
print(f"El total de ingresos por la venta de frutas hoy es: ${ingresos_totales:.2f}")
