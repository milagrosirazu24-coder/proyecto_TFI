from busquedas import buscar_herramienta

def alta_producto(inventario):
    nombre = input("Ingrese el nombre de la nueva herramienta: ").strip()  # Solicita el nombre y elimina espacios sobrantes
    
    if not nombre:  # Valida si el campo quedó vacío
        raise ValueError("El nombre de la herramienta no puede estar vacío.")  # Lanza error si está vacío
        
    if buscar_herramienta(inventario, nombre):  # Consulta si ya existe usando la función auxiliar
        raise ValueError("La herramienta ya se encuentra registrada en el inventario.")  # Lanza error si está duplicada
        
    stock = int(input("Ingrese el stock inicial: "))  # Pide la cantidad inicial
    if stock < 0:  # Valida que el stock no sea negativo
        raise ValueError("El stock inicial no puede ser negativo.")  # Lanza error si es negativo
        
    # Si pasa todas las validaciones, agrega el diccionario a la lista principal
    inventario.append({'herramienta': nombre, 'cantidad': stock})  # Inserta el nuevo producto al final del inventario
    print(f"Herramienta '{nombre}' agregada con éxito.")  # Mensaje de confirmación


def cargar_herramientas(inventario):
    try:
        cantidad_a_cargar = int(input("¿Cuántas herramientas desea cargar?: ")) # Solicita el número total de herramientas a ingresar
        if cantidad_a_cargar <= 0: # Valida que la cantidad sea mayor a cero
            print("Error: La cantidad a cargar debe ser mayor a cero.") # Muestra mensaje si la cantidad no es válida
            return # Sale de la función si hay error
    except ValueError: # Captura el error si ingresan texto en vez de números
        print("Error: Debe ingresar un número entero válido.") # Informa que se esperaba un entero
        return # Sale de la función

    i = 0 # Inicializa el contador para el bucle de cargas
    while i < cantidad_a_cargar: # Bucle que se repite hasta completar la cantidad indicada
        print(f"\n--- Carga de herramienta {i + 1} de {cantidad_a_cargar} ---") # Muestra el número de herramienta actual
        
        nombre = input("Ingrese el nombre de la herramienta: ").strip() # Pide el nombre de la herramienta y quita espacios vacíos
        if not nombre: # Verifica si el campo quedó vacío
            print("Error: El nombre no puede estar vacío. Intente nuevamente.") # Muestra aviso si está vacío
            continue # Salta a la siguiente iteración para volver a pedir este producto
            
        if buscar_herramienta(inventario, nombre): # Llama a la función de búsqueda para detectar duplicados
            print("Error: La herramienta ya se encuentra registrada en el inventario. Ingrese otra.") # Aviso de duplicado
            continue # Vuelve a pedir el nombre si ya existe
            
        try:
            stock = int(input("Ingrese el stock inicial: ")) # Solicita el stock inicial de la herramienta
            if stock < 0: # Valida que el stock no sea un número negativo
                print("Error: El stock inicial no puede ser negativo. Intente nuevamente.") # Aviso de stock negativo
                continue # Vuelve a pedir el stock
        except ValueError: # Captura error si el stock ingresado no es numérico
            print("Error: Debe ingresar un número entero válido para el stock. Intente nuevamente.") # Aviso de error numérico
            continue # Vuelve a pedir el stock
            
        inventario.append({'herramienta': nombre, 'cantidad': stock}) # Agrega el diccionario con los datos a la lista principal
        print(f"Herramienta '{nombre}' cargada con éxito.") # Mensaje de confirmación del éxito de la carga
        
        i += 1 # Incrementa el contador solo si la carga se completó bien