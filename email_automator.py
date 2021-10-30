from email.message import EmailMessage
import smtplib
import os
from dotenv import load_dotenv

load_dotenv(".env")

SENDER = os.environ.get("GMAIL_USER")
PASSWORD = os.environ.get("GMAIL_PASSWORD")

def send_email(recipients, subject, body):
    """
    send_email takes in recipients, a subject, and a body, and sends the ...
    email using smtplib
    """
    msg = EmailMessage()
    msg.set_content(body)
    msg["Subject"] = subject
    msg["From"] = SENDER
    if len(recipients) == 1:
        recipient = recipients[0]
        print(recipient)
    else:
        recipient = ", ".join(recipients)
        print(recipient)
    msg["To"] = recipient
    sent_successfully = False
    try:
        server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
        server.login(SENDER, PASSWORD)
        server.send_message(msg)
        server.quit()
        sent_successfully = True
    except:
        sent_successfully = False
    return sent_successfully

# send_email("replace_me@hey.com", subject="test", body="test")