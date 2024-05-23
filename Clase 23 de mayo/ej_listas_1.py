#Actividad: Creación de Listas con Datos Relacionados
#Instrucciones:
#1. Utiliza los siguientes datos para crear varias listas relacionadas.
#2. Luego, muestra algún dato específico de cada lista utilizando índices o métodos de acceso.
#Datos:
# Nombres de Frutas: "Manzana", "Banana", "Naranja", "Pera", "Uva"
# Precios de las Frutas: 2.50, 1.80, 1.20, 3.00, 2.75 (en dólares)
# Cantidades de Frutas Disponibles: 10, 15, 8, 12, 20 (en kilogramos)
#Actividad:
#1. Crea una lista llamada frutas que contenga los nombres de las frutas proporcionadas.
#2. Crea una lista llamada precios que contenga los precios de las frutas.
#3. Crea una lista llamada cantidades que contenga las cantidades de frutas disponibles.
#4. Muestra el tercer nombre de fruta de la lista frutas.
#5. Muestra el precio de la "Naranja".
#6. Muestra la cantidad disponible de "Pera".


# Crear la lista de nombres de frutas
frutas = ["Manzana", "Banana", "Naranja", "Pera", "Uva"]

# Crear la lista de precios de las frutas
precios = [2.50, 1.80, 1.20, 3.00, 2.75]

# Crear la lista de cantidades de frutas disponibles
cantidades = [10, 15, 8, 12, 20]

tercer_fruta = frutas[2]
print(f"El tercer nombre de fruta es: {tercer_fruta}")

precio_naranja = precios[2]
print(f"El precio de la Naranja es: ${precio_naranja:.2f}")

cantidad_pera = cantidades[3]
print(f"La cantidad disponible de Pera es: {cantidad_pera} kg")
