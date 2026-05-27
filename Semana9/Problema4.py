'''
Universidad Fidelitas
Programacion Basica
Gabriel Granados Ureña
Semana #9 Problema 4
'''

# Elaborar una solución con funcion que reciba 4 enteros y nos retorne el valor promedio de ellos.
def calcular_promedio(num1, num2, num3, num4):
    promedio = (num1 + num2 + num3 + num4) / 4
    return promedio

# Solicitar al usuario que ingrese 4 números enteros
num1 = int(input("Ingrese el primer número entero: "))
num2 = int(input("Ingrese el segundo número entero: ")) 
num3 = int(input("Ingrese el tercer número entero: "))
num4 = int(input("Ingrese el cuarto número entero: "))

# Llamar a la función y mostrar el resultado
resultado = calcular_promedio(num1, num2, num3, num4)
print("El promedio de los cuatro números es:", resultado)