import smtplib
from email.message import EmailMessage
import imghdr

EMAIL_ADRESS = "gaiborjimenezjosue@gmail.com"
EMAIL_PASSWORD = "GOE2005@"
def RECIEVER(): 
 email = 'eggaibor@hotmail.com'
msg = EmailMessage()
msg['Subject'] = 'TITULO DEL EMAIL'
msg['From'] = EMAIL_ADRESS
msg['To'] = RECIEVER
msg.set_content("CONTENIDO DEL MENSAJE")
with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(EMAIL_ADRESS, EMAIL_PASSWORD)
    
    smtp.send_message(msg)