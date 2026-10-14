import os
from dataProduct import *


def validacion_nombre(nameProduct):
    """
    Función para validar el nombre de un producto
    :param nameProduct: Nombre solicitado por el usuario
    """
    if nameProduct == "":  # VALIDACIONES: Que el nombre no esté vacio, que tenga una longitud de 3 como mínimo y 50 como máximo
        raise ValueError("Nombre de producto no válido")
    elif len(nameProduct) < 3:
        raise ValueError("No existen productos con el nombre tan corto")
    elif len(nameProduct) > 50:
        raise ValueError("No existen productos con el nombre tan largo")


def error_producto(error):
    """
    Función para mostrar error en la ejecución de cualquier método
    :param error: Error registrado durante la ejecución
    """
    os.system("cls")
    print("Error: {}".format(error))  # Mostramos el error y le obligamos a empezar de nuevo
    input("Por favor, pulse enter y vuelva a intentarlo desde el principio.\n")
    os.system("cls")


def registrar_movimiento():
    """
    Función para registrar una venta o una compra
    """
    try:
        nameProduct = str(input("¿Como se llama el producto que quieres tratar?: ")).strip()
        validacion_nombre(nameProduct)  # Llamamos a la función para validar el nombre
        if nameProduct in productsStock:  # Comprobamos si el producto existe dentro de nuestro almacen
            movimiento = str(
                input("¿Que movimiento quieres registrar, una [V]enta o una [C]ompra?: ")).strip().lower()
            while movimiento != "v" and movimiento != "c":  # Pedimos al usuario que tipo de movimiento quiere realizar (venta o compra)
                movimiento = str(
                    input("¿Que movimiento quieres registrar, una [V]enta o una [C]ompra?: ")).strip().lower()
            if movimiento == "v":
                stock = int(input("¿Cuanto has vendido?: "))
                if stock <= 0:  # VALIDACIONES: Que el stock vendido no sea negativo y que tenga stock en el almacen suficiente
                    raise ValueError("No puedes vender una cantidad negativa")
                elif stock > productsStock[nameProduct]:
                    raise ValueError("No puedes vender una cantidad mayor a la que tienes")
                else:  # Restamos el stock del almacen y mostramos el stock actual
                    productsStock[nameProduct] -= stock
                    print("Stock actualizado correctamente (Stock antiguo {} -> {} Stock nuevo)".format(
                        (productsStock[nameProduct] + stock), productsStock[nameProduct]))
            else:
                stock = int(input("¿Cuanto has comprado?"))
                if stock <= 0:  # VALIDACIONES: Que la cantidad comprada no sea 0 o negativa, para eso existe el modificar stock o registrar venta
                    raise ValueError("No puedes comprar una cantidad negativa")
                else:  # Sumamos el stock comprado y se lo mostramos al usuario
                    productsStock[nameProduct] += stock
                    print("Stock actualizado correctamente (Stock antiguo {} -> {} Stock nuevo)".format(
                        (productsStock[nameProduct] - stock), productsStock[nameProduct]))
        else:  # Si no existe el producto en el almacen saltamos error
            raise ValueError("No existe producto solicitado")

    except ValueError as error:
        error_producto(error)


def insertar_producto():
    """
    Función para insertar un nuevo producto en el almacen
    """
    try:
        nameProduct = str(input("¿Como se llama el producto que quieres insertar?: ")).strip()
        validacion_nombre(nameProduct)
        stockProduct = int(input("¿Cuanto stock tienes de ese producto?: "))
        if stockProduct < 0:  # Comprobamos que el stock del producto insertado no sea negativo
            raise ValueError("No puedes crear un producto con stock negativo")

        priceProduct = float(input("¿Que precio quieres que tenga?: "))
        if priceProduct < 0:  # Comprobamos que el precio del producto insertado no sea negativo
            raise ValueError("No puedes crear un producto con valor negativo")

        productsStock[nameProduct] = stockProduct
        productsPrice[nameProduct] = priceProduct
        # Mostramos un mensaje de confirmación y limpiamos la consola
        os.system("cls")
        print('Producto "{}", con cantidad {} y valor {}€ insertado correctamente'.format(nameProduct, stockProduct,
                                                                                          priceProduct))
        input("Pulse enter para continuar")
        os.system("cls")
    except ValueError as error:
        error_producto(error)


def buscar_producto():
    """
    Función para buscar un producto por su nombre
    :return:
    """
    try:
        nameProduct = str(input("¿Como se llama el producto que quieres buscar?: ")).strip()
        validacion_nombre(nameProduct)
        if nameProduct in productsStock:  # Si el producto se encuentra dentro de nuestro almacen
            os.system("cls")  # mostramos la información del producto
            print("""INFORMACIÓN DE {}
            - STOCK: {}
            - PRECIO: {}€
            - VALOR TOTAL: {}€""".format(nameProduct, productsStock[nameProduct], productsPrice[nameProduct],
                                         productsPrice[nameProduct] * productsStock[nameProduct]))
            input("Pulse enter para continuar")
            os.system("cls")
        else:  # Si no existe el producto se lo mostramos mediante un error
            raise ValueError("No existe producto solicitado")
    except ValueError as error:
        error_producto(error)


def modificar_producto():
    """
    Función para modificar un producto por su nombre
     """
    try:
        nameProduct = str(input("¿Como se llama el producto que quieres modificar?: ")).strip()
        validacion_nombre(nameProduct)
        if nameProduct in productsStock:  # Si tiene ese producto en su almacen
            os.system("cls")  # le ofrecemos modificar el precio o el stock
            action = int(input("""¿Que tipo de dato quieres modificar de {}?
            1. Precio
            2. Stock
            * Pulse cualquier otro NÚMERO para salir: 
            """.format(nameProduct)))
            os.system("cls")
            if action == 1:
                precioUpdate = float(input(
                    "Dime el nuevo precio que quieres ponerle a {} (Precio actual: {}): ".format(nameProduct,
                                                                                                 productsPrice[
                                                                                                     nameProduct])))
                # Si modifica el precio nos aseguramos que la modificación sea válida (>0) y la realizamos
                if precioUpdate < 0:
                    raise ValueError("No puedes poner a un producto valor negativo")
                else:
                    print("Nuevo precio de {} actualizado correctamente {}€ -> {}€".format(nameProduct,
                                                                                           productsPrice[
                                                                                               nameProduct],
                                                                                           precioUpdate))
                    productsPrice[nameProduct] = precioUpdate
            elif action == 2:
                stockUpdate = int(input(
                    "Dime el nuevo stock que quieres ponerle a {} (Stock actual: {}): ".format(nameProduct,
                                                                                               productsStock[
                                                                                                   nameProduct])))
                # Si modifica el stock nos aseguramos que la modificación sea válida (>0) y la realizamos
                if stockUpdate < 0:
                    raise ValueError("No puedes poner a un producto stock negativo")
                else:
                    print("Nuevo stock de {} actualizado correctamente {} -> {}".format(nameProduct,
                                                                                        productsStock[nameProduct],
                                                                                        stockUpdate))
                    productsStock[nameProduct] = stockUpdate

            else:  # En caso de no poner ni el 1 ni el 2 se aborta el proceso
                os.system("cls")
                print("Abortando modificacion")
            input("Pulse enter para continuar")
            os.system("cls")
        else:
            raise ValueError("No existe producto solicitado")
    except ValueError as error:
        error_producto(error)


def eliminar_producto():
    """
    Función para eliminar un producto de nuestro almacen
    """
    try:
        nameProduct = str(input("¿Como se llama el producto que quieres eliminar?: ")).strip()
        validacion_nombre(nameProduct)
        if nameProduct in productsStock:
            del productsStock[
                nameProduct]  # Si el producto existe dentro de nuestro almacen eliminamos el stock y el precio
            del productsPrice[nameProduct]
            os.system("cls")
            print('¡Almacen actualizado correctamente! Producto "{}" eliminado'.format(nameProduct))
            input("Pulse enter para continuar")  # Avisamos al usuario de que la operación fue exitosa
            os.system("cls")
        else:
            raise ValueError("No existe producto solicitado")
    except ValueError as error:
        error_producto(error)


def mostrar_productos():
    """
    Función para mostrar todos los productos del almacen
    """
    try:
        if len(productsStock) == 0:  # Si no tiene productos en el almacen salta el error
            raise ValueError("No tienes productos en tu almacen")
        else:
            os.system("cls")
            print('Estos son todos los productos de tu almacen:\n')
            count = 1  # Mostramos todos los productos y les ponemos un numero al principio
            for producto in productsStock.keys():
                print("{}. {} | Stock actual: {} | Precio actual: {}".format(count, producto, productsStock[producto],
                                                                             productsPrice[producto]))
                count += 1

    except ValueError as error:
        error_producto(error)
