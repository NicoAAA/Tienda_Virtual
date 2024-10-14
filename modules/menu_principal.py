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
Modulo que permite ir al menú principal de la aplicación.
Este módulo es llamado desde otros módulos para regresar 
al menú principal. Se hace esto para evadir las importaciones
circulares, que dada la lógica del programa eran necesarias.
'''

# Importaciones Locales
from modules.styles.styles_store import style_menu


def ir_al_menu():
    '''
    Función que permite ir al menú principal de la aplicación.
    '''  
    from modules.funciones import mostrar_menu  
    mostrar_menu(style_menu)





