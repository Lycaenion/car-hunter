import smtplib
from email.mime.text import MIMEText
from itertools import islice

subject = "Test email"
body = "This is the body"
recipients = []
with open('emails.txt') as f:
    sender = f.readline().strip('\n')
    for line in islice(f, 0,2):
        recipients.append(line.strip('\n'))

