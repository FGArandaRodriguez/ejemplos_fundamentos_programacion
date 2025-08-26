def calcular_precio(tipo_visitante, es_menor, edad):
    precio_menor = 30
    precio_adulto = 45

    # Tabla de verdad de descuentos
    descuentos = {
        "adulto_mayor": 0.12,
        "profesor": 0.10,
        "estudiante": 0.10,
        "ninguno": 0.0
    }

    # Niños menores de 3 años no pagan
    if edad < 3:
        return 0

    # Determinar precio base
    precio_base = precio_menor if es_menor else precio_adulto

    # Aplicar descuento correspondiente
    descuento = descuentos.get(tipo_visitante, 0.0)
    precio_final = precio_base * (1 - descuento)

    return precio_final


def main():
    total = 0
    try:
        n = int(input("Ingrese el número de visitantes que pagarán boleto: "))
    except ValueError:
        print("Entrada no válida.")
        return

    for i in range(n):
        print(f"\n--- Visitante {i+1} ---")

        edad = int(input("Edad del visitante: "))
        
        if edad < 3:
            print("Este visitante no paga boleto (menor de 3 años).")
            continue  # Cláusula continue

        es_menor = True if edad < 18 else False

        print("Tipo de visitante:")
        print("1. Adulto mayor")
        print("2. Profesor")
        print("3. Estudiante")
        print("4. Ninguno")

        opcion = input("Seleccione el tipo (1-4, o 'x' para salir): ")

        if opcion.lower() == 'x':
            print("Se interrumpió el registro de visitantes.")
            break  # Cláusula break

        tipos = {
            "1": "adulto_mayor",
            "2": "profesor",
            "3": "estudiante",
            "4": "ninguno"
        }

        tipo_visitante = tipos.get(opcion, "ninguno")

        precio = calcular_precio(tipo_visitante, es_menor, edad)
        print(f"Precio a pagar para este visitante: ${precio:.2f}")
        total += precio

    print(f"\nTotal a pagar por todos los visitantes: ${total:.2f}")


if __name__ == "__main__":
    main()
