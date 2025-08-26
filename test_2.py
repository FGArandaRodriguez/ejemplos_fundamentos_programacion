#cual es el resultado de este fragmento de código?

# my_list = [1, 2]

# for v in range(2):
#     my_list.insert(-1, my_list[v])

# print(my_list)


#############################################

#cual es el resultado de este fragmento de código?

# def function_1(a):
#     return None

# def function_2(a):
#     return function_1(a) * function_1(a)


# print(function_2(2))
#####################################################

#cual es el resultado de este fragmento de código?
print(1 // 2)
#################################
#cual es el resultado de este fragmento de código?
# def func(a, b):
#     return b ** a

# print(func(b=2, 2))

#########################################

#Qué valor se le asigna a X?

# z = 0
# y = 10
# x = y < z and z > y or y < z and z < y

# print(x)

###################################

#cual es el resultado de este fragmento de código?

# my_list =  [x * x for x in range(5)]

# def fun(lst):
#     del lst[lst[2]]
#     return lst


# print(fun(my_list))

#################################

#cual es el resultado de este fragmento de código?
# x = 1
# y = 2
# x, y, z = x, x, y
# z, y, z = x, y, z

# print(x, y, z)

################################
#cual es el resultado de este fragmento de código?

# a = 1
# b = 0
# a = a ^ b
# b = a ^ b
# a = a ^ b

# print(a, b)

###################################
# #cual es el resultado de este fragmento de código?
# def fun(x):
#     if x % 2 == 0:
#         return 1
#     else:
#         return 2


# print(fun(fun(2)))

################################
#cual es el resultado de este fragmento de código? si se ingresa 3 y 2?
# x = int(input())
# y = int(input())
# x = x % y
# x = x % y
# y = y % x
# print(y)

################################

#cual es el resultado de este fragmento de código? 3 y 6

# y = input()
# x = input()
# print(x + y)


############################
#cual es el resultado de este fragmento de código?
# print("a", "b", "c", sep="sep")
#########################

#cual es el resultado de este fragmento de código?

# x = 1 // 5 + 1 / 5
# print(x)

#############################

#cual es el resultado de este fragmento de código? 2 y 4

# x = float(input())
# y = float(input())
# print(y ** (1 / x))

################################

#cual es el resultado de este fragmento de código?

# dct = {'one': 'two', 'three': 'one', 'two': 'three'}
# v = dct['three']

# for k in range(len(dct)):
#     v = dct[v]

# print(v)

# lst = [i for i in range(-1, -2)]

# print(lst)

#####################
#cual es el resultado de este fragmento de código?
# def fun(x, y):
#     if x == y:
#         return x
#     else:
#         return fun(x, y-1)


# print(fun(0, 3))
#####################

#Cuantos * se imprimiran? 

# i = 0
# while i < i + 2 :
#     i += 1
#     print("*")
# else:
#     print("*")

#####################

#cual es el resultado de este fragmento de código?

# dd = {"1": "0", "0": "1"}
# for x in dd.vals():
#     print(x, end="")


#################
#cual es el resultado de este fragmento de código?

# dct = {}
# dct['1'] = (1, 2)
# dct['2'] = (2, 1)

# for x in dct.keys():
#     print(dct[x][1], end="")

################

#cual es el resultado de este fragmento de código?

# def fun(inp=2, out=3):
#     return inp * out
# print(fun(out=2))

################


#cuantos "#" se imprimen?
# lst = [[x for x in range(3)] for y in range(3)]

# for r in range(3):
#     for c in range(3):
#         if lst[r][c] % 2 != 0:
#             print("#")


#####################


#Qe pasa si ingreso 0
# try:
#     value = input("Ingresa un valor: ")
#     print(int(value)/len(value))
# except ValueError:
#     print("Entrada incorrecta...")
# except ZeroDivisionError:
#     print("Entrada erronea...")
# except TypeError:
#     print("Entrada muy erronea...")
# except:
#     print("¡Buuu!")


#####################

#que pasa con este código? 

# try:
#     print(5/0)
#     break
# except:
#     print("Lo siento, algo salió mal...")
# except (ValueError, ZeroDivisionError):
#     print("Mala suerte...")

####
# foo = (1, 2, 3)
# foo.index(0)


##########
#que pasa con este código?
#print(¡Hola, Mundo!)








##############
# i = 1
# while i <= 5:

#     print(i)
#     i += 1
###############

# i = 10
# while i > 0:
#     print(i, end=" ")
#     i -= 2

###############
# i = 1
# while i <= 10:
#     print(i, end=" ")
#     i += 2
#################

# x = 1
# suma = 0
# while x <= 4:
#     print(x)
#     suma += x
#     x += 1
# print(suma)

#################
num = 123
invertido = 0
while num > 0:
    print(num)
    digit = num % 10
    invertido = invertido * 10 + digit
    num //= 10
print(invertido)

#####################
