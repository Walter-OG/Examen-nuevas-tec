def recibir_frutas():
    frutas = []
    n = int(input("Ingrese la cantidad de frutas que desea agregar al salpicón: "))
    for i in range(1, n + 1):
        fruta = {}
        fruta["id"] = i
        fruta["nombre"] = input(f"Ingrese el nombre de la fruta {i}: ")
        fruta["precio_unitario"] = float(input(f"Ingrese el precio unitario de la fruta {i}: "))
        fruta["cantidad"] = int(input(f"Ingrese la cantidad de la fruta {i}: "))
        frutas.append(fruta)
    return frutas

def costo_total_salpicon(frutas):
    costo_total = sum(fruta["precio_unitario"] * fruta["cantidad"] for fruta in frutas)
    return costo_total

def mostrar_frutas_ordenadas_por_costo(frutas):
    frutas_ordenadas = sorted(frutas, key=lambda x: x["precio_unitario"], reverse=True)
    print("Frutas ordenadas por costo (de mayor a menor):")
    for fruta in frutas_ordenadas:
        print(f"Nombre: {fruta['nombre']}, Precio unitario: {fruta['precio_unitario']}")

def fruta_mas_barata(frutas):
    fruta_barata = min(frutas, key=lambda x: x["precio_unitario"])
    return fruta_barata



frutas = recibir_frutas()


costo_total = costo_total_salpicon(frutas)
print("****************************************")
print(f"Costo total del salpicón: {costo_total}")


mostrar_frutas_ordenadas_por_costo(frutas)


fruta_barata = fruta_mas_barata(frutas)
print("****************************************")
print(f"La fruta más barata es: {fruta_barata['nombre']} con precio unitario de {fruta_barata['precio_unitario']}")
