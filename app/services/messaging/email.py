import logging
import smtplib
from email.errors import MessageError
from email.message import EmailMessage

from app.core.config import settings


def send_email(email_recipient, message):
    msg = EmailMessage()
    msg.set_content(message)

    msg["Subject"] = "Welcome"
    msg["From"] = settings.EMAIL_SENDER
    msg["To"] = email_recipient

    s = smtplib.SMTP(settings.SMTP_SERVER)
    try:
        s.send_message(msg)
        s.quit()
    except MessageError as e:
        logging.error(e)
