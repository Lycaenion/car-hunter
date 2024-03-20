#import smtplib
#from email.mime.text import MIMEText
#from itertools import islice
from getpass import getpass

import base64
from email.mime.text import MIMEText
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from requests import HTTPError

SCOPES = [
    "https://www.googleapis.com/auth/gmail.send"
]

flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
creds = flow.run_local_server(port=0)

#subject = "Test email"
body = "This is the body of an email sent via a python script created by Linn"
with open('emails.txt') as f:
    recipients = f.read().splitlines()
    f.close()

def sendemail(body):

    service = build('gmail', 'v1', credentials=creds)
    msg = MIMEText(body)
    msg['Subject'] = "This is a test email"
    msg['To'] = ", ".join(recipients)
    create_message = {'raw': base64.urlsafe_b64encode(msg.as_bytes()).decode()}

    try:
        message = (service.users().messages().send(userId='me', body=create_message).execute())
        print(F'sent message to {message} Message Id: {message["id"]}')
    except HTTPError as error:
        print(F'An error occured: {error}')


#sendemail(body)

