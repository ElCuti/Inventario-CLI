
from dataProduct import *


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
        print("Por favor, vuelva a intentarlo desde el principio.\n")

def buscar_producto():
    """

    :return:
    """
    print('Hello World2')


def modificar_producto():
    """

    :return:
     """
    print('Hello World3')


def eliminar_producto():
    """

    :return:
    """
    print('Hello World4')


def mostrar_produtos():
    """

    :return:
    """
    print('Hello World5')
