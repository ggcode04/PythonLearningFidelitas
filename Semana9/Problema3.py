'''
Universidad Fidelitas
Programacion Basica
Gabriel Granados Ureña
Semana #9 Problema 3
'''

# Desarrollar un programa que permita ingresar un lado de un cuadrado. Luego preguntar si quiere calcular y mostrar su perimetro o su area.

def captura():
    lado = float(input("Ingrese el lado del cuadrado: "))
    return lado

def calcular_perimetro(lado):
    perimetro = 4 * lado
    return perimetro

def calcular_area(lado):
    area = lado ** 2
    return area

# Solicitar al usuario que ingrese el lado del cuadrado
lado = captura()

# Preguntar al usuario qué desea calcular
opcion = int(input("Seleccione lo que desea calcular: \n1. Perímetro\n2. Área\n"))

if opcion == 1:
    resultado = calcular_perimetro(lado)
    print("El perímetro del cuadrado es:", resultado)
elif opcion == 2:
    resultado = calcular_area(lado)
    print("El área del cuadrado es:", resultado)
else:
    print("Opción no válida")