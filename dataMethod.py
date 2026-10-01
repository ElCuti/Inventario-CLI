from itertools import product

from dataProduct import *

def registrar_movimiento():
    try:
        nameProduct = str(input("¿Como se llama el producto que quieres tratar?")).strip()
        if (nameProduct == ""):
            raise ValueError("Nombre de producto no válido")
        elif len(nameProduct) < 3:
            raise ValueError("No existen productos con el nombre tan corto")
        elif len(nameProduct) > 50:
            raise ValueError("No existen productos con el nombre tan largo")
        else:
            if nameProduct in productsStock:
                movimiento = str(input("¿Que movimiento quieres registrar, una [V]enta o una [C]ompra?")).strip().lower()
                while movimiento!= "v" and movimiento!= "c":
                    movimiento = str(input("¿Que movimiento quieres registrar, una [V]enta o una [C]ompra?")).strip().lower()
                if movimiento == "v":
                    stock = int(input("¿Cuanto has vendido?"))
                    if stock <= 0:
                        raise ValueError("No puedes vender una cantidad negativa")
                    elif stock > productsStock[nameProduct]:
                        raise ValueError("No puedes vender una cantidad mayor a la que tienes")
                    else:
                        productsStock[nameProduct] -= stock
                        print("Stock actualizado correctamente (Stock antiguo {} -> {} Stock nuevo)".format(
                            (productsStock[nameProduct] + stock), productsStock[nameProduct]))
                else:
                    stock = int(input("¿Cuanto has comprado?"))
                    if stock <= 0:
                        raise ValueError("No puedes comprar una cantidad negativa")
                    else:
                        productsStock[nameProduct] += stock
                        print("Stock actualizado correctamente (Stock antiguo {} -> {} Stock nuevo)".format(
                            (productsStock[nameProduct] - stock), productsStock[nameProduct]))
            else:
                raise ValueError("No existe producto solicitado")

    except ValueError as error:
        print("Error: {}".format(error))
        input("Por favor, pulse enter y vuelva a intentarlo desde el principio.\n")

def insertar_producto():
    """

    :return:
    """
    try:
        nameProduct = str(input("¿Como se llama el producto que quieres insertar?")).strip()
        if (nameProduct == ""):
            raise ValueError("Nombre de producto no válido")
        elif len(nameProduct) < 3:
            raise ValueError("El nombre es demasiado corto (mínimo 3 caracteres)")
        elif len(nameProduct) > 50:
            raise ValueError("El nombre es demasiado largo (máximo 50 caracteres)")

        stockProduct = int(input("¿Cuanto stock tienes de ese producto?"))
        if stockProduct < 0:
            raise ValueError("No puedes crear un producto con stock negativo")

        priceProduct = float(input("¿Que precio quieres que tenga?"))
        if priceProduct < 0:
            raise ValueError("No puedes crear un producto con valor negativo")

        productsStock[nameProduct] = stockProduct
        productsPrice[nameProduct] = priceProduct
        print("Producto insertado correctamente")
        print(productsStock, productsPrice)
    except ValueError as error:
        print("Error: {}".format(error))
        input("Por favor, pulse enter y vuelva a intentarlo desde el principio.\n")

def buscar_producto():
    """

    :return:
    """
    try:
        nameProduct = str(input("¿Como se llama el producto que quieres buscar?")).strip()
        if (nameProduct == ""):
            raise ValueError("Nombre de producto no válido")
        elif len(nameProduct) < 3:
            raise ValueError("No existen productos con el nombre tan corto")
        elif len(nameProduct) > 50:
            raise ValueError("No existen productos con el nombre tan largo")
        else:
            if nameProduct in productsStock:
                print("""INFORMACIÓN DE {}
                - STOCK: {}
                - PRECIO: {}€
                - VALOR TOTAL: {}€""".format(nameProduct, productsStock[nameProduct], productsPrice[nameProduct], productsPrice[nameProduct]*productsStock[nameProduct]))
            else:
                raise ValueError("No existe producto solicitado")
    except ValueError as error:
        print("Error: {}".format(error))
        input("Por favor, pulse enter y vuelva a intentarlo desde el principio.\n")


def modificar_producto():
    """

    :return:
     """
    try:
        nameProduct = str(input("¿Como se llama el producto que quieres modificar?")).strip()
        if (nameProduct == ""):
            raise ValueError("Nombre de producto no válido")
        elif len(nameProduct) < 3:
            raise ValueError("No existen productos con el nombre tan corto")
        elif len(nameProduct) > 50:
            raise ValueError("No existen productos con el nombre tan largo")
        else:
            if nameProduct in productsStock:
                action = int(input("""¿Que tipo de dato quieres modificar?
                1. Precio
                2. Stock
                * Pulse cualquier otro número para salir
                """))
                if action == 1:
                    precioUpdate = float(input("Dime el nuevo precio que quieres ponerle a {} (Precio actual: {}): ".format(nameProduct,productsPrice[nameProduct])))
                    if precioUpdate < 0:
                        raise ValueError("No puedes poner a un producto valor negativo")
                    else:
                        print("Nuevo precio de {} actualizado correctamente {}€ -> {}€".format(nameProduct,productsPrice[nameProduct],precioUpdate))
                        productsPrice[nameProduct] = precioUpdate
                elif action == 2:
                    stockUpdate = int(input("Dime el nuevo stock que quieres ponerle a {} (Stock actual: {}): ".format(nameProduct, productsStock[nameProduct])))
                    if stockUpdate < 0:
                        raise ValueError("No puedes poner a un producto stock negativo")
                    else:
                        print("Nuevo stock de {} actualizado correctamente {} -> {}".format(nameProduct,productsStock[nameProduct],stockUpdate))
                        productsStock[nameProduct] = stockUpdate
                else:
                    print("Abortando modificacion")
            else:
                raise ValueError("No existe producto solicitado")
    except ValueError as error:
        print("Error: {}".format(error))
        input("Por favor, pulse enter y vuelva a intentarlo desde el principio.\n")


def eliminar_producto():
    """

    :return:
    """
    try:
        nameProduct = str(input("¿Como se llama el producto que quieres eliminar?")).strip()
        if (nameProduct == ""):
            raise ValueError("Nombre de producto no válido")
        elif len(nameProduct) < 3:
            raise ValueError("No existen productos con el nombre tan corto")
        elif len(nameProduct) > 50:
            raise ValueError("No existen productos con el nombre tan largo")
        else:
            if nameProduct in productsStock:
                del productsStock[nameProduct]
                del productsPrice[nameProduct]
                print("¡Almacen actualizado correctamente! producto {} eliminado".format(nameProduct))
            else:
                raise ValueError("No existe producto solicitado")
    except ValueError as error:
        print("Error: {}".format(error))
        input("Por favor, pulse enter y vuelva a intentarlo desde el principio.\n")


def mostrar_produtos():
    """

    :return:
    """
    print('Estos son todos los productos de tu almacen')
    count = 1
    for producto in productsStock.keys():
        print("{}. {} | Stock actual: {} | Precio actual: {}".format(count,producto,productsStock[producto],productsPrice[producto]))
        count+=1