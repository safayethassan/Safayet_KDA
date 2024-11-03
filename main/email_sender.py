import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

def send_email(report_file, recipient_emails):
    sender_email = "safayethassan340@gmail.com"
    password = "dagameishere"

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['Subject'] = "Test Report"

    for email in recipient_emails:
        msg['To'] = email

    with open(report_file, "rb") as attachment:
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read())
        encoders.encode_base64(part)
        part.add_header("Content-Disposition", f"attachment; filename= {report_file}")
        msg.attach(part)

    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login(sender_email, password)
        server.send_message(msg)

# Call send_email() after generating the report