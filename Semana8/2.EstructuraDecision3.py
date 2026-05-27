'''
Universidad Fidelitas
Programacion Basica
Gabriel Granados Ureña
Semana #8
Estructura de decisión simple
'''

# Se le solicita el precio y luego se convierte en un entero
precio = input("Ingrese el precio del producto: ")
precio = int(precio)

# Se le solicita la cantidad y se utiliza la funcion en la misma linea para convertirlo en un entero
cantidad = int(input("Ingrese la cantidad del producto: "))
if cantidad >= 12:
    # Si la cantidad es al menos 12
    # se hace un rebajo del 20% al precio
    precio = precio * 0.8
# Se obtiene el valor total de la compra
total = precio * cantidad
# Se muestra el valor al usuario
print("El total a pagar es: " + str(total) + " colones.")