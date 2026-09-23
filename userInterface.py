import readchar


def userInterface():
    end=False
    while end:
        print('''
        1. Añadir producto
        2. Buscar producto
        3. Modificar producto
        4. Eliminar producto
        5. Mostrar productos
        6. Salir
        ''')
        action = ord(readchar.readchar())
        print(action)