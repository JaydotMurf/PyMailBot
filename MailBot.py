
import csv, smtplib, ssl
from getpass import getpass

port = 465
server = "smtp.gmail.com"
message = """Subject: Your grade

Hi {name}, your grade is {grade}"""

from_address = "murftestdevops@gmail.com"
password = getpass() # Prompt the user for a password without echoing
context = ssl.create_default_context()

with smtplib.SMTP_SSL(server, port, context=context) as server:
    server.login(from_address, password)
    with open("contact_list.csv".strip()) as file: # Import csv and strip white space
        reader = csv.reader(file) # Makes it easy to read a CSV file line by line 
        next(reader)  # Skip header row
        for name, email, grade in reader:
          print(f"Sending email to {name}")
          server.sendmail(from_address,email,message.format(name=name,grade=grade),)
