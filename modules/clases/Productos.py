'''
SENA CBA CENTRO DE BIOTECNOLOGIA AGROPECUARIA
PROGRAMACION DE SOFTWARE

FICHA: 2877795
AUTOR: NICOLAS ANDRES ACOSTA HIGUERA
PROYECTO: TIENDA VIRTUAL (clase Productos)
FECHA: 2024-07-01
VERSION: 4.5.6
'''

class Producto:
    '''
    Clase que representa un producto en la tienda virtual.
    '''
    def __init__(self, codigo='', descripcion='', inventario= 0, precio=0.00):
        """
        Constructor de la clase Productos.

        Args:
            codigo (int): El código del producto.
            descripcion (str): La descripción del producto.
            inventario (int): La cantidad en inventario del producto.
            precio (float): El precio del producto.
        """
        self.__codigo = codigo
        self.__descripcion = descripcion
        self.__inventario = inventario
        self.__precio = precio




    def set_codigo(self, codigo):
        """
        Establece el código del producto.

        Args:
            codigo (int): El nuevo código del producto.
        """
        self.__codigo = codigo

    def get_codigo(self):
        """
        Obtiene el código del producto.

        Returns:
            int: El código del producto.
        """
        return self.__codigo



    def set_descripcion(self, descripcion):
        """
        Establece la descripción del producto.

        Args:
            descripcion (str): La nueva descripción del producto.
        """
        self.__descripcion = descripcion
        
    def get_descripcion(self):
        """
        Obtiene la descripción del producto.

        Returns:
            str: La descripción del producto.
        """
        return self.__descripcion



    def set_inventario(self, inventario):
        """
        Establece la cantidad en inventario del producto.

        Args:
            inventario (int): La nueva cantidad en inventario del producto.
        """
        self.__inventario = inventario
        
    def get_inventario(self):
        """
        Obtiene la cantidad en inventario del producto.

        Returns:
            int: La cantidad en inventario del producto.
        """
        return self.__inventario


    def set_precio(self, precio):
        """
        Establece el precio del producto.

        Args:
            precio (float): El nuevo precio del producto.
        """
        self.__precio = precio

    def get_precio(self):
        """
        Obtiene el precio del producto.

        Returns:
            float: El precio del producto.
        """
        return self.__precio



    def obtener_atributos(self):
        """
        Obtiene un diccionario con los atributos del producto.

        Returns:
            dict: Un diccionario con los atributos del producto.
        """
        atributos = {
            'codigo': self.__codigo,
            'descripcion': self.__descripcion,
            'inventario': self.__inventario,
            'precio': self.__precio
        }
        return atributos