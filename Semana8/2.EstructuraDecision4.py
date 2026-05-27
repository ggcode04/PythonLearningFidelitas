'''
Universidad Fidelitas
Programacion Basica
Gabriel Granados Ureña
Semana #8
Estructura de decisión doble
'''

# Se le solicita la nota
nota = int(input("Ingrese la nota del estudiante: "))
if nota >= 60:
    # Si la nota es al menos 60, se muestra un mensaje de aprobación
    print("¡Felicidades! Has aprobado el curso.")
else:
    # Si la nota es menor a 60, se muestra un mensaje de reprobación
    print("Lo siento, has reprobado el curso. ¡Sigue esforzándote!")
print("Fin del programa")