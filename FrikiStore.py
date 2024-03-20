import random 

productos = []

def generar_id():
    return random.randint(1, 100)

def registrar_producto():
    producto = {}
    producto["id"] = generar_id()
    producto["nombre"] = input("Nombre del producto: ")
    producto["precio"] = float(input("Precio unitario del producto: "))
    producto["ubicacion"] = input("Ubicación en la tienda (A, B, C, D): ").upper()
    producto["descripcion"] = input("Descripción del producto: ")
    producto["casa"] = input("Casa a la que pertenece el producto (Marvel, DC): ")
    producto["referencia"] = input("Referencia (código alfanumérico): ")
    producto["pais_origen"] = input("País de origen del producto: ")
    producto["unidades_compradas"] = int(input("Número de unidades compradas del producto: "))
    producto["garantia_extendida"] = input("Producto con garantía extendida (true/false): ").lower() == "true"
    productos.append(producto)
    print("Producto registrado con éxito.")

def mostrar_productos_bodega():
    print("Productos en bodega:")
    for producto in productos:
        print(producto)

def buscar_producto_por_nombre():
    nombre = input("Ingrese el nombre del producto: ")
    for producto in productos:
        if producto["nombre"] == nombre:
            print("ID:", producto["id"])
            print("Nombre:", producto["nombre"])
            print("Precio unitario:", producto["precio"])
            print("Descripción:", producto["descripcion"])
            break
    else:
        print("Producto no encontrado.")

def modificar_unidades_compradas():
    nombre = input("Ingrese el nombre del producto: ")
    for producto in productos:
        if producto["nombre"] == nombre:
            nuevas_unidades = int(input("Ingrese el nuevo número de unidades compradas: "))
            if nuevas_unidades <= producto["unidades_compradas"]:
                producto["unidades_compradas"] = nuevas_unidades
                print("Número de unidades compradas actualizado.")
            else:
                print("Error: La modificación no puede ser mayor al número inicial.")
            break
    else:
        print("Producto no encontrado.")

def eliminar_producto():
    nombre = input("Ingrese el nombre del producto que desea eliminar: ")
    for producto in productos:
        if producto["nombre"] == nombre:
            confirmacion = input(f"¿Está seguro que desea eliminar el producto '{nombre}'? (Sí/No): ").lower()
            if confirmacion == "si":
                productos.remove(producto)
                print("Producto eliminado.")
            break
    else:
        print("Producto no encontrado.")


while True:
    print("\nMENU")
    print("1. Registrar producto")
    print("2. Mostrar productos en bodega")
    print("3. Buscar producto por nombre")
    print("4. Modificar número de unidades compradas")
    print("5. Eliminar producto")
    print("6. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        registrar_producto()
    elif opcion == "2":
        mostrar_productos_bodega()
    elif opcion == "3":
        buscar_producto_por_nombre()
    elif opcion == "4":
        modificar_unidades_compradas()
    elif opcion == "5":
        eliminar_producto()
    elif opcion == "6":
        print("Saliendo del programa.")
        break
    else:
        print("Opción inválida. Por favor, seleccione una opción válida.")
