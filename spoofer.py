import smtplib


cuenta_origen = input("Ingresa la cuenta de origen: ")
cuenta_destino = input("Ingresa la cuenta de destino: ")
servidor = input("Ingresa el servidor SMTP: ")
puertos = [25, 465, 587]  

mensaje = """Subject: Prueba de Spoofing\n\nEste es un correo de prueba."""

def probar_envio(servidor, cuenta_origen, cuenta_destino, puerto):
    try:
        if puerto == 465:
            server = smtplib.SMTP_SSL(servidor, puerto)
        else:
            server = smtplib.SMTP(servidor, puerto)
            server.ehlo()
            if puerto == 587:
                server.starttls()
        
        server.sendmail(cuenta_origen, cuenta_destino, mensaje)
        server.quit()
        print(f"Correo enviado exitosamente a través del puerto {puerto}.")
        return True
    except Exception as e:
        print(f"Error en el puerto {puerto}: {e}")
        return False

for puerto in puertos:
    if probar_envio(servidor, cuenta_origen, cuenta_destino, puerto):
        break
