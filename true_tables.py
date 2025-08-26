# Se asignan los valores a las variables
verdadero=True
falso=False


# Se muestra la tabla de verdad
print("\n       Tabla de Verdad")
print("  A     B\t  and\t  or")
print("===============================")
print("True  True\t", verdadero and verdadero, "\t", verdadero or verdadero)
print("True  False\t", verdadero and falso, "\t", verdadero or falso)
print("False True\t", falso and verdadero, "\t", falso or verdadero)
print("False False\t", falso and falso, "\t", falso or falso)