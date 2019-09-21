import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from config import MAIL_SERVER, MAIL_PORT, MAIL_USERNAME, MAIL_PASSWORD, MAIL_DEFAULT_SENDER

def send_email(receiver_mail, email_subject, content):
    message = MIMEMultipart("alternative")
    message['Subject'] = email_subject
    message['From'] = MAIL_DEFAULT_SENDER
    message['To'] = receiver_mail

    email = MIMEText(content, "plain")
    message.attach(email)

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(MAIL_SERVER, MAIL_PORT, context=context) as server:
        server.login(MAIL_USERNAME, MAIL_PASSWORD)
        server.sendmail(MAIL_DEFAULT_SENDER, receiver_mail, message.as_string())
