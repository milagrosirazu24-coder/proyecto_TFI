

def validar_opcion_menu(numero):
    '''
    Valida que el número ingresado corresponda a una opción del menú.
    Argumentos:
    numero: int que representa la opción ingresada.
    Valor de retorno:
    Retorna True si el número es válido. Si el número no es válido, lanza ValueError.
    '''

    if numero < 1 or numero > 7:
        raise ValueError("Debe ingresar un número del 1 al 7.")

    return True


