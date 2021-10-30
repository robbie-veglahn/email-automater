from email.message import EmailMessage
import smtplib
import os
from dotenv import load_dotenv

load_dotenv(".env")

SENDER = os.environ.get("GMAIL_USER")
PASSWORD = os.environ.get("GMAIL_PASSWORD")

def send_email(recipient, subject, body):
    msg = EmailMessage()
    msg.set_content(body)
    msg["Subject"] = subject
    msg["From"] = SENDER
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