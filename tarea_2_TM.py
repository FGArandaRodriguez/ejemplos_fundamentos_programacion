precio_menor = 30
precio_mayor = 45


descuentos = {
    "adulto mayor": 0.12,
    "profesor": 0.10,
    "estudiante": 0.10,
    "ninguno": 0.0
}

while True:
    try:
        n = int(input("¿Cuántos visitantes pagarán boleto? "))
        if n <= 0:
            print("Por favor, introduce un número positivo.")
            continue
        break
    except ValueError:
        print("Por favor, introduce un número entero o válido.")


total = 0

for i in range(n):
    print("\nVisitante", i+1)


    while True:
        # Debemos preguntar si es mayor de edad
        mayor = input("¿Es mayor de 18 años? (s/n): ").lower()

        if mayor not in ["s", "n"]:
            print("Por favor, introduce 's' o 'n'.")
            continue
        break

    if mayor == "s":
        precio = precio_mayor
    else:
        precio = precio_menor

    while True:
        # Debemos preguntar que tipo de visitante es
        print("Tipos: adulto mayor | profesor | estudiante | ninguno")
        tipo = input("Indica el tipo de visitante: ").lower()

        if tipo not in descuentos:
            print("Por favor, introduce un tipo de visitante valido.")
            continue
        break

    # Luego validamos el tipo de visitante
    if tipo not in descuentos:
        print("Tipo no válido, se tomará como 'ninguno'")
        tipo = "ninguno"

    # Calculamos descuento
    descuento = descuentos[tipo]
    precio_final = precio * (1 - descuento)

    print("Precio del boleto: $", precio_final)
    total += precio_final

print("\nTOTAL A PAGAR: $", total)