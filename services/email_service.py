from credentials import get_email_for_email_report, get_password_for_email_report, get_recipients_for_email_report
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

class EmailService():
    def __init__(self) -> None:
        self.port = 465
        self.smtp_server = "smtp.gmail.com"
        self.sender_email = get_email_for_email_report()
        self.password = get_password_for_email_report()
        self.recipients = get_recipients_for_email_report

    def send_email(self, subject, body):
        msg = MIMEMultipart()
        msg['From'] = self.sender_email
        msg['To'] = ', '.join(self.recipients)
        msg["Subject"] = subject
        body = MIMEText(body)
        msg.attach(body)
        
        server = smtplib.SMTP_SSL(self.smtp_server, self.port)

        server.login(self.sender_email, self.password)
        server.sendmail(self.sender_email, self.recipients, msg.as_string())
        server.quit()