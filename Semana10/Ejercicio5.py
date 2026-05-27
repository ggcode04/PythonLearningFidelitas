import array

numeros = array.array('i')

for i in range(10):
    valor = int(input("Ingrese el numero: #"))
    numeros.append(valor)

print("\nContenido del arreglo:")
for n in numeros:
    print(n)