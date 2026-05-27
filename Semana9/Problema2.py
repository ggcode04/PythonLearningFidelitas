'''
Universidad Fidelitas
Programacion Basica
Gabriel Granados Ureña
Semana #9 Problema 2
'''

# Confeccionar una funcion que reciba 4 valores enteros y nos muestre el mayor de ellos
def mayor_de_cuatro(num1, num2, num3, num4):
    mayor = num1
    if num2 > mayor:
        mayor = num2
    if num3 > mayor:
        mayor = num3
    if num4 > mayor:
        mayor = num4
    return mayor

# Solicitar al usuario que ingrese 4 números enteros
num1 = int(input("Ingrese el primer número entero: "))
num2 = int(input("Ingrese el segundo número entero: "))
num3 = int(input("Ingrese el tercer número entero: "))
num4 = int(input("Ingrese el cuarto número entero: "))

# Llamar a la función y mostrar el resultado
resultado = mayor_de_cuatro(num1, num2, num3, num4)
print("El mayor de los cuatro números es:", resultado)
