num1 = input("Ingrese un numero: ")
num2 = input("Ingrese otro numero: ")

print(type(num1), type(num2))

num1 = int(num1)
num2 = int(num2)

print(type(num1), type(num2))

print("1",num1 == num2)
print("2",num1 != num2)
print("3",num1,"es mayor que", num2, num1 > num2)
print("4",num1 < num2)
print("5",num1 >= num2)
print("6",num1 <= num2)