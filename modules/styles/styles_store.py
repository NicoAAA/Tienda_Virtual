from prompt_toolkit.styles import Style

style_store = Style.from_dict({
    "dialog": "bg:#ECF0F1",          # Fondo del cuadro de diálogo (blanco nítido)
    "dialog.body": "bg:#2C3E50 fg:#ECF0F1",  # Fondo del cuerpo del diálogo (gris oscuro) con texto blanco
    "dialog.shadow": "bg:#34495E",    # Sombra del cuadro de diálogo (gris más oscuro)
    "dialog.title": "fg:#3498DB bold", # Título en azul deportivo y negrita
    "dialog.button": "bg:#2ECC71 fg:#2C3E50",    # Fondo de los botones en verde vibrante con texto gris oscuro
    "dialog.button.focused": "bg:#E67E22 fg:#ECF0F1 bold", # Botón enfocado en naranja energético con texto blanco
})

"""
ESTILO PARA EL MENÚ PRINCIPAL
"""
style_menu = Style.from_dict({
    "dialog": "bg:#ffc400  #e3b314",  # Fondo rojo, texto blanco
    'radiolist': 'bg:#4CAF50 fg:#ffffff',
    "button.accept": "bg:#27AE60 fg:#FFFFFF bold",  # Botón de aceptar en verde
    "button.cancel": "bg:#E74C3C fg:#FFFFFF bold",  # Botón de cancelar en rojo
    "dialog.shadow": "bg:#34495E",  # Sombra del diálogo en gris más oscuro
    'dialog.body': 'bg:#ffffff fg:#000000',
    'message_dialog': 'bg:#888888 fg:#000000',   
})


""" 
ESTILO PARA VENTANA DE VALIDAR EL CÓDIGO DE UN PRODUCTO.
"""
style = Style.from_dict({
    "dialog": "bg:#17202A",             # Fondo del diálogo en negro nítido
    "dialog.title": "fg:#3498DB bold",  # Título en azul deportivo y negrita
    "dialog.body": "bg:#2C3E50 fg:#ECF0F1",  # Fondo del cuerpo en gris oscuro con texto blanco
    "dialog.shadow": "bg:#34495E",      # Sombra del diálogo en gris más oscuro
    "button": "bg:#2ECC71 fg:#2C3E50",  # Botones en verde vibrante con texto gris oscuro
    "button.focused": "bg:#E67E22 fg:#ECF0F1 bold",  # Botón enfocado en naranja energético con texto blanco
})

"""
ESTILO PARA VENTANA DE VALIDAR DESCRIPCION DE UN PRODUCTO. 
"""
styles = Style.from_dict({
    "dialog": "bg:#1C2833",             # Fondo del diálogo en negro nítido
    "dialog.title": "fg:#3498DB bold",  # Título en azul deportivo y negrita
    "dialog.body": "bg:#2C3E50 fg:#ECF0F1",  # Fondo del cuerpo en gris oscuro con texto blanco
    "dialog.shadow": "bg:#34495E",      # Sombra del diálogo en gris más oscuro
    "button": "bg:#2ECC71 fg:#2C3E50",  # Botones en verde vibrante con texto gris oscuro
    "button.focused": "bg:#E67E22 fg:#ECF0F1 bold",  # Botón enfocado en naranja energético con texto blanco
})

style_1 = Style.from_dict({
    "dialog": "bg:#1C2833",             # Fondo del diálogo en negro nítido
    "dialog.title": "fg:#3498DB bold",  # Título en azul deportivo y negrita
    "dialog.body": "bg:#2C3E50 fg:#ECF0F1",  # Fondo del cuerpo en gris oscuro con texto blanco
    "dialog.shadow": "bg:#34495E",      # Sombra del diálogo en gris más oscuro
    "button": "bg:#2ECC71 fg:#2C3E50",  # Botones en verde vibrante con texto gris oscuro
    "button.focused": "bg:#E67E22 fg:#ECF0F1 bold",  # Botón enfocado en naranja energético con texto blanco
    "input": "bg:#2C3E50 fg:#3498DB",   # Fondo de input en gris oscuro con texto azul
    "input.focused": "bg:#1ABC9C fg:#2C3E50 bold",   # Input enfocado en verde agua con texto gris oscuro
    "delete": "bg:#E74C3C fg:#ECF0F1 bold",  # Fondo rojo vibrante para eliminar producto con texto blanco
    "delete.focused": "bg:#C0392B fg:#ECF0F1 bold",  # Fondo más oscuro al enfocarse
})


style_9 = Style.from_dict({
    "dialog": "bg:#273746",             # Fondo del diálogo en azul grisáceo oscuro
    "dialog.title": "fg:#3498DB bold",  # Título en azul deportivo y negrita
    "dialog.body": "bg:#2C3E50 fg:#ECF0F1",  # Fondo del cuerpo en gris oscuro con texto blanco
    "dialog.shadow": "bg:#34495E",      # Sombra del diálogo en gris más oscuro
    "button": "bg:#2ECC71 fg:#2C3E50",  # Botones en verde vibrante con texto gris oscuro
    "button.focused": "bg:#E67E22 fg:#ECF0F1 bold",  # Botón enfocado en naranja energético con texto blanco
    "input": "bg:#2C3E50 fg:#3498DB",   # Fondo de input en gris oscuro con texto azul
    "input.focused": "bg:#1ABC9C fg:#2C3E50 bold",   # Input enfocado en verde agua con texto gris oscuro
    "delete": "bg:#E74C3C fg:#ECF0F1 bold",  # Fondo rojo vibrante para eliminar producto con texto blanco
    "delete.focused": "bg:#C0392B fg:#ECF0F1 bold",  # Fondo más oscuro al enfocarse
})

style_9 = Style.from_dict({
    "dialog": "bg:#273746",             # Fondo del diálogo en azul grisáceo oscuro
    "dialog.title": "fg:#3498DB bold",  # Título en azul deportivo y negrita
    "dialog.body": "bg:#2C3E50 fg:#ECF0F1",  # Fondo del cuerpo en gris oscuro con texto blanco
    "dialog.shadow": "bg:#34495E",      # Sombra del diálogo en gris más oscuro
    "button": "bg:#2ECC71 fg:#2C3E50",  # Botones en verde vibrante con texto gris oscuro
    "button.focused": "bg:#E67E22 fg:#ECF0F1 bold",  # Botón enfocado en naranja energético con texto blanco
    "input": "bg:#2C3E50 fg:#3498DB",   # Fondo de input en gris oscuro con texto azul
    "input.focused": "bg:#1ABC9C fg:#2C3E50 bold",   # Input enfocado en verde agua con texto gris oscuro
    "delete": "bg:#E74C3C fg:#ECF0F1 bold",  # Fondo rojo vibrante para eliminar producto con texto blanco
    "delete.focused": "bg:#C0392B fg:#ECF0F1 bold",  # Fondo más oscuro al enfocarse
})

style_10 = Style.from_dict({
    "dialog": "bg: #2ECC71",             # Fondo del diálogo en verde claro
    "dialog.title": "fg:#3498DB bold",  # Título en azul deportivo y negrita
    "dialog.body": "bg:#2ECC71 fg:#ECF0F1",  # Fondo del cuerpo en gris oscuro con texto blanco
    "dialog.shadow": "bg:#34495E",      # Sombra del diálogo en gris más oscuro
    "button": "bg:#2ECC71 fg:#2C3E50",  # Botones en verde vibrante con texto gris oscuro
    "button.focused": "bg:#E67E22 fg:#ECF0F1 bold",  # Botón enfocado en naranja energético con texto blanco
    "input": "bg:#2C3E50 fg:#3498DB",   # Fondo de input en gris oscuro con texto azul
    "input.focused": "bg:#1ABC9C fg:#2C3E50 bold",   # Input enfocado en verde agua con texto gris oscuro
    "delete": "bg:#E74C3C fg:#ECF0F1 bold",  # Fondo rojo vibrante para eliminar producto con texto blanco
    "delete.focused": "bg:#C0392B fg:#ECF0F1 bold",  # Fondo más oscuro al enfocarse
})
