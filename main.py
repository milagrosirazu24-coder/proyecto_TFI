from validaciones import pedir_opcion_menu #Agregué la funcion "pedir_opcion_menu"


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

    opcion = pedir_opcion_menu() # Queda todo validado y limpio

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
