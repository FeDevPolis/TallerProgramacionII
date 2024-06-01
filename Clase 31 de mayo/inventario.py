# Definir una lista para almacenar los productos
inventario = []

# Bucle para ingresar los productos
while True:
    # Pedir el nombre del producto
    nombre = input("Ingrese el nombre del producto (o 'salir' para terminar): ")
    if nombre.lower() == 'salir':
        break
    
    # Pedir la cantidad del producto
    try:
        cantidad = int(input(f"Ingrese la cantidad de {nombre}: "))
    except ValueError:
        print("Por favor, ingrese un número válido para la cantidad.")
        continue
    
    # Agregar el producto y su cantidad al inventario
    inventario.append((nombre, cantidad))

# Mostrar los productos y sus cantidades
print("\nInventario:")
for producto in inventario:
    print(f"Producto: {producto[0]}, Cantidad: {producto[1]}")

# Calcular y mostrar el total de productos en el inventario
total_productos = sum(producto[1] for producto in inventario)
print(f"\nTotal de productos en el inventario: {total_productos}")