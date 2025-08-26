# # # numerofavorito=[["Juan",5],["Mary",2],["Pepe",17]]

# # # print(numerofavorito)


# # artistas=[["Nombre real", "Nombre artístico"],
# # ["María Guadalupe Araujo Yong", "Ana Gabriel"],
# # ["Alberto Aguilera Valadez", "Juan Gabriel"],
# # ["Hassan Emilio Kabande Laija", "Peso Pluma"],
# # ["Juan Luis Londoño Arias", "Maluma"],
# # ["Elmer Figueroa Arce", "Chayanne"],
# # ["Adele Laurie Blue Adkins", "Adele"],
# # ["Carolina Giraldo Navarro", "Karol G"],
# # ["Rosalía Vila Tobella", ""]]
# # print(artistas)


# #Programa "Crear matriz con ciclo for"
# # matriz = []

# # for i in range(6):
# #     print("primera dimensión", i)
# #     matriz.append([])

# #     for j in range(2):
# #         print("segunda dimensión", j)
# #         print("matriz[i]",matriz[i])
# #         matriz[i].append(7)

# # print (matriz)



# matriz = []
# for i in range(3):
#     print("primera dimensión", i)
#     matriz.append([])

#     for j in range(3):
#         print("segunda dimensión", j)
#         print("matriz[i]",matriz[i])
#         matriz[i].append(7)

# print (matriz)

# matriz = [["Dato" for col in range(2)] for ren in range(6)]
# print(matriz)

# matriz = [[69 for col in range(1800)] for ren in range(5000)]
# print(matriz)




#Programa "Mostrar Paquetes de cómputo"
# paquetes=[["start","standart","pro","premium"],
# ["10 GB","20 GB","30 GB","50 GB"],
# ["1 User","3 Users","7 Users","10 Users"],
# ["5 Email","10 Email","15 Email","20 Email"],
# ["","Free update","Free update","Free update"],
# ["","","24/7 Support""24/7 Support"]]

# #Se muestra la multilista usando ciclo for
# for i in range(1):
#     print(paquetes[i])




#Programa operaciones mutables en multilistas

colores=[["Rojo",3],["Azul",2],["Gris",6],["Rojo",3],["Amarillo",0]]
print("Lista original: ",colores)
del colores[2]
print("Lista eliminando la posición 2: ",colores)
colores.append("Gris")
print("Lista anexando el color Gris: ",colores)
colores.insert(1,"Blanco")
print("Lista intercalando el color Blanco: ",colores)
colores.remove(["Rojo",3])
print("Lista quitando la primera aparición de Rojo: ",colores)
colores.reverse()
print("Lista con orden invertido: ",colores)