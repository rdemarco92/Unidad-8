#Ejercicio 1
with open("productos.txt", "w", encoding="utf-8") as arch:
    arch.write("Lapicera,120.5,30\n")
    arch.write("Cuaderno,450.0,15\n")
    arch.write("Regla,80.0,50\n")
print("Archivo productos.txt creado.")

#Ejercicio 2
with open("productos.txt", "r", encoding="utf-8") as arch:
    for linea in arch:
        nombre, precio, cantidad = linea.strip().split(",")
        print(f"Producto:{nombre} |Precio:${precio}|Cantidad:{cantidad}")

#Ejercicio 3
with open("productos.txt", "a", encoding="utf-8") as arch:
    nombre = input("Nombre del producto: ")
    precio = input("Precio: ")
    cantidad = input("Cantidad: ")
    arch.write(f"{nombre},{precio},{cantidad}\n")
print("Producto agregado.")

#Ejercicio 4
productos = []
with open("productos.txt", "r", encoding="utf-8") as arch:
    for linea in arch:
        nombre, precio, cantidad = linea.strip().split(",")
        productos.append({
            "nombre": nombre,
            "precio": float(precio),
            "cantidad": int(cantidad)
        })
print("Lista de diccionarios:")
print(productos)

#Ejercicio 5
productos = []
with open("productos.txt", "r", encoding="utf-8") as arch:
    for linea in arch:
        nombre, precio, cantidad = linea.strip().split(",")
        productos.append({
            "nombre": nombre,
            "precio": float(precio),
            "cantidad": int(cantidad)
        })

buscar = input("Producto a buscar: ").strip().lower()
encontrado = False
for p in productos:
    if p["nombre"].lower() == buscar:
        print(f"Nombre: {p['nombre']}, Precio: ${p['precio']}, Cantidad: {p['cantidad']}")
        encontrado = True
        break
if not encontrado:
    print("Producto no encontrado.")

#Ejercicio 6
with open("productos.txt", "w", encoding="utf-8") as arch:
    for p in productos:
        arch.write(f"{p['nombre']},{p['precio']},{p['cantidad']}\n")
print("Archivo actualizado.")

#FIN