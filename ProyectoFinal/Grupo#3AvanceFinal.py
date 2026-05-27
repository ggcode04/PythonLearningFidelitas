# =========================
# VARIABLES GLOBALES
# =========================

# Lista donde se almacenan todas las tutorías - Matriz unidimensional
tutorias = []

# Contador de tutorías
cantTutorias = 0


# =========================
# SUBPROGRAMA 1: LOGIN
# =========================

def login():
    # Variables de control de intentos
    intentos = 0
    mostrarIntentos = 3

    # Ciclo que permite hasta 3 intentos
    while intentos < 3:
        intentos = intentos + 1
        mostrarIntentos = mostrarIntentos - 1

        print("\n--- INICIO DE SESIÓN ---")
        correo = input("Correo: ")
        contrasena = input("Contraseña: ")

        # Validación para estudiante
        if correo == "estudiante@ufidelitas.ac.cr" and contrasena == "1234":
            print("✅ Bienvenido estudiante")
            menu_principal()
            return

        # Validación para administrador/tutor
        elif correo == "tutor@ufidelitas.ac.cr" and contrasena == "Tutor123":
            print("✅ Bienvenido tutor")
            modulo_administracion()
            return

        # Si los datos son incorrectos
        else:
            print("❌ Credenciales incorrectas")
            print("Le quedan", mostrarIntentos, "intentos")

        # Si llega al último intento
        if intentos == 3:
            print("⛔ Límite de intentos alcanzado")


# =========================
# SUBPROGRAMA 2: MENÚ PRINCIPAL
# =========================

def menu_principal():
    # Ciclo del menú
    while True:
        print("\n--- MENÚ PRINCIPAL ---")
        print("1. Reservar tutoría")
        print("2. Gestionar tutorías")
        print("3. Cerrar sesión")

        opcion = int(input("Seleccione: "))

        if opcion == 1:
            reservar_tutorias()
        elif opcion == 2:
            gestion_tutorias()
        elif opcion == 3:
            if cerrar_sesion():
                return
        else:
            print("❌ Opción inválida")


# =========================
# SUBPROGRAMA 3: RESERVAR
# =========================

def reservar_tutorias():
    global cantTutorias

    print("\n--- RESERVAR TUTORÍA ---")

    # Selección de materia
    print("1. Cálculo")
    print("2. Álgebra")
    print("3. Matemáticas Discretas")
    print("4. Probabilidades")

    menuMateria = int(input("Seleccione materia: "))

    # Asignación según opción
    if menuMateria == 1:
        materia = "Cálculo"
    elif menuMateria == 2:
        materia = "Álgebra"
    elif menuMateria == 3:
        materia = "Matemáticas Discretas"
    elif menuMateria == 4:
        materia = "Probabilidades"
    else:
        print("❌ Opción incorrecta")
        materia = "No definida"

    # Solicitud de datos
    tema = input("Tema: ")
    fecha = input("Fecha (dd/mm): ")
    hora = input("Hora (hh:mm): ")

    # Variable para validar si el horario está ocupado
    ocupado = False

    # Recorrer todas las tutorías existentes
    for t in tutorias:
        # Validar si coincide fecha y hora
        if t["fecha"] == fecha and t["hora"] == hora:
            ocupado = True

    # Si el horario NO está ocupado
    if ocupado == False:
        # Guardar tutoría en la lista
        tutorias.append({
            "materia": materia,
            "tema": tema,
            "fecha": fecha,
            "hora": hora
        })

        cantTutorias = cantTutorias + 1
        print("✅ Tutoría reservada correctamente")

    # Si está ocupado
    else:
        print("❌ Ese horario ya está ocupado")


# =========================
# SUBPROGRAMA 4: GESTIÓN
# =========================

def gestion_tutorias():
    global cantTutorias

    print("\n--- GESTIÓN DE TUTORÍAS ---")

    # Validar si hay tutorías
    if cantTutorias > 0:

        # Mostrar todas las tutorías con índice
        for i in range(len(tutorias)):
            t = tutorias[i]
            print(i, "-", t["materia"], "|", t["fecha"], "|", t["hora"])

        print("\n1. Cancelar tutoría")
        print("2. Confirmar asistencia")

        opcion = int(input("Seleccione: "))

        # Cancelar tutoría
        if opcion == 1:
            num = int(input("Número de tutoría: "))
            confirm = input("¿Confirmar cancelación? (S/N): ")

            if confirm == "S":
                if num < len(tutorias):
                    tutorias.pop(num)
                    cantTutorias = cantTutorias - 1
                    print("✅ Tutoría cancelada")
                else:
                    print("❌ Número inválido")
            else:
                print("No se canceló")

        # Confirmar asistencia
        elif opcion == 2:
            num = int(input("Número de tutoría: "))
            confirm = input("¿Confirmar asistencia? (S/N): ")

            if confirm == "S":
                print("✅ Asistencia confirmada")
            else:
                print("No se confirmó")

    else:
        print("No tienes tutorías registradas")


# =========================
# SUBPROGRAMA 5: ADMIN
# =========================

def modulo_administracion():
    global cantTutorias

    opcion = "S"

    print("\n--- MÓDULO ADMINISTRATIVO ---")

    # Ciclo controlado por el usuario
    while opcion == "S":

        print("\n1. Ver tutorías")
        print("2. Ver cantidad de estudiantes")
        print("3. Cancelar tutoría")
        print("4. Cerrar sesión")

        menu = int(input("Seleccione: "))

        # Ver todas las tutorías
        if menu == 1:
            # Validar si hay tutorías registradas
            if cantTutorias > 0:
                for t in tutorias:
                    print(t)
            else:
                print("No hay tutorías registradas en el sistema.")

        # Ver cantidad
        elif menu == 2:
            print("Cantidad de tutorías:", cantTutorias)

        # Cancelar tutoría
        elif menu == 3:
            if cantTutorias > 0:
                for i in range(len(tutorias)):
                    print(i, tutorias[i])

                num = int(input("Número a cancelar: "))
                confirm = input("¿Seguro? (S/N): ")

                if confirm == "S":
                    if num < len(tutorias):
                        tutorias.pop(num)
                        cantTutorias = cantTutorias - 1
                        print("Tutoría eliminada")
                    else:
                        print("Número inválido")
                else:
                    print("No se eliminó")
            else:
                print("No hay tutorías")

        # Cerrar sesión
        elif menu == 4:
            confirmar = input("¿Desea cerrar sesión? (S/N): ")

            if confirmar == "S":
                print("Sesión finalizada")
                opcion = "N"
            else:
                print("Regresando al menú administrativo...")


# =========================
# SUBPROGRAMA 6: CERRAR SESIÓN
# =========================

def cerrar_sesion():
    opcion = input("¿Desea cerrar sesión? (S/N): ")

    if opcion == "S":
        print("Sesión finalizada")
        return True
    else:
        return False


# =========================
# PROGRAMA PRINCIPAL
# =========================

login()