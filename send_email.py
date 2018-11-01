# coding: utf-8
import smtplib
from email.mime.text import MIMEText
 
def send_email(receivers, subject, message):
    messageFormatted = MIMEText(message)
    messageFormatted['From'] = "From: Sistema de Alerta - SUIN <suin.alert@gmail.com>"
    messageFormatted['To'] = receivers
    messageFormatted['Subject'] = subject
 
    # create server
    server = smtplib.SMTP('smtp.gmail.com: 587')
    server.starttls()
 
    # setup the parameters of the message
    password = "alert1234"
    # Login Credentials for sending the mail
    server.login("suin.alert@gmail.com", password) 
    # send the message via the server.
    server.sendmail("suin.alert@gmail.com", receivers, messageFormatted.as_string()) 
    server.quit()

    print "successfully sent email to: %s" % (receivers)
