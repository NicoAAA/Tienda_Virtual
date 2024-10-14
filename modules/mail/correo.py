'''
SENA CBA CENTRO DE BIOTECNOLOGIA AGROPECUARIA
PROGRAMACION DE SOFTWARE

FICHA: 2877795
AUTOR: NICOLAS ANDRES ACOSTA HIGUERA
PROYECTO: TIENDA VIRTUAL (modulos/mail/correo.py)
FECHA: 2024-07-01
VERSION: 4.5.6
'''

# Importar el módulo os para acceder a funcionalidades dependientes del Sistema Operativo
import os

# Importar el módulo ssl para crear una conexión segura
import ssl

# Importar el módulo smtplib para enviar correos electrónicos
import smtplib

# Importar la función load_dotenv para cargar las variables de entorno
from dotenv import load_dotenv

# Importar la clase EmailMessage para crear mensajes de correo
from email.message import EmailMessage



def enviar_por_pdf(ruta_pdf,nombre,correo):
    '''
    Funcion que permite enviar un correo con un archivo PDF adjunto.
    
    Argumentos:
    
        ruta_pdf -- str -- La ruta del archivo PDF a adjuntar.
        nombre -- str -- El nombre del destinatario.
        correo -- str -- El correo del destinatario.
    '''
    
    # Cargar las variables de entorno
    load_dotenv()

    
    #  Correo del remitente
    email_sender= 'andres.django.puebas@gmail.com'
    
    # Contraseña del remitente 
    password = os.getenv("PASSWORD")
    
    # Correo del destinatario
    email_reciver = correo

    # Asunto del correo
    subject = 'FACTURA DE COMPRA'
    
    # Cuerpo del correo
    body = f'¡Hola {nombre}!\n\nNos  alegra que hallas comprado en la  tienda virtual  CBA, gracias\npor tu compra. A continuación te presentamos tu factura de compra:\n\n'



    # Crear el mensaje 
    em = EmailMessage()
    em["From"] = email_sender
    em["To"] = email_reciver
    em["Subject"] = subject
    em.set_content(body)
    
    # Adjuntar el PDF generado
    with open(ruta_pdf, "rb") as file:
        file_data = file.read()
        file_name = os.path.basename(ruta_pdf)



    # Agregar el PDF como adjunto
    em.add_attachment(file_data, maintype="application", subtype="pdf", filename=file_name)

    

    # Enviar el correo
    context = ssl.create_default_context()

    # Conexión con el servidor SMTP de Gmail
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(email_sender, password)
        server.sendmail(email_sender, email_reciver, em.as_string()),
        server.quit()
    