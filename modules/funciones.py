'''
SENA CBA CENTRO DE BIOTECNOLOGIA AGROPECUARIA
PROGRAMACION DE SOFTWARE

FICHA: 2877795
AUTOR: NICOLAS ANDRES ACOSTA HIGUERA
PROYECTO: TIENDA VIRTUAL (modulos/menu_principal.py)
FECHA: 2024-07-01
VERSION: 4.5.6
'''

'''
IMPORTACION DE LIBRERIAS
'''

# Importar la librería os para acceder a funcionalidades dependientes del Sistema Operativo
import os

# Importar la librería prompt_toolkit para crear interfaces de usuario en la terminal
from prompt_toolkit.shortcuts import radiolist_dialog, message_dialog, button_dialog

'''
IMPORTACION DE CLASES
'''

# Importar la clase ProductosVenta del módulo Clases y renombrarla como PV
from modules.clases.Clases import ProductosVenta as PV

# Importar la clase ProductoCarrito del módulo Clases y renombrarla como PC
from modules.clases.Clases import ProductoCarrito as PC

# Importar la clase CarritoCompra del módulo Clases y renombrarla como CC
from modules.clases.Clases import CarritoCompra as CC

# Importar el estilo de la ventana de diálogo del menú principal
from modules.styles.styles_store import styles


# Variables globales, instancias de las clases ProductosVenta, ProductoCarrito y CarritoCompra.
Pv= PV()
productos_cargados= False
Pc= PC(None)
Cc= CC(None)




def mostrar_menu(style):
    '''
    Funcion que muestra el menu principal de la tienda virtual usando la libreria prompt_toolkit.
    
    Args:
        style -- Style -- Estilo de la ventana de dialogo.
    
    Returns:
        None
    
    '''
    # Variables globales
    global productos_cargados, Pc, Pv
    
    # Mostrar el menú principal
    opcion= radiolist_dialog(
        title="===========   TIENDA VIRTUAL   ===========",
        text="\nSeleccione una opción: \n",
        values=[
            ("CARGAR LOS PRODUCTOS", "════════════════════════         CARGAR PRODUCTOS        ═══════════════════════════\n"),
            ("COPIA DE RESPALDO", "════════════════════════         COPIA DE RESPALDO       ═══════════════════════════\n"),
            ("REPARAR PRODUCTO", "════════════════════════          REPARAR PRODUCTO       ═══════════════════════════\n"),
            ("GRABAR NUEVOS PRODUCTOS", "════════════════════════      GRABAR NUEVOS PRODUCTOS    ═══════════════════════════\n"),
            ("BORRAR PRODUCTO", "════════════════════════         BORRAR  PRODUCTO        ═══════════════════════════\n"),
            ("COMPRAR PRODUCTOS", "════════════════════════        COMPRAR  PRODUCTOS       ═══════════════════════════\n"),
            ("IMPRIMIR FACTURA", "════════════════════════         IMPRIMIR FACTURA        ═══════════════════════════\n"),
        ],
        ok_text="Ok",
        cancel_text="Salir",
        style= styles
    ).run()
    
    

    # Si se selecciona la opción "CARGAR LOS PRODUCTOS" se cargan los productos.
            
    if opcion == "CARGAR LOS PRODUCTOS": 
        
        os.system('cls')
        """ 
        # Si los productos ya han sido cargados, se muestra un mensaje de error.
        if productos_cargados:
            tabla=Pv.existencia_productos()
            message_dialog(
                title= 'ERROR',
                text= 'Los productos ya han sido cargados.\n'+ tabla
            ).run()
            
        # Si los productos no han sido cargados, se cargan los productos.
        else: """
        tabla=Pv.cargar_archivo_producto() 
        os.system('cls')
        productos_cargados= True
        Pc= PC(Pv)
        message_dialog(
            title="CARGAR LOS PRODUCTOS",
            text= tabla + '\n\nProductos cargados correctamente.'
        ).run()
        
    
        
        
    # Si se selecciona la opción "COPIA DE RESPALDO" se crea una copia de respaldo.  
    elif opcion == "COPIA DE RESPALDO":
        
        # Si no se han cargado los productos, se muestra un mensaje de error.
        if not productos_cargados:
            os.system('cls')
            message_dialog(
                title="ERROR",
                text="Debe cargar los productos primero antes de hacer una copia de respaldo.\nSeleccione la opción 'CARGAR PRODUCTOS' en el menú principal."
            ).run()
        
        # Si los productos se han cargado, genera una copia de respaldo.
        else:
            Pv.copia_respaldo()
            message_dialog(
                title="COPIA DE RESPALDO",
                text="Copia de respaldo creada correctamente."
            ).run()
    
    # Si se selecciona la opción "REPARAR PRODUCTO" se muestra un menú para seleccionar el archivo con el cual reparar los datos.
    elif opcion == "REPARAR PRODUCTO":
        
        # Mientras el usuario desee reparar productos, se reparan los datos.
        while True:
            os.system('cls')
            Pv.reparar_datos()
            reparar_producto= button_dialog(
                title="REPARAR PRODUCTO",
                text="     Producto Reparado Correctamente\n\n      ¿Quiere cambiar el archivo con el que fue reparado?",
                buttons=[
                ("Sí", True),
                ("No", False)   
            ],
            style=style
            ).run() 
            
            if reparar_producto:
                continue
            else:
                break
     
                
    # Si se selecciona la opción "GRABAR NUEVOS PRODUCTOS" se graban nuevos productos.  
    elif opcion == "GRABAR NUEVOS PRODUCTOS":
        if not productos_cargados:
            message_dialog(
                title="ERROR",
                text="Debe cargar los productos primero antes de grabar nuevos productos.\nSeleccione la opción 'CARGAR PRODUCTOS' en el menú principal.".center(100)
            ).run()
        
        # Si los productos han sido cargados, se graban nuevos productos.
        else:
            # Mientras el usuario desee grabar nuevos productos, se graban los productos.
            while True:
                os.system('cls')
                Pv.agregar_producto()   
                grabar_nuevamente= button_dialog(
                    title="GRABAR NUEVOS PRODUCTOS",
                    text="¿Desea grabar más nuevos productos?",
                    buttons=[
                    ("Sí", True),
                    ("No", False)
                ],
                style=style
                ).run() 
                if grabar_nuevamente:
                    continue
                else:
                    break
                    
        
    # Si se selecciona la opción "BORRAR PRODUCTO" se borra un producto.    
    elif opcion == "BORRAR PRODUCTO":
        
        # Si no se han cargado los productos, se muestra un mensaje de error.
        if not productos_cargados:
            message_dialog(
                title="ERROR",
                text="      Debe cargar los productos primero antes de borrar un producto.\n      Seleccione la opción 'CARGAR PRODUCTOS' en el menú principal."
            ).run()
        
        # Si los productos han sido cargados, se borra un producto.
        else:
            while True:
                os.system('cls')
                Pv.eliminar_producto()
                borrar_nuevamente= Pv.eliminar_producto() 
                if borrar_nuevamente:
                    continue
                else:
                    break
        
    # Si se selecciona la opción "COMPRAR PRODUCTOS" se inicia el proceso de compra.  
    elif opcion == "COMPRAR PRODUCTOS":
        
        # Si no se han cargado los productos, se muestra un mensaje de error.
        if not productos_cargados:
            message_dialog(
                title="ERROR",
                text="Debe cargar los productos primero antes de comprar.\nSeleccione la opción 'CARGAR PRODUCTOS' en el menú principal."
            ).run()
            
        # Si los productos han sido cargados, se inicia el proceso de compra.
        else:
            os.system('cls')
            Pc= PC(Pv)
            Pc.proceso_de_compra()   
                
            
                
    # Si se selecciona la opción "IMPRIMIR FACTURA" se imprime la factura.    
    elif opcion == "IMPRIMIR FACTURA":
        
        Cc= CC(Pc)
        
        # Si no se han cargado los productos, se muestra un mensaje de error.
        if not productos_cargados:
            message_dialog(
                title="ERROR",
                text="Debe cargar los productos primero antes de imprimir una factura.\nSeleccione la opción 'CARGAR PRODUCTOS' en el menú principal."
            ).run()
            
        # Si no se han comprado productos, se muestra un mensaje de error.
        elif not Pc.get_lista_compra():
            message_dialog(
                title="ERROR",
                text="Debe comprar productos antes de imprimir una factura.\nSeleccione la opción 'COMPRAR PRODUCTOS' en el menú principal."
            ).run()
        
        else:
            Cc.mostrar_datos()
            Cc.generar_factura_pdf()
            message_dialog(
                title="IMPRIMIR FACTURA",
                text="Imprimiendo factura...",

                
        ).run()

    elif opcion is None:  # Cuando se selecciona "Salir"
        confirmacion = button_dialog(
            title="Confirmar Salida",
            text="¿Está seguro de que desea salir?",
            buttons=[
                ("Sí", True),
                ("No", False)
            ],
            style=style
        ).run()
        
        if confirmacion:
            return os.system('cls')   # Termina el programa   
        else:
            mostrar_menu(style)  # Vuelve al menú principal
    if opcion != "Salir":
        mostrar_menu(style) # Aplicamos recursividad para volver al menu principal, dentro de la funcion del menu principal.
    

