##Demostración de paso de argumentos

x = 1
y = 2


def sumar ():
    print("Dame el valor de x:")
    x= float(input())
    print("Dame el valor de y:")
    y= float(input())
    print("El resultado de la suma es: ",x+y)

sumar()


def saludar(nombre: str,edad: int):
    
    print("Hola", nombre, "tienes", edad, "años")

#saludar("Giovanni", 27)