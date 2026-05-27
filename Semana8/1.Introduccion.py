'''
Universidad Fidelitas
Programacion Basica
Gabriel Granados Ureña
Semana #8
'''

# Datos de entrada
A_Actual = 2026
Nombre = input("Ingrese su nombre: ") # Dato tipo string/texto

A_Nacimiento = int(input("Ingrese su año de nacimiento: ")) # Dato tipo entero/number/numerico

# Proceso de datos
Edad = A_Actual - A_Nacimiento

# Salida de datos
print("Hola " + Nombre + ", tu edad es: " + str(Edad) + " años.") # Dato tipo string/texto