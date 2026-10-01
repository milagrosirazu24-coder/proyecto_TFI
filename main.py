from validaciones import OpcionInvalida, validar_opcion_menu


inventario = []                                                                   # Crea una lista vacía para almacenar los datos del inventario

opcion = 0

while opcion != 7:
    print("\n========== MENÚ PRINCIPAL ==========")
    print("1. Carga de herramientas con existencias iniciales")
    print("2. Visualización de inventario")
    print("3. Consulta de stock")
    print("4. Reporte de agotados")
    print("5. Alta de nuevo producto")
    print("6. Actualización de stock (venta / ingreso)")
    print("7. Salir")

    try:
        opcion = int(input("\nSeleccione una opción: "))     # Se solicita el número de opción elegido
        validar_opcion_menu(opcion)                          # Valida que el número ingresado corresponda a una opción del menú

        if opcion == 1:
            pass

        elif opcion == 2:
            pass

        elif opcion == 3:
            pass

        elif opcion == 4:
            pass

        elif opcion == 5:
            pass

        elif opcion == 6:
            pass

        elif opcion == 7:
            print("Saliendo del sistema.")

    except ValueError:                                       # Captura el error cuando el valor ingresado no puede convertirse a un número entero
        print("Error: Debe ingresar un número entero.")

    except OpcionInvalida as e:                              # Captura el error cuando el número ingresado no corresponde a una opción válida del menú
        print(f"Error: {e}")

