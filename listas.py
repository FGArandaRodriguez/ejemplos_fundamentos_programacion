# #Lista homogénea
# diasem=["Dom","Lun","Mar","Mie","Jue","Vie","Sab"]
# print(diasem)

# #Lista heterogénea
# datosgrales=["Guillermo",53,1.72,False] #Nombre, edad, Estatura, Soltero
# print(datosgrales)

# #Lista vacía
# vacia=[]
# print(vacia)

# #Lista con lista
# listalista=["Círculo",[2,-3],5] #Figura, Posición en el plano (x,y), radio
# print (listalista)

# #Diccionario
# {
#     "Figura": "Círculo",
#     "Posicion": [2,-3],
#     "Radio": 5,
#     "lista de figuras": ["Círculo", "Cuadrado", "Triángulo"]
#     "diccionario de alumnos": {
#         "Alumno 1": "Guillermo",
#         "Alumno 2": "Luis",
#         "Alumno 3": "Pedro
#     }
# },
#Lista
# x =[
#     "Círculo",
#     [2,-3],
#     5,
#     {
#         "Alumno 1": "Guillermo",
#         "Alumno 2": "Luis",
#         "Alumno 3": "Pedro"
#     },
# ]

# # print(x[3].get("Alumno 2"))

# # print(x[3]["Alumno 2"])

# buscando = "Luis"

# for i in x:
#     if type(i) == dict:
#         for key, value in i.items():
#             if value == buscando:
#                 print(f"Valor encontrado {value}, con llave {key}")
#     else:
#         print("No es un diccionario")
#     #print(i)


# #Lista original
# estaciones=["Primavera", "Otoño", "Berano", "Invierno"]
# print("Esta es la lista original:  ",estaciones)

# #Cambiar el elemento “Berano” por “Verano”
# estaciones[2]="Verano"
# print("Esta es la lista corregida: ",estaciones)

# Mencionar las estaciones en orden inverso
# estaciones=["Primavera", "Verano", "Otoño", "Invierno"]

# print(estaciones[-1])
# print(estaciones[-2])
# print(estaciones[-3])
# print(estaciones[-4])