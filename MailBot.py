# Send emails with python using smtplib

# Import smtplib for the actual sending function
import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from getpass import getpass
import fulltext


sender_email = "murftestdevops@gmail.com"
receiver_email = "jerraillmurphy2012@gmail.com"
email_subject = "Blick"

port = 587
smtp_server = "smtp.gmail.com"
password = getpass()

context = ssl.create_default_context()
# Open the DOC file that contains email body.

message = MIMEMultipart('alternative')
message['From'] = sender_email
message['To'] = receiver_email
message['Subject'] = email_subject

text = fulltext.get('FormatedEmail.docx', None)

html =

try:
    server = smtplib.SMTP(smtp_server, port)
    server.ehlo()
    server.starttls(context=context)
    server.ehlo()
    server.login(sender_email, password)
    print("GOOD LOGIN")
    server.sendmail(sender_email, receiver_email, message.as_string())
except Exception as e:
    print(e)
finally:
    server.quit()
