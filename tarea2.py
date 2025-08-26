# # Se inicializan las variables
# terminacion1=terminacion2=terminacion9=terminacion0=terminacionplaca=0

# while terminacionplaca>=0:
#     terminacionplaca=int(input("En qué termina la placa (negativo para terminar) "))
#     if terminacionplaca==1:
#         terminacion1=terminacion1+1
#     elif terminacionplaca==2:
#         terminacion2=terminacion2+1
#     elif terminacionplaca==9:
#         terminacion9=terminacion9+1
#     elif terminacionplaca==0:
#         terminacion0=terminacion0+1
#     elif terminacionplaca < 0:
#         break
#     else:
#         print("Placa no reconocida")

# print("Total de terminación en 1: ",terminacion1)
# print("Total de terminación en 2: ",terminacion2)
# print("Total de terminación en 9: ",terminacion9)
# print("Total de terminación en 0: ",terminacion0)


import random

numtiro=1

while True:
    numdado=random.randint(1,6)
    print("Tiro ", numtiro, ": ", numdado)
    if numdado==6:
        print("Juego terminado")
        break
    else:
        numtiro+=1