from validaciones import validar_opcion_menu
from inventario import alta_producto, cargar_herramientas, mostrar_inventario, consultar_stock, reporte_agotados, actualizar_stock


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
            cargar_herramientas(inventario)

        elif opcion == 2:
            mostrar_inventario(inventario)

        elif opcion == 3:
            consultar_stock(inventario)

        elif opcion == 4:
            reporte_agotados(inventario)

        elif opcion == 5:
            alta_producto(inventario)

        elif opcion == 6:
            actualizar_stock(inventario)

        elif opcion == 7:
            print("Saliendo del sistema.")

    except ValueError as e:                                   # Captura los errores de valor producidos durante la ejecución
        print(f"Error: {e}")

