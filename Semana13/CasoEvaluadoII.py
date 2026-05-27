##################################
# Gabriel Esteban Granados Ureña #
#     Universidad Fidélitas      #
#  Caso Evaluado II - Semana 13  #
##################################

# ==================================================================================== #
#       Sistema de registro de préstamos de películas en una tienda de alquiler        #
#                               Videoclub Films S.A.                                   #
# ==================================================================================== #

# VARIABLES GLOBALES
# Matriz de películas: cada elemento es [código, nombre, año]
pelicula = []

# Matriz de préstamos: cada elemento es [id_cliente, código_película, fecha_devolución, estado]
prestamo = []

# CONSTANTES DEL SISTEMA
# ============================================================================
COSTO_PELICULA = 1500      # Costo de alquiler por película en colones
MULTA_ATRASO = 1000        # Multa por atraso en colones
USUARIO_ADMIN = "Admin"    # Usuario de administrador
CLAVE_ADMIN = "123"        # Clave de administrador

# ============================================================================
# FUNCIÓN: AUTENTICACIÓN
# ============================================================================
def autenticacion():
    """
    Valida el acceso del administrador al sistema.
    Permite 3 intentos para ingresar usuario y contraseña correctos.
    Retorna True si es exitosa, False si falla.
    """
    intentos = 3
    
    while intentos > 0:
        # Mostrar pantalla de bienvenida
        print("\n" + "="*50)
        print("BIENVENIDO AL SISTEMA DE VIDEOCLUB FILMS S.A.")
        print("="*50)
        
        # Solicitar credenciales
        usuario = input("Ingrese el usuario: ")
        clave = input("Ingrese la clave: ")
        
        # Validar credenciales
        
        if usuario == USUARIO_ADMIN and clave == CLAVE_ADMIN:
            print("\n¡Autenticación exitosa!")
            return True
        else:
            # Disminuir intentos
            intentos = intentos - 1
            if intentos > 0:
                print(f"\nDatos incorrectos. Intente nuevamente. ({intentos} intentos restantes)")
            else:
                print("\nAcceso denegado. Demasiados intentos fallidos.")
    
    return False

# ============================================================================
# FUNCIÓN: AGREGAR PELÍCULA
# ============================================================================
def agregar_pelicula():
    """
    Permite agregar una nueva película al sistema.
    Solicita código, nombre y año de la película.
    Guarda la información en la matriz de películas.
    Retorna al menú principal después de completar.
    """
    print("\n" + "="*50)
    print("AGREGAR PELÍCULA")
    print("="*50)
    
    # Solicitar datos de la película
    codigo = input("Ingrese el código de la película: ")
    nombre = input("Ingrese el nombre de la película: ")
    anio = input("Ingrese el año de la película: ")
    
    # Crear registro de película [código, nombre, año]
    nueva_pelicula = [codigo, nombre, anio]
    
    # Agregar a la matriz de películas
    pelicula.append(nueva_pelicula)
    
    # Confirmar agregación
    print("\n¡Película agregada correctamente!")
    input("Presione Enter para continuar...")

# ============================================================================
# FUNCIÓN: REGISTRAR PRÉSTAMO
# ============================================================================
def registrar_prestamo():
    """
    Registra un préstamo de película para un cliente.
    Permite registrar múltiples películas en un mismo préstamo.
    Calcula el monto total a pagar (1500 colones por película).
    Retorna al menú principal después de completar.
    """
    print("\n" + "="*50)
    print("REGISTRAR PRÉSTAMO")
    print("="*50)
    
    # Solicitar identificación del cliente
    id_cliente = input("Ingrese la identificación del cliente: ")
    monto_total = 0
    
    # Permitir registrar múltiples películas
    continuar = "si"
    while continuar.lower() == "si":
        # Solicitar datos del préstamo
        codigo_pelicula = input("Ingrese el código de la película a prestar: ")
        fecha_devolucion = input("Ingrese la fecha de devolución (ej: 25/04/2026): ")
        
        # Crear registro de préstamo [id_cliente, código_película, fecha_devolución, estado]
        nuevo_prestamo = [id_cliente, codigo_pelicula, fecha_devolucion, "PRESTAMO"]
        
        # Agregar a la matriz de préstamos
        prestamo.append(nuevo_prestamo)
        
        # Aumentar el monto total
        monto_total = monto_total + COSTO_PELICULA
        
        # Informar costo
        print(f"Película registrada. Costo: {COSTO_PELICULA} colones")
        
        # Preguntar si desea alquilar otra película
        continuar = input("\n¿Desea alquilar otra película? (si/no): ")
    
    # Mostrar monto total a pagar
    print("\n" + "-"*50)
    print(f"MONTO TOTAL A PAGAR: {monto_total} colones")
    print("-"*50)
    
    input("Presione Enter para continuar...")

# ============================================================================
# FUNCIÓN: REGISTRAR DEVOLUCIÓN
# ============================================================================
def registrar_devolucion():
    """
    Registra la devolución de películas de un cliente.
    Verifica si hay atraso y aplica multa de 1000 colones por película.
    Actualiza el estado de los préstamos a "DEVUELTO".
    Retorna al menú principal después de completar.
    """
    print("\n" + "="*50)
    print("REGISTRAR DEVOLUCIÓN")
    print("="*50)
    
    # Solicitar datos de devolución
    id_cliente = input("Ingrese la identificación del cliente: ")
    fecha_actual = input("Ingrese la fecha actual de devolución (ej: 25/04/2026): ")
    
    # Variables para contar películas y calcular multas
    prestamos_cliente = 0
    multa_total = 0
    
    # Recorrer la matriz de préstamos para buscar los del cliente
    for i in range(len(prestamo)):
        # Verificar si el préstamo es del cliente y aún está activo
        if prestamo[i][0] == id_cliente and prestamo[i][3] == "PRESTAMO":
            prestamos_cliente = prestamos_cliente + 1
            
            # Obtener la fecha programada de devolución
            fecha_programada = prestamo[i][2]
            
            # Extraer componentes de la fecha programada (formato DD/MM/YYYY)
            dia_prog = int(fecha_programada.split("/")[0])
            mes_prog = int(fecha_programada.split("/")[1])
            anio_prog = int(fecha_programada.split("/")[2])
            
            # Extraer componentes de la fecha actual (formato DD/MM/YYYY)
            dia_actual = int(fecha_actual.split("/")[0])
            mes_actual = int(fecha_actual.split("/")[1])
            anio_actual = int(fecha_actual.split("/")[2])
            
            # Convertir fechas a números para comparación
            fecha_prog_numero = anio_prog * 10000 + mes_prog * 100 + dia_prog
            fecha_actual_numero = anio_actual * 10000 + mes_actual * 100 + dia_actual
            
            # Comparar fechas
            if fecha_actual_numero > fecha_prog_numero:
                # Hay atraso, aplicar multa
                multa_total = multa_total + MULTA_ATRASO
                print(f"Película {prestamo[i][1]}: ¡ATRASO! Multa de {MULTA_ATRASO} colones")
            else:
                # Devolución a tiempo
                print(f"Película {prestamo[i][1]}: Devuelto a tiempo")
            
            # Actualizar estado del préstamo
            prestamo[i][3] = "DEVUELTO"
    
    # Mostrar resumen de la devolución
    if prestamos_cliente == 0:
        print(f"\nNo hay préstamos activos para el cliente {id_cliente}")
    else:
        print("\n" + "-"*50)
        print(f"Total de películas devueltas: {prestamos_cliente}")
        if multa_total > 0:
            print(f"Multa por atraso: {multa_total} colones")
        print("-"*50)
    
    input("Presione Enter para continuar...")

# ============================================================================
# FUNCIÓN: MENÚ PRINCIPAL
# ============================================================================
def menu_principal():
    """
    Muestra el menú principal del sistema.
    Gestiona las opciones disponibles para el administrador.
    Repite hasta que el usuario seleccione "Salir".
    """
    while True:
        # Mostrar opciones del menú
        print("\n" + "="*50)
        print("MENÚ PRINCIPAL - VIDEOCLUB FILMS S.A.")
        print("="*50)
        print("Le damos la bienvenida, por favor escoja el número")
        print("de la opción del menú que le interese:")
        print("\n1. Agregar película")
        print("2. Registrar préstamo")
        print("3. Registrar devolución")
        print("5. Salir")
        print("="*50)
        
        # Solicitar opción del usuario
        opcion = input("Ingrese su opción: ")
        
        # Procesar opción seleccionada
        if opcion == "1":
            agregar_pelicula()
        elif opcion == "2":
            registrar_prestamo()
        elif opcion == "3":
            registrar_devolucion()
        elif opcion == "5":
            # Mostrar mensaje de despedida
            print("\n" + "="*50)
            print("Gracias por su visita. Le esperamos pronto")
            print("="*50)
            break
        else:
            # Opción no válida
            print("\nOpción no válida. Intente nuevamente.")

# ============================================================================
# PROGRAMA PRINCIPAL
# ============================================================================
# Punto de entrada del programa

if __name__ == "__main__":
    # Intentar autenticación del administrador
    if autenticacion():
        # Si la autenticación es exitosa, mostrar el menú principal
        menu_principal()
    else:
        # Si falla la autenticación, terminar el programa
        print("\nEl programa ha sido terminado.")