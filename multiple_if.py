edad = 18
ingresos = 350000
def calcular_ingresos():
    if edad < 18:
        print("Eres menor de edad")
    elif 18 <= edad < 30 and ingresos > 30000:
        print("Eres joven y con buen ingreso")
    else:
        print("Pasas a otra categoría")


def if_anidado(usuario, activo):
    if usuario == "admin":
        if activo:
            print("El usuario es admin y esta activo")
        else:
            print("El usuario es admin pero no esta activo")
    else:
        print("El usuario no es admin")

if_anidado("admin", True)