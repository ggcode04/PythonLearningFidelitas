import array

numeros = array.array('i', [5, 10, 15, 20, 25, 30, 35, 40, 45, 50])

suma = 0 # Iniciar el acumulador

# Recorrer el arreglo y acumular valores
for n in numeros:
    suma = suma + n
    print(suma)

print("La suma total es:", suma)
print("El promedio es:", suma / len(numeros))