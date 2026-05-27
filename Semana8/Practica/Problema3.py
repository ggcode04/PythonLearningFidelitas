print("Escribe una solución para imprimir la tabla de multiplicar, (del 0 al 12), de cualquier numero (X) dado por el usuario.")

# print("For tabla de multiplicar")
# number = int(input("Ingrese el número para la tabla de multiplicar: "))
# for i in range(0, 13):
#     print(f"{number} x {i} = {number * i}")

print("While tabla de multiplicar")
number = int(input("Ingrese el número para la tabla de multiplicar: "))
i = 0
while i <= 12:
    print(f"{number} x {i} = {number * i}")
    i = i + 1