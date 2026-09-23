import readchar

from dataMethod import buscar_producto, insertar_producto, modificar_producto, eliminar_producto, mostrar_produtos


def userInterface():
    end=False
    while not end:
        print('''
        1. Añadir producto
        2. Buscar producto
        3. Modificar producto
        4. Eliminar producto
        5. Mostrar productos
        6. Salir
        ''')
        action = int(input())
        if action == 1:
            print("Opción 1")
            insertar_producto()

        elif action == 2:
            print("Opción 2")
            buscar_producto()

        elif action == 3:
            print("Opción 3")
            modificar_producto()

        elif action == 4:
            print("Opción 4")
            eliminar_producto()

        elif action == 5:
            print("Opción 5")
            mostrar_produtos()

        elif action == 6:
            print("Opción 6")
            end=True