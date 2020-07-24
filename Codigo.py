from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib, ssl

#correo
username = input('')
#password correo
password = input('')

#correo de remitente
recipient = ('')

#asunto
affair = ("")

message = MIMEMultipart("alternative")
message ["subject"] = affair
message ["From"] = username
message ["To"] = recipient

#codigo html5
html = f""" 
 
"""

html_part = MIMEText(html, "html")
message.attach(html_part)

conection = ssl.create_default_context()


#servidor puerto
with smtplib.SMTP_SSL("", 595, context=conection) as server:
    server.login(username, password)
    print("correct login")  
    server.sendmail(username, recipient, message.as_bytes())
    print("message sent")

