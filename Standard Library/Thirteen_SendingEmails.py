# It is particularly useful if we have a database of customers and send emails based on their ineterest
# We need to import couple of classes one to create email msges another one to connect with a SMTP server for sending emails

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText #for sending text
from email.mime.image import MIMEImage #for sending image
from pathlib import Path #for image path
import smtplib 

message = MIMEMultipart()
message["from"] = "Sadman Sakib"
message["to"] = "triplesa55@gmail.com" 
message["subject"] = "This is a test msg using python."
message.attach(MIMEText("Body")) #Its for sending text
message.attach(MIMEImage(Path("image_path").read_bytes())) #Its for sending image


with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp: #The value will be our smtp value
    smtp.ehlo() #This is a simple hello msg to the smtp server (part of smtp protocol)
    smtp.starttls() #tls: Transport Layer Security (all the commands will be encripted)
    smtp.login("testuser@gmail.com", "password123") #it sets our email and password
    smtp.send_message(message)
    print("Sent...")
