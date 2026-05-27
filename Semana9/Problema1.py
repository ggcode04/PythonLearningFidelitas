'''
Universidad Fidelitas
Programacion Basica
Gabriel Granados Ureña
Semana #9 Problema 1
'''

# Modifique el programa realizado en clases, para que las operaciones basicas, se llamen en un menu a partir de las funciones creadas.

def sumar (x, y):
    print("Ingreso a la opcion de suma")
    resultado = x + y
    print("La suma es: ", resultado)

def restar (x, y):
    print("Ingreso a la opcion de resta")
    resultado = x - y
    print("La resta es: ", resultado)

def multiplicar (x, y):
    print("Ingreso a la opcion de multiplicacion")
    resultado = x * y
    print("La multiplicacion es: ", resultado)

def dividir (x, y):
    print("Ingreso a la opcion de division")
    resultado = x / y
    print("La division es: ", resultado)

# main
seleccion = int(input("Seleccione la operación a realizar: \n1. Suma\n2. Resta\n3. Multiplicación\n4. División\n"))

if seleccion == 1:
    a= int(input("Ingrese el primer número: "))
    b= int(input("Ingrese el segundo número: "))
    sumar(a, b)
elif seleccion == 2:
    a= int(input("Ingrese el primer número: "))
    b= int(input("Ingrese el segundo número: "))
    restar(a, b)
elif seleccion == 3:
    a= int(input("Ingrese el primer número: "))
    b= int(input("Ingrese el segundo número: "))
    multiplicar(a, b)
elif seleccion == 4:
    a= int(input("Ingrese el primer número: "))
    b= int(input("Ingrese el segundo número: "))
    dividir(a, b)
else:
    print("Opción no válida")