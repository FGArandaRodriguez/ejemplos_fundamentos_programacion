#Programa que suma los primeros n números naturales

#Descripción del programa:
#   El programa solicita un número entero y realiza la suma de los primeros
#   números naturales hasta llegar al número que proporcionó el usuario
#   EJEM: si el usuario proporciona el número 5 el resultado deberá ser:
#   15 ya que 1 + 2 + 3 + 4 + 5 = 15, si el usuario indica 9 entonces
#   el resultado deberá ser 45 ya que 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 = 45.

import pdb; pdb.set_trace()

#Se definen las variables
total=0

#Se solicita el número tope
numero=int(input("Dame el número: "))

#Ciclo principal del programa
for i in range(numero):
    total+=i
    print(total)