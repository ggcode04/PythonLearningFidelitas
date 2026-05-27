def sumar (x, y):
    resultado = x + y
    return resultado

def restar (x, y):
    return x - y

def multiplicar (x, y):
    resultado = x * y
    return resultado

def dividir (x, y):
    resultado = x / y
    return resultado

a = int(input("Ingrese el primer número: "))
b = int(input("Ingrese el segundo número: "))
resultado = sumar(a, b)
print(f"La suma de {a} y {b} es: {resultado}")
print(f"La resta de {a} y {b} es: {restar(a, b)}")
print(f"La multiplicación de {a} y {b} es: {multiplicar(a, b)}")
print(f"La división de {a} y {b} es: {dividir(a, b)}")
