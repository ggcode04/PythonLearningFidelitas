'''
Universidad Fidelitas
Programacion Basica
Gabriel Granados Ureña
Semana #9
'''

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
a= int(input("Ingrese el primer número: "))
b= int(input("Ingrese el segundo número: "))

sumar(a, b)
restar(a, b)
multiplicar(a, b)
dividir(a, b)