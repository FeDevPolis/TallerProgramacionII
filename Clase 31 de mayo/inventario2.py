inventario = {}

num_productos = int(input("Ingresa la cantidad de productos en el inventario a cargar: "))

for _ in range(num_productos):
    nombre = input("Ingresa el nombre del producto: ")
    cantidad = int(input(f"Ingresa la cantidad de {nombre}: "))
    inventario[nombre] = cantidad

print("\nInventario:")

total_productos = 0

for producto, cantidad in inventario.items():
    print(f"{producto}: {cantidad}")
    total_productos += cantidad

print("\nTotal de productos en el inventario: ", total_productos)