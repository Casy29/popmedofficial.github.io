
import smtplib 
from email.message import EmailMessage
from email.mime.application import MIMEApplication
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from typing import Text

EmailAdd = "casian168@gmail.com" 
Pass = "ygqthflstkaflmbw" 

msg = EmailMessage()
msg['Subject'] = 'rezervare online' 
msg['From'] = EmailAdd
msg['To'] = input('introdu adresa de email')
msg.set_content(input('pentru ce ati dori sa faceti rezervare?')) 


