#!/usr/bin/env python3
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import json

data = {}
#with open('pass.json') as f:
 # data = json.load(f)
# create message object instance

msg = MIMEMultipart()

 
message = "Hola soy Fernanda, de la clase de Laboratorio de Ciberseguridad de los Sabados a las 12pm."

 
msg['From'] = 'fernanda.lealmr@uanl.edu.mx'
receipents = ["fernandalealmo@gmail.com","Sergio1402morado@gmail.com","iris.sanchezvz@uanl.edu.mx"]
msg['To'] = ", ".join(receipents)
msg['Subject'] = 'Saludos a todos!'

msg.attach(MIMEText(message, 'plain'))

server = smtplib.SMTP('smtp.office365.com:587')
server.starttls()

server.login('fernanda.lealmr@uanl.edu.mx','------------')

server.sendmail(msg['From'], receipents, msg.as_string())
server.quit()
print("successfully sent email to %s:" % (msg['To']))

