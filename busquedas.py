# busquedas.py

def buscar_herramienta(inventario, nombre):
    '''
    Busca una herramienta por su nombre dentro del inventario.
    Argumento:
    inventario: lista que contiene las herramientas registradas y sus cantidades.
    nombre: str que representa el nombre de la herramienta a buscar.
    Valor de retorno:
    Retorna el diccionario de la herramienta si se encuentra registrada y None si no se encuentra.
    '''
    for producto in inventario:
        if producto['herramienta'].lower() == nombre.strip().lower():
            return producto

    return None
