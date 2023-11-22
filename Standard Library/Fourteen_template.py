from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText 
from email.mime.image import MIMEImage 
from pathlib import Path 
from string import Template #for using template
import smtplib 


template = Template(Path("Standard Library/subfolder14/template.html").read_text())
#template.substitute() #with this substitute method we can replace parameters dynamically

message = MIMEMultipart()
message["from"] = "Sadman Sakib"
message["to"] = "triplesa55@gmail.com" 
message["subject"] = "This is a test msg using python."


body = template.substitute({ "name": "John" }) #this will return a string object (or keyword argument: template.substitute(name="John"))
message.attach(MIMEText(body, "html")) #here we will pass a template
message.attach(MIMEImage(Path("image_path").read_bytes()))


with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp: 
    smtp.ehlo() 
    smtp.starttls() 
    smtp.login("testuser@gmail.com", "password123") 
    smtp.send_message(message)
    print("Sent...")
