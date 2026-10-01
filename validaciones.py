class OpcionInvalida(Exception): # Define una excepción personalizada para las opciones inválidas del menú.
    pass

def validar_opcion_menu(numero):
    '''
    Valida que el número ingresado corresponda a una opción del menú.
    Argumentos:
    numero: int que representa la opción ingresada.
    Valor de retorno:
    Retorna True si el número es válido. Si el número no es válido, lanza la excepción OpcionInvalida.
    '''

    if numero < 1 or numero > 7:
        raise OpcionInvalida("Debe ingresar un número del 1 al 7.")

    return True

def pedir_opcion_menu():
    while True:
        try:
            numero = int(input("\nSeleccione una opción: ")) # Intentamos convertir la entrada directamente a entero, si se ingresó una letra o frase, int() falla y salta al except           
            validar_opcion_menu(numero) # Valida si está entre 1 y 7
            return numero # Si todo es correcto, devuelve el número
            
        except ValueError:
            print("Error: Debe ingresar un número entero.")
        except OpcionInvalida as e:
            print(f"Error: {e}")