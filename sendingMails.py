import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

from passwords_info import mail2_pass


def send_mails(email_sender, email_receiver, file_Path, eventname, cert_type):

    email_subject = f"Your {eventname} certificate."
    email_body = f"This is to inform you, we just send your {eventname}'s certificate {cert_type}. "
    password = mail2_pass

    msg = MIMEMultipart()
    msg['From'] = email_sender
    msg['To'] = email_receiver
    msg['Subject'] = email_subject
    # msg.set_content = email_body
    msg.attach(MIMEText(email_body, 'plain'))

    # open the file to sent:
    filename = file_Path
    attachment = open(filename, 'rb')

    p = MIMEBase('application', 'octet-stream')

    p.set_payload((attachment).read())  # when we attach any file with text(or mix with anything) this is known as payload. 

    encoders.encode_base64(p)

    p.add_header("Content-Disposition", "attachment: filename= %s"%filename)

    msg.attach(p)

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(email_sender, password)

    text = msg.as_string()
    server.send_message(msg)
    server.quit()

    print("message send successfully....")

