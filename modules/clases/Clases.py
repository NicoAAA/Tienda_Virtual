'''
SENA CBA CENTRO DE BIOTECNOLOGIA AGROPECUARIA
PROGRAMACION DE SOFTWARE

FICHA: 2877795
AUTOR: NICOLAS ANDRES ACOSTA HIGUERA
PROYECTO: TIENDA VIRTUAL (clase Productos)
FECHA: 2024-07-01
VERSION: 4.5.6
'''

'''
Modulo que contiene las clases Producto y ProductosVenta.
En estas clases se gestionan los productos de venta, se pueden
agregar, eliminar, modificar y buscar productos.
'''

'''
IMPORTACIONES DE LIBRERIAS
'''
# Importar el módulo json para trabajar con archivos JSON
import json

# Importar el módulo os para acceder a funcionalidades dependientes del Sistema Operativo
import os

# Importar el módulo re para trabajar con expresiones regulares
import re

# Importar la clase FPDF para crear documentos PDF
from fpdf import FPDF

# Importar la función prompt del módulo prompt_toolkit para mostrar diálogos interactivos
from prompt_toolkit.shortcuts import radiolist_dialog, message_dialog, button_dialog, input_dialog

# Importar las variables de estilo de la tienda virtual
from modules.styles.styles_store import style, style_9, styles, style_10

# Immportar la clase datetime para trabajar con fechas y horas
from datetime import datetime

# Importar el módulo shutil para trabajar con archivos y directorios
import shutil


""" 
IMORTACIONES LOCALES
"""
# Importar la clase Producto del módulo Productos
from modules.clases.Productos import Producto

# Importar la función ir_al_menu del módulo menu_principal
from modules.menu_principal import ir_al_menu

# Importar la función enviar_por_pdf del módulo correo
from modules.mail.correo import enviar_por_pdf





class ProductosVenta:
    '''
    Clase que gestiona los productos de venta.
    
    Atributos:
        lista_productos_venta (list): Lista de productos de venta.
    '''
    def __init__(self, lista_productos_venta=None):
        '''
        Método constructor de la clase ProductosVenta.
        
        Args:
            lista_productos_venta (list): Lista de productos de venta.
        '''
        if lista_productos_venta is None:
            lista_productos_venta = []
        self.__lista_productos_venta = lista_productos_venta
    

        
    
    def get_lista_productos_venta(self):
        '''
        Método que obtiene la lista de productos de venta.
        
        Returns:
            list: La lista de productos de venta.
        '''
        return self.__lista_productos_venta
    
    def cargar_archivo_producto(self):
            """
            Carga los productos desde un archivo JSON y los agrega a la lista de productos de venta.

            El método lee un archivo JSON llamado 'datos.json' y recorre los objetos en el archivo.
            Por cada objeto, crea una instancia de la clase Producto, establece sus atributos con 
            los valores del objeto y agrega el producto a la lista de productos de venta.

            Args:
                self: La instancia de la clase ProductosVenta.

            Returns:
                tabla: La tabla con los productos cargados desde el archivo.
            """
            
            # Limpiar la lista de productos para evitar duplicados
            self.__lista_productos_venta.clear()
            
            tabla = """
╔════════════════════════════════════════════════════════════════════════════════════════════════╗
║                               PRODUCTOS CARGADOS DESDE ARCHIVOS                                ║
╠════════════════════╦══════════════════════════════════════╦═════════════════╦══════════════════╣
║ CODIGO PRODUCTO    ║          DESCRIPCION                 ║  INVENTARIO     ║  PRECIO DE VENTA ║
╠════════════════════╬══════════════════════════════════════╬═════════════════╬══════════════════╣
"""
            with open('BD_USO/datos.json', 'r') as json_file:
                data = json.load(json_file)

                for objeto in data:
                    producto = Producto()
                    producto.set_codigo(objeto['codigo'])
                    producto.set_descripcion(objeto['descripcion'])
                    producto.set_inventario(objeto['inventario'])
                    producto.set_precio(objeto['precio'])
                    self.__lista_productos_venta.append(producto)
                    tabla += '║ {0:<18} ║ {1:<36} ║ {2:<15} ║ {3:<16.2f} ║\n'.format( 
                        str(objeto['codigo']),
                        str(objeto['descripcion']),
                        int(objeto['inventario']),
                        float(objeto['precio']))
                
                    
                tabla += "╚════════════════════╩══════════════════════════════════════╩═════════════════╩══════════════════╝\n"
             
                return tabla
               
                
    def existencia_productos(self):
        '''
        Método que muestra la existencia de productos en la lista de productos de venta.
        
        Returns:
            str: La tabla con los productos cargados desde el archivo.
        '''
     
        tabla = """
╔════════════════════════════════════════════════════════════════════════════════════════════════╗
║                               PRODUCTOS CARGADOS DESDE ARCHIVOS                                ║
╠════════════════════╦══════════════════════════════════════╦═════════════════╦══════════════════╣
║ CODIGO PRODUCTO    ║          DESCRIPCION                 ║  INVENTARIO     ║  PRECIO DE VENTA ║
╠════════════════════╬══════════════════════════════════════╬═════════════════╬══════════════════╣
"""
        objeto = Producto()
        for objeto in self.__lista_productos_venta:
            tabla += '║ {0:<18} ║ {1:<36} ║ {2:<15} ║ {3:<16.2f} ║\n'.format(
                objeto.get_codigo(),
                objeto.get_descripcion(),
                objeto.get_inventario(),
                objeto.get_precio()
                )
        tabla += "╚════════════════════╩══════════════════════════════════════╩═════════════════╩══════════════════╝\n"
        return tabla
       
    
    
    def digitar_dato(self, mensaje):
        """
        Solicita al usuario que digite un dato.

        Args:
            mensaje (str): El mensaje que se mostrará al usuario.

        Returns:
            str: El dato ingresado por el usuario.
        """
        dato = input(mensaje)
        return dato
    
    
    def agregar_producto(self):
        '''
        Método que permite agregar un producto a la lista de productos de venta.
        '''
        
        cod= self.validar_codigo()
      
        des= self.validar_descripcion()       
      
        inv= self.validar_inventario()
       
        pre= self.validar_precio()
        
        self.__lista_productos_venta.append(Producto(cod, des, inv, pre))
        self.grabar_archivo_producto()
        
        
        
        tabla = f"""
╔════════════════════════════════════════════════════════════════════════════════════════════════╗
║ El producto con código {cod} ha sido agregado correctamente.                                 ║
╠════════════════════╦══════════════════════════════════════╦═════════════════╦══════════════════╣
║ CODIGO PRODUCTO    ║          DESCRIPCION                 ║  INVENTARIO     ║  PRECIO DE VENTA ║
╠════════════════════╬══════════════════════════════════════╬═════════════════╬══════════════════╣
"""
        
        tabla += '║ {0:<18} ║ {1:<36} ║ {2:<15} ║ {3:<16.2f} ║\n'.format(
            cod,des,inv,pre
            )
        tabla += "╚════════════════════╩══════════════════════════════════════╩═════════════════╩══════════════════╝\n"
        
        message_dialog(
            title='PRODUCTO AGREGADO',
            text=tabla,
            style= style_10
        ).run()


 
    
        
        

    
    def grabar_archivo_producto(self):
            """
            Guarda los productos en un archivo JSON.

            Este método recorre la lista de productos y crea un diccionario 
            con la información de cada producto.
            
            Luego, guarda los datos en un archivo JSON llamado 'datos.json' 
            en formato legible.

            Args:
                self: La instancia de la clase ProductosVenta.

            Returns:
                None: No retorna nada.
            """
            data = []
            
            for objeto in self.get_lista_productos_venta():
                data.append(dict(
                    codigo = objeto.get_codigo(),
                    descripcion = objeto.get_descripcion(),
                    inventario = objeto.get_inventario(),
                    precio = objeto.get_precio()
                ))
            
            with open('BD_USO/datos.json', 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=4)
        
    
    
        
                
       
    def validar_codigo(self):
        '''
        Método que solicita al usuario el código del producto.
        
        Returns:
            str: El código del producto.
        '''
        while True:
                try:
                    
                    
                    codigo= input_dialog(
                        title='Código del Producto',
                        text= self.existencia_productos() + '\nDIGITE EL CÓDIGO DEL PRODUCTO (máximo 7 dígitos):',          
                        ok_text='Aceptar',
                        cancel_text= 'Cancelar',
                        style= styles
                    ).run()
                    
                    if codigo== None:
                        ir_al_menu() 
                        
            
                    
                    if not codigo.isdigit():
                        raise ValueError ('El código debe ser numérico. Por favor, intente de nuevo.                     ')
                    
                    if len(codigo) > 7:
                        raise ValueError ('El código debe tener máximo 7 dígitos. Por favor, intente de nuevo.           ')
                    
                    codigo = codigo.zfill(7)
                    
                    if self.verificar_codigo(codigo):
                        raise ValueError ('El código ya existe. Ingrese un código diferente. Por favor, intente de nuevo.')
                    
                    os.system('cls')
    
                    break

                except ValueError as ve:
                    error_message = f"Error: {ve}"
                    os.system('cls' if os.name == 'nt' else 'clear')
                    
                    message_dialog(
                        title='Error',
                        text=error_message
                    ).run()
                                
        return codigo
    
    
    def validar_descripcion(self):
        '''
        Método que solicita al usuario la descripción del producto.
        
        Returns:
            str: La descripción del producto.
        
        '''
        while True:
            try:
                descripcion= input_dialog(
                    title='Descripción del Producto',
                    text=self.existencia_productos() + '\nDIGITE LA DESCRIPCIÓN DEL PRODUCTO :',
                    ok_text='Aceptar',
                    style= style_9
                ).run()
                
                if descripcion== None:
                    ir_al_menu()
                
                
                
                
                
                if not isinstance(descripcion, str):
                    raise ValueError("La descripción debe ser una cadena de texto.")
                
                if not descripcion.strip():
                    raise ValueError("La descripción no puede estar vacía o contener solo espacios en blanco.       ")
                
                if len(str(descripcion)) > 36:
                    raise ValueError ('El inventario debe tener máximo 36 caracteres. Por favor, intente de nuevo.   ')
                
                if not any(char.isalpha() for char in descripcion):
                    raise ValueError("La descripción debe contener al menos una letra y no puede ser solo números.  ")
                
                descripcion = descripcion.upper()
                
                if self.verificar_descripcion(descripcion):
                    raise ValueError ('El código ya existe. Ingrese un código diferente. Por favor, intente de nuevo.')
                
                os.system('cls')
                break

            except ValueError as ve:
                error_message = f"Error: {ve}"
                os.system('cls' if os.name == 'nt' else 'clear')
                
                
                message_dialog(
                    title='Error',
                    text=error_message
                ).run()
        return descripcion
    
    
    def validar_inventario(self):
        '''
        Método que solicita al usuario la cantidad de productos en el inventario.
        
        Returns:
            int: La cantidad de productos en el inventario.
        '''
        while True:
                try:
                    cantidad= input_dialog(
                        title='PRODUCTOS EN INVENTARIO',
                        text=self.existencia_productos() + '\nDIGITE LA CANTIDAD DE PRODUCTOS EN INVENTARIO:'.strip(),
                        ok_text='Aceptar',
                        cancel_text='Cancelar',
                        style=style_9
                    ).run()
                    
                    if cantidad== None:
                        ir_al_menu()
                    
                    
                    if not cantidad.isdigit():
                        raise ValueError ('La cantidad de productos en el inventario debe ser un dato numérico. Por favor, intente de nuevo. ')
                    
                    if len(cantidad) > 15:
                        raise ValueError ('El inventario debe tener máximo 15 dígitos. Por favor, intente de nuevo.                          ')
                    os.system('cls')
                    break
                    
                    
                except ValueError as ve:
                    error_message = f"Error: {ve}"
                    os.system('cls' if os.name == 'nt' else 'clear')
                    
                    
                    message_dialog(
                        title='Error',
                        text=error_message
                    ).run()
                         
        return int(cantidad)
    
    def validar_precio(self):
        '''
        Método que solicita al usuario el precio del producto.
        
        Returns:
            float: El precio del producto.
        '''
        while True:
            try:
                precio= input_dialog(
                    title='PRODUCTOS EN INVENTARIO',
                    text= self.existencia_productos() + '\nDIGITE EL PRECIO DEL PRODUCTO:'.strip(),
                    ok_text='Aceptar',
                    cancel_text= 'Cancelar',
                    style=style_9
                ).run()
                
                if precio== None:
                        ir_al_menu()
                
                
                try:
                    precio = float(precio)
                except ValueError:
                    raise ValueError('El precio debe ser un número entero o flotante. Por favor, intente de nuevo.')
                
                if len(str(int(precio))) > 16:
                    raise ValueError('El precio debe tener máximo 16 dígitos antes del punto decimal. Por favor, intente de nuevo.')
                
                os.system('cls')
                break
                
            except ValueError as ve:
                
                error_message = f"Error: {ve}"
                os.system('cls' if os.name == 'nt' else 'clear')
                self.existencia_productos()
                    
                message_dialog(
                    title='Error',
                    text=error_message
                ).run()
                
        return precio
    
    
    
    def eliminar_producto(self):
        '''
        Método que permite eliminar un producto de la lista de productos de venta
        por medio de su código.
        
        Returns:
            bool: True si se desea borrar más productos, False si no se desea borrar más productos.
        '''
        
        titulo= (
    f"╔═════════════════════════════════════════════════════════════════════════════════════════════════════╗\n"
    f"║ Para ELIMINAR un producto siga las siguientes instruccciones:                                       ║\n"
    f"╚═════════════════════════════════════════════════════════════════════════════════════════════════════╝\n"
        )
        
        code=self.eliminar_con_codigo(titulo)
        
        confirmar_eliminar_producto= button_dialog(
            title="ELIMINAR PRODUCTO",
            text= self.existencia_productos() +f"¿Está seguro que desea eliminar el producto de codigo: {code}?",
            buttons=[
                ("Sí", True),
                ("No", False)
            ],
            style=style_9
        ).run()
        
        
        if confirmar_eliminar_producto:
            
            for producto in self.__lista_productos_venta:
                if producto.get_codigo() == code:
                    self.__lista_productos_venta.remove(producto)
                    self.grabar_archivo_producto()
            
            borrar_nuevamente_True= button_dialog(
                    title="BORRAR PRODUCTO",
                    text="Producto ELIMINADO Correctamente\n\n¿Desea borrar más productos?".center(10," "),
                    buttons=[
                    ("Sí", True),
                    ("No", False)
                    ],
                    style=styles
                ).run()
            
            return borrar_nuevamente_True
                        
        else:
           
            borrar_nuevamente_False= button_dialog(
                    title="BORRAR PRODUCTO",
                    text="¿Desea borrar algun producto?",
                    buttons=[
                    ("Sí", True),
                    ("No", False)
                ],
                style=style
                ).run()
            
            return borrar_nuevamente_False
            
        
        
         
    def eliminar_con_codigo(self,titulo):
        '''
        Método que solicita al usuario el código del producto a eliminar.
        
        Args:
            titulo (str): El título del diálogo.
        
        Returns:
            str: El código del producto a eliminar.
        '''
        while True:
                try:
                    codigo= input_dialog(
                        title='PRODUCTOS EN INVENTARIO',
                        text= titulo+self.existencia_productos() + '\nDIGITE EL CÓDIGO DEL PRODUCTO A ELIMINAR (máximo 7 dígitos):'.strip(),
                        ok_text='Aceptar',
                        cancel_text= 'Cancelar',
                        style= style_9
                     ).run()
                    
                    if codigo== None:
                        ir_al_menu()
                    
                    
                    
                    if not codigo.isdigit():
                        raise ValueError ('El código debe ser numérico. Por favor, intente de nuevo.                     ')
                    
                    if len(codigo) > 7:
                        raise ValueError ('El código debe tener máximo 7 dígitos. Por favor, intente de nuevo.           ')
                    
                    codigo = codigo.zfill(7)
                    
                    if not self.verificar_codigo(codigo):
                        raise ValueError ('El código no existe. Ingrese un código diferente. Por favor, intente de nuevo.')
                    
                    os.system('cls')
                    break
                    
                    
                

                except ValueError as ve:
                    
                    error_message = f"Error: {ve}"
                    os.system('cls' if os.name == 'nt' else 'clear')
                    
                    message_dialog(
                        title='Error',
                        text=error_message
                    ).run()
                    
        return codigo          
    
    def verificar_codigo(self, codigo):
        '''
        Método que verifica si el código de un producto ya existe en la lista de productos de venta.
        
        Args:
            codigo (str): Código del producto.
            
        Returns:
            bool: True si el código ya existe, False si no existe.
        
        '''
        
        for producto in self.__lista_productos_venta:
            if producto.get_codigo() == codigo:
                return True
            
        return False
            
    
    def verificar_descripcion(self, descripcion):
        '''
        Método que verifica si la descripción de un producto ya existe en la lista de productos de venta.
        
        Args:
            descripcion (str): Descripción del producto.
        
        Returns:
            bool: True si la descripción ya existe, False si no existe.
        '''
        
        for producto in self.__lista_productos_venta:
            if producto.get_descripcion() == descripcion:
                return True
            
    def modificar_inventario(self, codigo):
        
        '''
        Método que modifica el inventario de un producto en la lista de productos de venta.
        '''
        
        for producto in self.__lista_productos_venta:
            if producto.get_codigo() == codigo:
                return producto.get_codigo()
    
    def copia_respaldo(self):
        '''
        Método que crea una copia de respaldo de la base de datos en un archivo JSON.
        
        args:
            self: instancia de la clase ProductosVenta
        
        return:
            None
        '''
        
        # Se obtiene la fecha y hora actual
        fecha_hoy= datetime.now().strftime("%d-%m-%Y_%Hh.%Mm.%Ss")
        
        # Variable que almacena la carpeta donde se guardará la copia de respaldo
        carpeta= 'BD_JSON'
        
        # El nombre del archivo de respaldo
        nombre_archivo_respaldo = f'BD-{fecha_hoy}.json' 
        
        # La ruta del archivo de respaldo
        ruta_archivo = os.path.join(carpeta, nombre_archivo_respaldo)
        
        # Se crea la carpeta si no existe 
        self.ordenar_por_codigo()
        with open(ruta_archivo, 'w') as archivo_respaldo:
            productos_diccionario = [producto.obtener_atributos() for producto in self.get_lista_productos_venta()]
            json.dump(productos_diccionario, archivo_respaldo, indent=4)
    
    def reparar_datos(self):
        '''
        Método que permite reparar un archivo JSON que no se pueda cargar.
        '''
        
        # Variable que almacena la carpeta donde se guardará la copia de respaldo
        carpeta= 'BD_JSON'
        
        # Variable que almacena los archivos de respaldo
        archivos_respaldo = [archivo for archivo in os.listdir(carpeta) if archivo.endswith('.json')]
        
        # Si no hay archivos de respaldo, se muestra un mensaje y termina
        if not archivos_respaldo:
            message_dialog(
                title='ERROR',
                text='No hay copias de respaldo disponibles.'
            ).run()
            return ir_al_menu()
            
        
        else:
            # Se crea una lista de tuplas con los archivos de respaldo disponibles
            opciones = [(archivo, archivo) for archivo in archivos_respaldo] 
        
            # Mostrar un diálogo de lista radial con los archivos de respaldo disponibles
            archivo_seleccionado = radiolist_dialog(
                title='Seleccionar archivo de respaldo',
                text='Copias de respaldo disponibles:',
                values=opciones,
                style=style  
            ).run()
            
            if archivo_seleccionado == None:
                ir_al_menu()
            
            
        
        # Si el usuario seleccionó un archivo
        if archivo_seleccionado:
            ruta_archivo_seleccionado = os.path.join(carpeta, archivo_seleccionado)
        
        
        
            
            # se crea la copia del archivo
            fecha_actual = datetime.now().strftime('%d-%m-%Y_%Hh.%Mm.%Ss')
            nombre_copia = f'{os.path.splitext(archivo_seleccionado)[0]}-COPIA-{fecha_actual}.json'
            ruta_copia = os.path.join(carpeta, nombre_copia)

            

            try:
                with open(ruta_archivo_seleccionado, 'r') as archivo:
                    data = json.load(archivo)
                if not data:
                    

                    os.remove(ruta_archivo_seleccionado)
                    message_dialog(
                        title='Archivo eliminado',
                        text=f'El archivo vacío {archivo_seleccionado} ha sido eliminado.'
                    )
                    
                else:
                
                    # Se crea una copia de respaldo del archivo seleccionado con la fecha y hora actual
                    shutil.copy2(ruta_archivo_seleccionado, ruta_copia)
                    message_dialog(
                        title='Copia de respaldo creada',
                        text=f'Copia de respaldo creada: {ruta_copia}'
                    )
                    
                    nuevo_nombre = "datos.json"
                    ruta_nuevo_archivo = os.path.join("BD_USO", nuevo_nombre)
                        
                    # Para que evitar el error al no poder crear un archivo ya existente
                    if os.path.exists(ruta_nuevo_archivo):
                        os.remove(ruta_nuevo_archivo)
                        
                    # Se renombra el archivo seleccionado como 'datos.json'
                    os.rename(ruta_archivo_seleccionado, ruta_nuevo_archivo)
                    message_dialog(
                        title='Archivo renombrado',
                        text=f'Archivo renombrado a: {nuevo_nombre}'
                    ).run()
                

                    
            except json.JSONDecodeError:
                message_dialog(
                    title='Error',
                    text='El archivo seleccionado no es un archivo JSON válido.'
                ).run()
                
                
                os.remove(ruta_archivo_seleccionado)
                message_dialog(
                    title='Archivo eliminado',
                    text=f'El archivo {archivo_seleccionado} ha sido eliminado.'
                ).run()
               
        else:
            message_dialog(
                title='Error',
                text='No se seleccionó ningún archivo.'
            )
      

    def ordenar_por_codigo(self):
        '''
        Método que ordena la lista de productos de venta por código.
        '''
        self.__lista_productos_venta.sort(key=lambda producto: producto.get_codigo())

    
    
    def buscar_producto_por_codigo(self, codigo):
        """
        Metodo que busca un producto en la lista productos_venta por su código,
        para realizar una compra o eliminar un producto.
        
        args:
            codigo: int
            
        return:
            producto: Producto (si el codigo coincide con el de un producto)
            None: si el codigo no coincide con el de un producto
        """
        for producto in self.get_lista_productos_venta():
            if producto.get_codigo() == codigo:
                return producto
        return None
    

    def modificar_inventario(self, codigo, cantidad_a_comprar):
        '''
        Metodo que modifica el inventario de un producto en la lista de productos de venta.
        
        Args:
            codigo (str): Código del producto a comprar.
            cantidad_a_comprar (int): Cantidad de productos a comprar.
        
        Returns:
            bool: True si la compra se realizó correctamente, False si no se pudo realizar la compra.
        '''
        producto = self.buscar_producto_por_codigo(codigo)
        if producto and producto.get_inventario() >= cantidad_a_comprar > 0:
            producto.set_inventario(producto.get_inventario() - cantidad_a_comprar) 
            self.grabar_archivo_producto()
            return True
        return False
    
    def eliminar_sin_existencia(self):
        '''
        Este método elimina los productos de la lista de productos de venta que tengan 
        un inventario igual a 0.
        
        Args:
            self: instancia de la clase ProductosVenta
            
        Returns:
            None
        '''
        self.__lista_productos_venta = [
            producto for producto in self.__lista_productos_venta if producto.get_inventario() > 0
        ]

        self.grabar_archivo_producto()


class ProductoCarrito():
    '''
    Clase ProductoCarrito que permite gestionar los productos de
    compra, en ella se pueden agregar, eliminar y modificar productos.
    '''
    def __init__(self, productos_venta ,codigo='', nombre='',precio=0.00, inventario= 0 , subtotal= 0.00, lista_compra= None):
        '''
        Método constructor de la clase ProductoCarrito.
        
        Args:
            productos_venta (ProductosVenta): Instancia de la clase ProductosVenta.
            codigo (str): Código del producto.
            nombre (str): Nombre del producto.
            precio (float): Precio del producto.
            inventario (int): Cantidad de productos en el inventario.
            subtotal (float): Subtotal de la compra.
            lista_compra (list): Lista de productos de compra.
        '''
        self.productos_venta= productos_venta
        self.__codigo = codigo
        self.__nombre = nombre
        self.__precio = precio
        self.__inventario = inventario
        self.__subtotal = subtotal
        if lista_compra is None:
            lista_compra= []
        self.__lista_compra = lista_compra
        
    
    def get_codigo(self):
        '''
        Método que obtiene el código de un producto.
        
        Returns:
            str: El código de un producto.
        '''
        return self.__codigo
    
    def set_codigo(self, codigo):
        '''
        Método que establece el código de un producto.
        '''
        self.__codigo = codigo
    
    
    def get_nombre(self):
        '''
        Método que obtiene el nombre de un producto.
        
        Returns:
            str: El nombre de un producto.
        '''
        return self.__nombre
    
    def set_nombre(self, nombre):
        '''
        Método que establece el nombre de un producto.
        '''
        self.__nombre = nombre
    
    
    def get_precio(self):
        '''
        Método que obtiene el precio de un producto.
        
        Returns:
            float: El precio de un producto.
        '''
        return self.__precio
    
    def set_precio(self, precio):
        '''
        Método que establece el precio de un producto.
        '''
        self.__precio = precio
    
    
    def get_cantidad(self):
        '''
        Método que obtiene la cantidad de productos en el inventario.
        
        Returns:
            int: La cantidad de productos en el inventario.
        '''
        return self.__inventario
    
    def set_cantidad(self, inventario):
        '''
        Método que establece la cantidad de productos en el inventario.
        '''
        self.__inventario = inventario
    
    def get_subtotal(self):
        '''
        Metodo que obtiene el subtotal de la compra.
        
        Returns:
            float: El subtotal de la compra.
        '''
        return self.__subtotal
    
    def set_subtotal(self, subtotal):
        '''
        Método que establece el subtotal de la compra.
        '''
        self.__subtotal = subtotal
        
    def get_lista_compra(self):
        '''
        Método que obtiene la lista de productos de compra.
        
        Returns:
            list: La lista de productos de compra.
        '''
        return self.__lista_compra
    
    def set_lista_compra(self,lista_compra):
        '''
        Método que establece la lista de productos de compra.
        '''
        self.__lista_compra = lista_compra
    
    
    def digitar_dato(self, mensaje):
        '''
        Método que solicita al usuario que digite un dato.
        
        Returns:
            str: El dato ingresado por el usuario.
        '''
        dato= input(mensaje)
        return dato
    
    def verificar_code(self, codigo):
        '''
        Metodo que verifica si un producto ya está en la lista de productos de venta.
        
        Args:
            codigo (str): Código del producto a comprar.
        
        Returns:
            bool: True si el producto ya está en la lista de productos de venta, False si no está.
        '''
        for pr in self.productos_venta.get_lista_productos_venta():
            if pr.get_codigo() == codigo:
                return True
        return False
    
    def actualizar_productos_venta(self):
        '''
        Metodo que actualiza la lista de productos de venta.
        '''
        self.productos_venta = self.productos_venta.get_lista_productos_venta()
    
    def mostrar_productos_disponibles(self):
        '''
        Método que muestra los productos disponibles para la compra.
        
        Returns:
            str: Tabla con los productos disponibles para la compra.
        '''
        tabla = """
╔════════════════════════════════════════════════════════════════════════════════════════════════╗
║                               PRODUCTOS DISPONIBLES PARA COMPRA                                ║
╠════════════════════╦══════════════════════════════════════╦═════════════════╦══════════════════╣
║ CODIGO PRODUCTO    ║          DESCRIPCION                 ║  INVENTARIO     ║  PRECIO DE VENTA ║
╠════════════════════╬══════════════════════════════════════╬═════════════════╬══════════════════╣
"""
        for producto in self.productos_venta.get_lista_productos_venta():
            tabla += '║ {0:<18} ║ {1:<36} ║ {2:<15} ║ {3:<16.2f} ║\n'.format(
                producto.get_codigo(),
                producto.get_descripcion(),
                producto.get_inventario(),
                producto.get_precio()
            )
        tabla += "╚════════════════════╩══════════════════════════════════════╩═════════════════╩══════════════════╝\n"
        return tabla
    
    
    
    def verificar_producto_en_carrito(self,codigo):
        '''
        Método que verifica si un producto ya está en el carrito de compras.
        
        Args:
            codigo (str): Código del producto a comprar.
        
        Returns:
            dict: El producto en forma de diccionario si está en el carrito de compras, None si no está.
        
        '''
        for item in self.__lista_compra:
                    if item['codigo'] == codigo:
                        # Producto ya está en el carrito
                        message_dialog(
                            title='Producto ya en el carrito',
                            text=f"El producto '{item['nombre']}' ya está en el carrito con una cantidad de {item['cantidad']}."
                        ).run()
                        
                        return item
                    return None
                        
    def modificar_cantidad_producto(self, codigo): 
        '''
        Método que modifica la cantidad de un producto en el carrito de compras.
        
        Args:
            codigo (str): Código del producto a modificar.
        
        Returns:
            None
        
        '''
        
        item = self.buscar_producto_en_carrito(codigo)
        if not item:
            message_dialog(
                title='Error',
                text=f"El producto con el código '{codigo}' no se encuentra en el carrito."
            ).run()
            
            return False
        
        
        

    def verificar_producto_en_lista(self):  
        '''
        Método que verifica si un producto ya está en la lista de compras.
        
        Returns:
            dict: El producto en forma de diccionario si está en la lista de compras, None si no está.
    
        '''
        
        while True:
            codigo= self.dato_codigo_producto()
            item = self.verificar_producto_en_carrito(codigo)
            if item:
                self.modificar_cantidad_producto(codigo)
                return None
            
            producto= self.productos_venta.buscar_producto_por_codigo(codigo)
            if not producto:
                message_dialog(
                    title='Error',
                    text='El código no existe. Ingrese un código válido.'
                ).run()
            else:
                return producto
        
    def buscar_producto_en_carrito(self, codigo):
        """
        Busca un producto en el carrito de compras por su código.
        
        Args:
            codigo (int): El código del producto a buscar.
        
        Returns:
            dict: El producto en forma de diccionario si está en el carrito, None si no está.
        """
        
        # Busca en la lista de compras el producto con el código dado
        for item in self.__lista_compra:
            if item['codigo'] == codigo:
                return item
        return None       
    
    
    def dato_codigo_producto(self):
        '''
        Método que solicita al usuario el código del producto a comprar.
        
        Returns:
            str: El código del producto a comprar.
        
        '''
        
        tabla= self.productos_venta.existencia_productos()
        carrito= """ 
                                                             ╔═
                                                    ╔════════╣
                                                    ║▓▓▓▓▓▓▓▓║ 
                                                    ║▓▓▓▓▓▓▓▓║
                                                    ◯════════◯
                       """     
        
        while True:
                try:
                    
    
                    code= input_dialog(
                        title='Código del producto',
                        text= carrito + tabla +'\nDIGITE EL CÓDIGO DEL PRODUCTO  A COMPRAR (máximo 7 dígitos):',
                        ok_text='Aceptar',
                        cancel_text='Salir'
                    ).run()
                    
                    
                    if code == None:
                        ir_al_menu()
                    
                    
                    if not code.isdigit():
                        raise ValueError ('El código debe ser numérico. Por favor, intente de nuevo.                     ')
                    
                    if len(code) > 7:
                        raise ValueError ('El código debe tener máximo 7 dígitos. Por favor, intente de nuevo.           ')
                    
                    code = code.zfill(7)
                    
                    if not self.verificar_code(code):
                        raise ValueError ('El código no existe. Ingrese un código diferente. Por favor, intente de nuevo.')
                    
                    os.system('cls')
                    break
                    
                    
                except ValueError as ve:
                    error = f"Error: {ve}"
                    os.system('cls')
                    message_dialog(
                        title='Error',
                        text=error
                    ).run()
                    
        return code
    
    def validar_inventario(self, producto):
        '''
        Método que solicita al usuario la cantidad de productos en el inventario.
        
        Args:
            producto (Producto): Producto a comprar.
        
        Returns:
            int: La cantidad de productos en el inventario.
        '''
        
        
        while True:
                try:
                    cantidad= input_dialog(
                        title='Cantidad de productos',
                        text=f"Producto: {producto.get_descripcion()}\nInventario disponible: {producto.get_inventario()}\n\nDIGITE LA CANTIDAD DE PRODUCTOS EN INVENTARIO (máximo 15 dígitos):",
                        ok_text='Aceptar',
                        cancel_text='Salir'
                    ).run()
                    
                    if cantidad == None:
                        self.__lista_compra.clear()
                        ir_al_menu()
                    
                    if not cantidad.isdigit():
                        raise ValueError ('La cantidad de productos debe ser un dato numérico. Por favor, intente de nuevo. ')
                    
                    if len(cantidad) > 15:
                        raise ValueError ('La contidad de productos debe tener máximo 15 dígitos. Por favor, intente de nuevo.                          ')
                    cantidad_int = int(cantidad)
                    if int(cantidad) < 1:
                        raise ValueError ('La cantidad de productos en el inventario debe ser mayor a 0. Por favor, intente de nuevo.        ')
                    if cantidad_int > producto.get_inventario():
                        raise ValueError ('La cantidad de productos en el inventario no puede ser mayor a la cantidad de productos en inventario. Por favor, intente de nuevo. ') 
                    os.system('cls')
                    break
                    
                    
                except ValueError as ve:
                    error = f"Error: {ve}"
                    os.system('cls')
                    message_dialog(
                        title='Error',
                        text=error
                    ).run()
              
        return int(cantidad)
  
    
    
    
    def agregar_producto_carrito(self, producto,cantidad_a_comprar):
        '''
        Método que agrega un producto al carrito de compras.
        
        Args:
            producto (Producto): Producto a comprar.
            cantidad_a_comprar (int): Cantidad de productos a comprar.
        
        Returns:
            bool: True si el producto se agrega al carrito, False si no se agrega,
            o si este ya está en el carrito.
        '''
        for item in self.__lista_compra:
            if item['codigo'] == producto.get_codigo():
                
                message_dialog(
                    title="Producto ya en el carrito",
                    text=f"El producto {producto.get_descripcion()} ya está en el carrito."
                ).run()
                return False
        if 0 < cantidad_a_comprar <= producto.get_inventario():
            subtotal = cantidad_a_comprar * producto.get_precio()
            
            # Agregar el producto al carrito
            self.__lista_compra.append({
                'codigo': producto.get_codigo(),
                'nombre': producto.get_descripcion(),
                'precio': producto.get_precio(),
                'cantidad': cantidad_a_comprar,
                'subtotal': subtotal
            })
            message_dialog(
                title='Producto agregado',
                text=f"Producto agregado al carrito: {producto.get_descripcion()}"
            ).run()
            return True
        else:
            message_dialog(
                title='Error',
                text='Cantidad inválida. Debe ser mayor que 0 y no superar el inventario disponible.'
            ).run()
            
            return False
    

    def calcular_total_compra(self):
        '''
        Método que calcula el total de la compra.
        
        Returns:
            float: Total de la compra.
        
        Args:
            lista_compra (list): Lista de productos en el carrito.
        '''
        total = sum(item['subtotal'] for item in self.__lista_compra)
        return total
    
    
    def resumen_compra(self):
        """
        Muestra un resumen de los productos en el carrito y el total de la compra.
        
        Returns:
            str: Una tabla con el resumen de la compra.
        """
        
        tabla = """
╔═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
║                                                 RESUMEN DE COMPRA                                                 ║
╠════════════════════╦══════════════════════════════════════╦═════════════════╦══════════════════╦══════════════════╣
║ CODIGO PRODUCTO    ║          DESCRIPCION                 ║  CANTIDAD       ║  PRECIO DE VENTA ║  SUBTOTAL        ║
╠════════════════════╬══════════════════════════════════════╬═════════════════╬══════════════════╬══════════════════╣
"""
        for item in self.__lista_compra:
            tabla += '║ {0:<18} ║ {1:<36} ║ {2:<15} ║ ${3:<15.2f} ║ ${4:<15.2f} ║\n'.format(
                item['codigo'],
                item['nombre'],
                item['cantidad'],
                item['precio'],
                item['subtotal']
                )
        tabla += "╠════════════════════╩══════════════════════════════════════╩═════════════════╩══════════════════╩══════════════════╣\n"
        tabla += "║ TOTAL DE LA COMPRA: ${0:<92.2f} ║\n".format(self.calcular_total_compra())
        tabla += "╚═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝"                                               
    
        return tabla
    
    def mostrar_resumen_compra (self):
        '''
        Metodo que muestra un resumen de la compra.
        
        Returns:
            bool: Si es True, se agrega o edita un producto en el carrito. Si es False, se finaliza la compra.
        '''
        opcion= message_dialog(
            title='Resumen de la compra',
            text= self.resumen_compra(),
        ).run()
        return opcion

    """ def agregar_o_editar_producto(self,opcion):
        '''
        Método que permite agregar un producto al carrito o editar la cantidad de un producto en el carrito.
        
        Args:
            opcion (bool): Si es True, se agrega un producto al carrito. Si es False, se edita la cantidad de un producto en el carrito.
            
        Returns:
            None
        '''
        
        if opcion:
            agregar_o_editar= button_dialog(
                title='Agregar o Editar',
                text='¿Desea agregar un producto o editar la cantidad de algún producto?',
                buttons=[
                    ('Agregar', True),
                    ('Editar', False)
                ]
            ).run()
            if agregar_o_editar == False:
                # Mostrar un diálogo de lista radial con los productos en el carrito.
                editar= radiolist_dialog(
                    title='Editar producto',
                    text='Seleccione el producto que desea editar:',
                    values=[(item['nombre'], f"nombre: {item['nombre']}, Cantidad: {item['cantidad']}, Precio: {item['precio']}, Subtotal: {item['subtotal']}") for item in self.__lista_compra],
                    ok_text='Aceptar',
                    cancel_text='Salir'
                ).run()
                
                if editar == None:
                    # Si el usuario cancela la edición, retorna a mostrar el resumen de la compra.
                    return self.mostrar_resumen_compra()
                
                else:
                    '''
                    Variable "producto_seleccionado".
                    Buscar el producto seleccionado en la lista de compras por su nombre usando next y
                    un generador de lista por comprensión con un condicional if para editar la cantidad 
                    del producto con el nombre seleccionado en la lista de compras.
                    '''
                    producto_seleccionado = next((item for item in self.__lista_compra if item['nombre'] == editar), None) 
                    
                    if producto_seleccionado:
                        
                        # Guardar la cantidad actual del producto seleccionado.
                        cantidad_actual = producto_seleccionado['cantidad']
                        
                        # Buscar el producto original en la lista de productos de venta por su código.
                        producto_original = next((prod for prod in self.productos_venta.get_lista_productos_venta() if prod.get_codigo() == producto_seleccionado['codigo']), None)
                        
                        if producto_original:
                            
                            # Llamar al método "cambiar_inventario" para cambiar la cantidad del producto en el carrito.
                            nueva_cantidad = self.cambiar_inventario(producto_original,cantidad_actual )
                            
                            # Actualizar la cantidad y el subtotal del producto en el carrito.
                            producto_seleccionado['cantidad'] = nueva_cantidad  
                            
                            # Calcular el nuevo subtotal del producto en el carrito.
                            producto_seleccionado['subtotal'] = producto_seleccionado['precio'] * nueva_cantidad
                            
                            # Mostrar un mensaje de diálogo con el producto actualizado.
                            message_dialog(
                                title='Producto actualizado',
                                text=f"Producto '{producto_seleccionado['nombre']}' actualizado con cantidad de {producto_seleccionado['cantidad']}."
                            ).run()
                            return self.mostrar_resumen_compra()
            if agregar_o_editar == True:
            
                
                Si el usuario desea agregar un nuevo producto, se llama al método 
                "proceso_de_compra".
                
                self.proceso_de_compra() """ 

    """ 
    def cambiar_inventario(self, producto, cantidad_actual):
        '''
        Método que permite cambiar la cantidad de un producto en el carrito de compra.
        
        Args:
            producto (Producto): El producto a cambiar la cantidad.
            
        Returns:
            int: La nueva cantidad del producto.
            
        Raises:
            ValueError: Si la cantidad no es un número entero o si la cantidad es menor o igual a 0.
            ValueError: Si la cantidad es mayor que el inventario del producto.
            ValueError: Si la cantidad es mayor a 15 dígitos.
            ValueError: Si la cantidad no es un número entero.

        '''
        

        muestra=    "╔════════════════════════════════════════════════\n"
        muestra += f"║ PRODUCTO: {producto.get_descripcion()} \n"
        muestra += f"║ INVENTARIO DISPONIBLE: {producto.get_inventario()} \n"
        muestra += f"║ CANTIDAD ACTUAL: {cantidad_actual} \n"
        muestra +=  "╚════════════════════════════════════════════════\n "
        
        
        
        # Mientras sea verdadero el bucle, se ejecuta el bloque de código.
        while True:
    
                try:
                    
                    # Mostrar un cuadro de diálogo de entrada con la cantidad de productos en el inventario.
                    cantidad= input_dialog(
                        title='Cantidad de productos',
                        text= muestra+"\nDIGITE LA CANTIDAD DE PRODUCTOS EN INVENTARIO (máximo 15 dígitos):",
                        ok_text='Aceptar',
                        cancel_text='Salir'
                    ).run()
                    
                    # Si el usuario cancela la edición, se muestra el resumen de la compra.
                    if cantidad == None:
                       return self.mostrar_resumen_compra()
                    
                    # Si la cantidad no es un número entero, se muestra un mensaje de error.
                    if not cantidad.isdigit():
                        raise ValueError ('La cantidad de productos debe ser un dato numérico. Por favor, intente de nuevo. ')
                    
                    # Si la cantidad es mayor a 15 dígitos, se muestra un mensaje de error.
                    if len(cantidad) > 15:
                        raise ValueError ('La contidad de productos debe tener máximo 15 dígitos. Por favor, intente de nuevo.                          ')
                    cantidad_int = int(cantidad)
                    
                    # Si la cantidad es menor o igual a 0, se muestra un mensaje de error.
                    if int(cantidad) <= 0:
                        raise ValueError ('La cantidad de productos en el inventario debe ser mayor a 0. Por favor, intente de nuevo.        ')
                    
                    # Si la cantidad es mayor que el inventario del producto, se muestra un mensaje de error.
                    if cantidad_int > producto.get_inventario():
                        raise ValueError ('La cantidad de productos en el inventario no puede ser mayor a la cantidad de productos en inventario. Por favor, intente de nuevo. ') 
                    os.system('cls')
                    break
                    
                # Capturar las excepciones de los errores y mostrar un mensaje de error.   
                except ValueError as ve:
                    error = f"Error: {ve}"
                    os.system('cls')
                    message_dialog(
                        title='Error',
                        text=error
                    ).run()
        
        # Retornar la cantidad de productos en el inventario.    
        return int(cantidad) """
    
    def proceso_de_compra(self):
        '''
        Metodo  que permite agregar productos al carrito de compra, atraves  de la verificación de 
        la existencia  del producto en la lista de productos, la cantidad, y  la actualización del 
        inventario. Si  se agrega un  producto al carrito, se muestra un resumen de la compra y se
        permite agregar o editar la cantidad de los productos en el carrito.Al finalizar la compra,
        se muestra un mensaje de agradecimiento.
        
        Args:
            self: La instancia de la clase ProductoCarrito.
        
        Returns:
            None: No retorna nada.
        
        '''
       
       
        
        while True:
            
            producto= self.verificar_producto_en_lista() 
            
            if producto is None:
                continue
            
            cantidad= self.validar_inventario(producto)
            self.agregar_producto_carrito(producto,cantidad)
            
                

            otra_compra= button_dialog(
                title='Agregar otro producto',
                text='¿Desea agregar otro producto al carrito?\n\n'+self.resumen_compra(),
                buttons=[
                    ('Sí', True),
                    ('No', False)
                ]
            ).run()
            
            if otra_compra != True:
                break
            
            
            
        self.mostrar_resumen_compra()
        
        message_dialog(
            title='Compra finalizada',
            text='Gracias por su compra, dirigete a la opción "IMPRIMIR FACTURA"\n    en el menu principalpara para finalizar la compra.'
                  
        ).run()
    
    def limpiar_carrito(self):
        '''
        Método que limpia el carrito de compras.
        '''
        self.__lista_compra.clear()     


class CarritoCompra():
    '''
    Clase que representa un carrito de compras, para realizar la factura de compras.
    
    Attributes:
        nombre (str): El nombre del cliente.
        apellido (str): El apellido del cliente.
        correo (str): El correo del cliente.
        telefono (str): El teléfono del cliente.
        direccion (str): La dirección del cliente.
        cedula (int): La cédula del cliente.
        producto_carrito (ProductoCarrito): La instancia de la clase ProductoCarrito.

        
    
    '''
    def __init__(self,producto_carrito,nombre='',apellido= '',correo= " ",telefono= '',direccion="", cedula=''):
        '''
            Método constructor de la clase CarritoCompra.
            
            Args:
                nombre (str): El nombre del cliente.
                apellido (str): El apellido del cliente.
                correo (str): El correo del cliente.
                telefono (str): El teléfono del cliente.
                direccion (str): La dirección del cliente.
                cedula (int): La cédula del cliente.
                producto_carrito (ProductoCarrito): La instancia de la clase ProductoCarrito.
        
        '''
        self.__nombre= nombre
        self.__apellido= apellido
        self.__correo= correo
        self.__telefono= telefono
        self.__direccion= direccion
        self.__cedula= cedula
        self.producto_carrito= producto_carrito
    
    
    def get_nombre(self):
        '''
        Método get que retorna el nombre del cliente.
        '''
        return self.__nombre
    
    
    def set_nombre(self, nombre):
        '''
        Metodo set que asigna el nombre del cliente.
        '''
        self.__nombre = nombre
        
        
    def get_apellido(self):
        '''
        Método get que retorna el apellido del cliente.
        '''
        return self.__apellido
    
    
    def set_apellido(self, apellido):
        '''
        Metodo set que asigna el apellido del cliente.
        '''
        self.__apellido = apellido
    
    
    def get_correo(self):
        '''
        Método get que retorna el correo del cliente.
        '''
        return self.__correo

    
    def set_correo(self, correo):
        '''
        Metodo set que asigna el correo del cliente.
        '''
        self.__correo = correo
    
    
    def get_telefono(self):
        '''
        Método get que retorna el teléfono del cliente.
        '''
        return self.__telefono
    
    
    def set_telefono(self, telefono):
        '''
        Metodo set que asigna el teléfono del cliente.
        '''
        self.__telefono = telefono
    
    
    def get_direccion(self):
        '''
        Método get que retorna la dirección del cliente.
        '''
        return self.__direccion
    
    
    def set_direccion(self, direccion):
        '''
        Metodo set que asigna la dirección del cliente.
        '''
        self.__direccion = direccion
    
    
    def get_cedula(self):
        """ 
        Metodo get que retorna la cédula del cliente. 
        """
        return self.__cedula
    
    
    def set_cedula(self, cedula):
        '''
        Metodo set que asigna la cédula del cliente.
        '''
        self.__cedula = cedula
    
    
    def validar_nombre(self):
        '''
        Metodo que valida el nombre del cliente y retorna el nombre.
        
        Args:
            self: La instancia de la clase CarritoCompra.
            
        Returns:
            str: El nombre del cliente.
                
        Raises:
            ValueError: Si el nombre no es una cadena de texto.
            ValueError: Si el nombre está vacío o contiene solo espacios en blanco.
            ValueError: Si el nombre tiene más de 36 caracteres.
            ValueError: Si el nombre no contiene solo letras (incluidas letras con tilde y ñ).
                    '''

        resumen= self.producto_carrito.resumen_compra()
        
        while True:
            try:
                nombre= input_dialog(
                    title=' Nombre',
                    text=f'{resumen}\n\nDIGITE SU NOMBRE :',
                    ok_text='Aceptar',
                    style= style_9
                ).run()
                
                if nombre== None:
                    ir_al_menu()
                
                
                if not isinstance(nombre, str):
                    raise ValueError("El Nombre debe ser una cadena de texto.")
                
                if not nombre.strip():
                    raise ValueError("El nombre no puede estar vacía o contener solo espacios en blanco.       ")
                
                if len(str(nombre)) > 36:
                    raise ValueError ('El no debe tener máximo 36 caracteres. Por favor, intente de nuevo.   ')
                
                # Verificación de que solo contenga letras (incluidas letras con tilde y ñ)
                if not re.match(r'^[A-Za-záéíóúüñÁÉÍÓÚÜ\s]+$', nombre):
                    raise ValueError("El nombre solo puede contener letras del abecedario, incluyendo tildes y la letra 'ñ'.")
                
                nombre = nombre.capitalize()
                
                
                os.system('cls')
                break

            except ValueError as ve:
                error_message = f"Error: {ve}"
                os.system('cls' if os.name == 'nt' else 'clear')
                
                
                message_dialog(
                    title='Error',
                    text=error_message
                ).run()
        return  nombre
    
    def validar_apellido(self):
        '''
        Metodo que valida el apellido del cliente y retorna el apellido.
        
        Args:
            self: La instancia de la clase CarritoCompra.
            
        Returns:
            str: El apellido del cliente.
            
        Raises:
            ValueError: Si el apellido no es una cadena de texto.
            ValueError: Si el apellido está vacío o contiene solo espacios en blanco.
            ValueError: Si el apellido tiene más de 36 caracteres.
            ValueError: Si el apellido no contiene solo letras (incluidas letras con tilde y ñ).
        '''
        
        resumen= self.producto_carrito.resumen_compra()
        while True:
            try:
                apellido= input_dialog(
                    title='Apellido',
                    text=  f'{resumen} +\n\nDIGITE SU APELLIDO :',
                    ok_text='Aceptar',
                    cancel_text= 'Cancelar',
                    style= style_9
                ).run()
                
                if apellido== None:
                    ir_al_menu()
                
                
                if not isinstance(apellido, str):
                    raise ValueError("El apellido debe ser una cadena de texto.")
                
                if not apellido.strip():
                    raise ValueError("El apellido no puede estar vacio o contener solo espacios en blanco.       ")
                
                if len(str(apellido)) > 36:
                    raise ValueError ('El apellido debe tener máximo 36 caracteres. Por favor, intente de nuevo.   ')
                
                # Verificación de que solo contenga letras (incluidas letras con tilde y ñ)
                if not re.match(r'^[A-Za-záéíóúüñÁÉÍÓÚÜ\s]+$', apellido):
                    raise ValueError("El apellido solo puede contener letras del abecedario, incluyendo tildes y la letra 'ñ'." )
                
                apellido = apellido.capitalize()
                
                
                os.system('cls')
                break

            except ValueError as ve:
                error_message = f"Error: {ve}"
                os.system('cls' if os.name == 'nt' else 'clear')
                
                
                message_dialog(
                    title='Error',
                    text=error_message
                ).run()
        return apellido
    
    def validar_correo(self):
        while True:
            try:
                correo= input_dialog(
                    title='Correo',
                    text=  '\nDIGITE SU CORREO :',
                    ok_text='Aceptar',
                    style= style_9
                ).run()
                
                if correo== None:
                    ir_al_menu()
                
                if not isinstance(correo, str):
                    raise ValueError("El correo debe ser una cadena de texto.")
                
                if not correo.strip():
                    raise ValueError("El correo no puede estar vacio o contener solo espacios en blanco.       ")
                
                if len(str(correo)) > 36:
                    raise ValueError ('El correo debe tener máximo 36 caracteres. Por favor, intente de nuevo.   ')
                
                patron_correo = r'^[\S]+@[\S]+\.\w{2,}$'
                if not re.match(patron_correo, correo):
                    raise ValueError("El correo no tiene un formato válido. Debe contener '@' y un dominio válido.")
                
                os.system('cls')
                break

            except ValueError as ve:
                error_message = f"Error: {ve}"
                os.system('cls' if os.name == 'nt' else 'clear')
                
                
                message_dialog(
                    title='Error',
                    text=error_message
                ).run()
        return correo
    
    def validar_telefono(self):
        '''
        Método que valida el número telefónico del cliente y retorna el número telefónico.
        
        Args:
            self: La instancia de la clase CarritoCompra.
        
        Returns:
            str: El número telefónico del cliente.
        '''
        while True:
                try:
                    
                    resumen= self.producto_carrito.resumen_compra()
                    telefono= input_dialog(
                        title='Teléfono',
                        text=  f'{resumen}\n\nDIGITE SU NÚMERO TELEFONICO (10 dígitos):',          
                        ok_text='Aceptar',
                        cancel_text= 'Cancelar',
                        style= styles
                    ).run()
                    
                    if telefono== None:
                        ir_al_menu() 
                        
            
                    
                    if not telefono.isdigit():
                        raise ValueError ('El número telefono debe ser numérico. Por favor, intente de nuevo.                     ')
                    
                    if len(telefono) != 10:
                        raise ValueError ('El número telefono debe tener 10 dígitos. Por favor, intente de nuevo.       ')
                    
                    if not telefono.startswith('3'):
                        raise ValueError('El número telefónico debe comenzar con el dígito 3. Por favor, intente de nuevo.')
                    
                    telefono_formateado = f'({telefono[:3]}) {telefono[3:6]}-{telefono[6:]}'
                    
                    
                    os.system('cls')
    
                    break

                except ValueError as ve:
                    error_message = f"Error: {ve}"
                    os.system('cls' if os.name == 'nt' else 'clear')
                    
                    message_dialog(
                        title='Error',
                        text=error_message
                    ).run()
                                
        return telefono_formateado
    

    def validar_direccion(self):
        '''
        Método que valida la dirección del cliente y retorna la dirección.
        
        Args:
            self: La instancia de la clase CarritoCompra.
            
        Returns:
            str: La dirección del cliente.
        '''
        
        resumen= self.producto_carrito.resumen_compra()
        while True:
            try:
                direccion = input_dialog(
                    title='Dirección',
                    text=f'{resumen}\n\nDIGITE SU DIRECCIÓN:',
                    ok_text='Aceptar',
                    cancel_text='Cancelar',
                    style=styles
                ).run()

                if direccion is None:
                    ir_al_menu()

                # Definir patrones de expresiones regulares
                patrones = [
                    r'^(CRA|CALLE|AV)\s?\d+[a-zA-Z]?\s?#\s?\d+[a-zA-Z]?(-\d+)?$',  # Carrera o Calle o Avenida con número
                    r'^(TRANSVERSAL|DIAGONAL|CIRCUNVALAR)\s?\d+[a-zA-Z]?\s?#\s?\d+[a-zA-Z]?(-\d+)?$',  # Transversales, diagonales o circunvalares
                    r'^[A-Za-z\s]+\s?\d+[a-zA-Z]?\s?#\s?\d+[a-zA-Z]?(-\d+)?$',  # Nombres propios de calles
                    r'^(VEREDA)\s[A-Za-z\s]+,\s?[A-Za-z\s]+,\s?[A-Za-z\s]+$',# Direcciones en áreas rurales
                    r'^[A-Za-z\s]+,\s?LOCAL\s\d+,\s?TORRE\s[A-Z]$',  # Direcciones en centros comerciales
                ]

                # Convertir la dirección a mayúsculas
                direccion = direccion.upper()
                
                # Verificar si la dirección coincide con algún patrón
                if not any(re.match(patron, direccion) for patron in patrones):
                    raise ValueError('La dirección ingresada no es válida. Por favor, intente de nuevo.')

                os.system('cls')
                break

            except ValueError as ve:
                error_message = f"Error: {ve}"
                os.system('cls' if os.name == 'nt' else 'clear')

                message_dialog(
                    title='Error',
                    text=error_message
                ).run()

        return direccion
    
    def validar_cedula(self):
        '''
        Método que valida la cédula del cliente y retorna la cédula.
        
        Args:
            self: La instancia de la clase CarritoCompra.
        
        Returns:
            str: La cédula del cliente.
        '''
        while True:
            try:
                cedula = input_dialog(
                    title='Cédula',
                    text= '\nDIGITE SU NÚMERO DE CÉDULA (6 a 10 dígitos):',
                    ok_text='Aceptar',
                    cancel_text='Cancelar',
                    style=styles
                ).run()

                if cedula is None:
                    ir_al_menu()

                # Verificar que la cédula sea numérica
                if not cedula.isdigit():
                    raise ValueError('La cédula debe ser numérica. Por favor, intente de nuevo.')

                # Verificar la longitud de la cédula
                if len(cedula) < 6 or len(cedula) > 10:
                    raise ValueError('La cédula debe tener entre 6 y 10 dígitos. Por favor, intente de nuevo.')

                os.system('cls')
                break

            except ValueError as ve:
                error_message = f"Error: {ve}"
                os.system('cls' if os.name == 'nt' else 'clear')

                message_dialog(
                    title='Error',
                    text=error_message
                ).run()

        return cedula


    def mostrar_datos(self):
        '''
        Método que muestra los datos del cliente.
        
        Args:
            self: La instancia de la clase CarritoCompra.
        
        Returns:
            None
        '''
        
        Nombre= self.set_nombre(self.validar_nombre())
        Apellido= self.set_apellido(self.validar_apellido())
        Correo= self.set_correo(self.validar_correo())
        Telefono= self.set_telefono(self.validar_telefono())
        Direccion= self.set_direccion(self.validar_direccion())
        Cedula= self.set_cedula(self.validar_cedula())
        
        
        Nombre
        Apellido
        Correo
        Telefono
        Direccion
        Cedula
            

    
    def generar_factura_pdf(self):
        '''
        Método que genera una factura de compra en formato PDF.
        
        Args:
            self: La instancia de la clase CarritoCompra.
        
        Returns:
            None
        '''
        pdf = PDF()

        # Obtener la fecha actual
        fecha_actual = datetime.now().strftime('%d-%m-%Y_%Hh.%Mm.%Ss')
        
        # Definir la ruta del archivo PDF
        nombre_pdf = f"Factura_de_Compra_{fecha_actual}.pdf"
        ruta_pdf = os.path.join("FACTURAS", nombre_pdf)
        
        # Añadir una página
        pdf.add_page()
        
        # Datos del cliente
        pdf.datos_cliente(self.get_nombre(), self.get_apellido(), self.get_correo(), self.get_telefono(), self.get_direccion(), self.get_cedula())

        # Tabla de productos
        lista_compra = self.producto_carrito.get_lista_compra()
        pdf.tabla_productos(lista_compra)

        # Total de la compra
        total = self.producto_carrito.calcular_total_compra()
        pdf.total_compra(total)

        # Guardar el PDF
        pdf.output(ruta_pdf)
        
        enviar_por_pdf(ruta_pdf,self.get_nombre(),self.get_correo())
        self.producto_carrito.limpiar_carrito()


    
class PDF(FPDF):
    '''
    Clase que representa una factura de compra en formato PDF.
    
    Attributes:
        FPDF: Clase base para la creación de un documento PDF.
    
    Methods:
        header: Encabezado de la factura.
        footer: Pie de página de la factura.
        datos_cliente: Muestra los datos del cliente.
        tabla_productos: Crea la tabla de productos.
        total_compra: Muestra el total de la compra.
    
    Methods inherited from FPDF:
        add_page: Añade una página al documento.
        set_font: Establece la fuente para el texto.
        cell: Agrega una celda al documento.
        ln: Salto de línea.
        output: Guarda o muestra el documento.

    '''
    
    def header(self):
        """ Encabezado de la factura """
        self.set_font('Arial', 'B', 16)  # Usar la fuente Arial en negrita
        self.cell(0, 10, 'Tienda Virtual CBA', ln=True, align='C')
        self.ln(10)

    def footer(self):
        """ Pie de página de la factura """
        self.set_y(-30)
        self.set_font('Arial', '', 10)  # Usar la fuente Arial normal
        self.cell(0, 10, 'Tienda Virtual CBA Mosquera', ln=True, align='C')
        self.cell(0, 10, 'Teléfono: 3125271551 | Correo: andres.django.pruebas@gmail.com', ln=True, align='C')
        self.cell(0, 10, 'Dirección: Kilómetro 7, Bogotá-Mosquera, SENA Centro de Biotecnología Agropecuaria | NIT: 10510788', ln=True, align='C')

    def datos_cliente(self, nombre, apellido, correo, telefono, direccion, cedula):
        """ Muestra los datos del cliente """
        self.set_font('Arial', '', 12)  # Usar la fuente Arial normal
        self.cell(0, 10, f'Cliente: {nombre} {apellido}', ln=True)
        self.cell(0, 10, f'Correo: {correo}', ln=True)
        self.cell(0, 10, f'Teléfono: {telefono}', ln=True)
        self.cell(0, 10, f'Dirección: {direccion}', ln=True)
        self.cell(0, 10, f'Cédula: {cedula}', ln=True)
        self.ln(10)

    def tabla_productos(self, lista_compra):
        """ Crea la tabla de productos """
        self.set_font('Arial', 'B', 12)  # Usar la fuente Arial en negrita
        self.cell(30, 10, 'Código', 1)
        self.cell(60, 10, 'Descripción', 1)
        self.cell(30, 10, 'Precio Unit.', 1)
        self.cell(20, 10, 'Cantidad', 1)
        self.cell(30, 10, 'Subtotal', 1)
        self.ln()

        self.set_font('Arial', '', 12)  # Usar la fuente Arial normal
        for item in lista_compra:
            self.cell(30, 10, item['codigo'], 1)
            self.cell(60, 10, item['nombre'], 1)
            self.cell(30, 10, f"${item['precio']:.2f}", 1)
            self.cell(20, 10, str(item['cantidad']), 1)
            self.cell(30, 10, f"${item['subtotal']:.2f}", 1)
            self.ln()

    def total_compra(self, total):
        """ Muestra el total de la compra """
        self.ln(5)
        self.set_font('Arial', 'B', 12)  # Usar la fuente Arial en negrita
        self.cell(0, 10, f'Total de la compra: ${total:.2f}', ln=True, align='R')



        
        
        
        