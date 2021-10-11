#!/usr/bin/python
import os,sys,smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
CHANGE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(CHANGE_PATH)
from Lib.T_Global import PATHS as _P
from Lib.T_DateTime import getDateTime
from Lib.T_FileHandler import *
SMTP_SERVER = "smtp.gmail.com"
PORT = 465  # For starttls
SENDER_EMAIL = "rmakservice@gmail.com"
PASSWORD = "RM-SvC-2021"
def send_email(receiver_email,subject,flag,body):
    filename = _P.FLAGS_PATH+"/"+flag+"_"+str(getDateTime())+'.flg'
    f = open(filename, "a")
    f.write("")
    f.close()
    message = MIMEMultipart("alternative")
    message["Subject"] = subject
    message["From"] = SENDER_EMAIL
    message["To"] = receiver_email
    part = MIMEText(body, "html")
    message.attach(part)
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(SMTP_SERVER, PORT, context=context) as server:
        server.login(SENDER_EMAIL, PASSWORD)
        server.sendmail(SENDER_EMAIL, receiver_email, message.as_string())   

