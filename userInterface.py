from dataMethod import buscar_producto, registrar_movimiento, insertar_producto, modificar_producto, eliminar_producto, \
    mostrar_productos


def userInterface():
    """
    Función principal que muestra el menú interactivo de la aplicación de inventario.
    """
    end = False
    while not end:
        print('''
        1. Añadir producto
        2. Buscar producto
        3. Modificar producto
        4. Eliminar producto
        5. Mostrar productos
        6. Registrar movimiento
        7. Salir
        ''')
        try:
            action = int(input("Selecciona una opción: "))
        except ValueError:
            print("Por favor, introduce un número válido.")
            continue
        if action == 1:
            insertar_producto()

        elif action == 2:
            buscar_producto()

        elif action == 3:
            modificar_producto()

        elif action == 4:
            eliminar_producto()

        elif action == 5:
            mostrar_productos()

        elif action == 6:
            registrar_movimiento()

        elif action == 7:
            end = True
        else:
            print("Ingrese una opcion valida")
