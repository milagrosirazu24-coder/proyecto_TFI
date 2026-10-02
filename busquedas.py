# busquedas.py

def buscar_herramienta(inventario, nombre):
    for producto in inventario:  # Recorre cada elemento (diccionario) dentro de la lista inventario
        if producto['herramienta'].lower() == nombre.strip().lower():  # Compara el nombre normalizado (sin importar mayúsculas)
            return True  # Retorna True si encuentra la herramienta
    return False  # Retorna False si el bucle termina y no la encontró