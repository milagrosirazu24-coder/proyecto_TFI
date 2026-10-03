from busquedas import buscar_herramienta

def alta_producto(inventario):
    '''
    Agrega una nueva herramienta al inventario.
    Argumento:
    inventario: lista que contiene las herramientas registradas y sus cantidades.
    '''
    print(f"\n--- Alta de producto ---")
    nombre = input("Ingrese el nombre de la nueva herramienta: ").strip()   # Solicita el nombre de la herramienta
    
    if not nombre:                                                          # Valida que el campo no esté vacío
        raise ValueError("El nombre de la herramienta no puede estar vacío.")
        
    if buscar_herramienta(inventario, nombre):                               # Consulta si la herramienta ya existe en el inventario
        raise ValueError("La herramienta ya se encuentra registrada en el inventario.")
        
    stock = int(input("Ingrese el stock inicial: "))                         # Solicita el stock inicial
    
    if stock < 0:                                                            # Valida que el stock no sea negativo
        raise ValueError("El stock inicial no puede ser negativo.")          
        
    
    inventario.append({'herramienta': nombre, 'cantidad': stock})           # Agrega la nueva herramienta al inventario
    print(f"Herramienta '{nombre}' agregada con éxito.")



def cargar_herramientas(inventario):
    '''
    Carga en el inventario la cantidad de herramientas indicada por el usuario.
    Argumento:
    inventario: lista que contiene las herramientas registradas y sus cantidades.
    '''
    print(f"\n--- Cargar herramientas ---")

    try:
        cantidad_a_cargar = int(input("¿Cuántas herramientas desea cargar?: "))        # Solicita el número total de herramientas a ingresar

    except ValueError:                                                                 # Captura el error si el valor ingresado no puede convertirse a un número entero
        raise ValueError("Debe ingresar un número entero válido.")

    if cantidad_a_cargar <= 0:                                                         # Valida que la cantidad sea mayor a cero
        raise ValueError("La cantidad a cargar debe ser mayor a cero.")

    i = 0                                                                              # Inicializa el contador para el bucle de cargas

    while i < cantidad_a_cargar:

        try:
            print(f"\n--- Carga de herramienta {i + 1} de {cantidad_a_cargar} ---")

            nombre = input("Ingrese el nombre de la herramienta: ").strip()             # Solicita el nombre de la herramienta

            if not nombre:                                                              # Valida que el campo no esté vacío
                raise ValueError("El nombre no puede estar vacío.")

            if buscar_herramienta(inventario, nombre):                                  # Consulta si la herramienta ya existe en el inventario
                raise ValueError("La herramienta ya se encuentra registrada en el inventario.")

            try:
                stock = int(input("Ingrese el stock inicial: "))                        # Solicita el stock inicial

            except ValueError:                                                          # Captura el error si el valor ingresado no puede convertirse a un número entero
                raise ValueError("Debe ingresar un número entero válido para el stock.")

            if stock < 0:                                                               # Valida que el stock no sea negativo
                raise ValueError("El stock inicial no puede ser negativo.")

        except ValueError as e:                                                         # Captura los errores producidos durante la carga
            print(f"Error: {e}")
            continue

        inventario.append({'herramienta': nombre, 'cantidad': stock})                   # Agrega la herramienta al inventario
        print(f"Herramienta '{nombre}' cargada con éxito.")

        i += 1                                                                          # Incrementa el contador después de una carga correcta



def mostrar_inventario(inventario):
    '''
    Muestra las herramientas registradas en el inventario y sus cantidades.
    Argumento:
    inventario: lista que contiene las herramientas registradas y sus cantidades.
    '''

    print(f"\n--- Mostrar inventario ---")

    if not inventario:                                                              # Verifica si el inventario está vacío
        print("No hay inventario para mostrar.")

    for producto in inventario:                                                     # Recorre las herramientas registradas en el inventario
        print(f"Herramienta: {producto['herramienta']} | Stock: {producto['cantidad']}") # Imprime el nombre de la herramienta y la cantidad disponible




def consultar_stock(inventario):
    '''
    Consulta la cantidad disponible de una herramienta en el inventario.
    Argumento:
    inventario: lista que contiene las herramientas registradas y sus cantidades.
    '''

    print(f"\n--- Consulta de stock ---")

    if not inventario:
        raise ValueError("No hay herramientas cargadas en el inventario.")
        
    consulta = input("Ingrese el nombre de la herramienta que desea conocer su stock: ").strip()     # Solicita el nombre de la herramienta que se desea consultar

    if not consulta:                                                              # Valida que el campo no esté vacío
        raise ValueError("El nombre no puede estar vacío.")

    producto = buscar_herramienta(inventario, consulta)                           # Busca la herramienta en el inventario

    if producto:                                                                  # Imprime la cantidad si la herramienta fue encontrada.
        print(f"Herramienta: {producto['herramienta']}. Cantidad: {producto['cantidad']}")

    else:
        print("La herramienta solicitada no se encuentra en el inventario.")       # Informa si la herramienta no fue encontrada.


def reporte_agotados(inventario):
    '''
    Muestra las herramientas del inventario que se encuentran agotadas.
    Argumento:
    inventario: lista que contiene las herramientas registradas y sus cantidades.
    '''

    print(f"\n--- Reporte de herramientas agotadas ---")
    
    agotados_encontrados = False                                                 # Variable para llevar el control si hay o no elementos agotados
    
    for producto in inventario:                                                  # Recorre cada diccionario dentro de la lista principal
        if producto['cantidad'] == 0:                                            # Verifica si la cantidad disponible es exactamente cero
            print(f"Herramienta agotada: {producto['herramienta']}")             # Imprime el nombre de la herramienta sin stock
            agotados_encontrados = True                                          # Indica que se encontró al menos una herramienta agotada
            
    if not agotados_encontrados:                                                 # Comprueba si después de recorrer todo no hubo ningún agotado
        print("No hay herramientas agotadas en este momento.")



def actualizar_stock(inventario):
    '''
    Actualiza el stock de una herramienta mediante una venta o un ingreso.
    Argumento:
    inventario: lista que contiene las herramientas registradas y sus cantidades.
    '''

    print(f"\n--- Actualización de stock ---")

    if not inventario:
        raise ValueError("No hay herramientas cargadas en el inventario.")

    herramienta_a_actualizar = input("Ingrese el nombre de la herramienta que desea actualizar: ").strip()

    if not herramienta_a_actualizar:                                              # Valida que el campo no esté vacío
        raise ValueError("El nombre no puede estar vacío.")

    producto = buscar_herramienta(inventario, herramienta_a_actualizar)           # Busca la herramienta en el inventario

    if producto:

        operacion = input("¿Qué operación desea realizar? (venta / ingreso): ").strip().lower()       # Solicita el tipo de operación que se desea realizar

        if operacion == "venta":

            try:
                venta_producto = int(input("Ingrese la cantidad de unidades que desea vender: "))     # Solicita la cantidad de unidades que se desea vender

            except ValueError:                                                                        # Captura el error si el valor ingresado no puede convertirse a un número entero
                raise ValueError("La cantidad de unidades debe ser un número entero.")

            if venta_producto <= 0:                                                                   # Valida que la cantidad a vender sea mayor a 0
                raise ValueError("La cantidad de unidades a vender debe ser mayor a 0.")

            stock_resultante = producto['cantidad'] - venta_producto                                  # Calcula el stock que quedaría después de realizar la venta

            if stock_resultante < 0:                                                                  # Valida que el stock resultante no sea negativo
                raise ValueError("La venta no se puede realizar porque el stock resultante sería negativo.")

            producto['cantidad'] = stock_resultante                                                   # Actualiza el stock con la cantidad resultante de la venta
            print("Operación realizada exitosamente.")
            print(f"Herramienta: {producto['herramienta']}. Stock actualizado: {producto['cantidad']}")


        elif operacion == "ingreso":

            try:
                ingreso_producto = int(input("Ingrese la cantidad de unidades que desea agregar: "))  # Solicita la cantidad de unidades que se desea agregar

            except ValueError:                                                                        # Captura el error si el valor ingresado no puede convertirse a un número entero
                raise ValueError("La cantidad de unidades a agregar debe ser un número entero.")

            if ingreso_producto <= 0:                                                                 # Valida que la cantidad a agregar sea mayor a cero
                raise ValueError("La cantidad de unidades a agregar debe ser mayor a 0.")

            producto['cantidad'] = producto['cantidad'] + ingreso_producto                            # Suma al stock la cantidad de unidades ingresadas
            print("Operación realizada exitosamente.")
            print(f"Herramienta: {producto['herramienta']}. Stock actualizado: {producto['cantidad']}")

        else:
            raise ValueError("La operación debe ser 'venta' o 'ingreso'.")

    else:
        raise ValueError("La herramienta no se encuentra registrada en el inventario.")