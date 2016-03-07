"""
enotipy core functions
"""
import smtplib # Import smtplib for the actual sending function
from email.mime.text import MIMEText # Import the email modules we'll need

def send_mail(subject, text, source, password, destination, server = "smtp.gmail.com"):
    # Open a plain text file for reading.  For this example, assume that
    # the text file contains only ASCII characters.
    msg = MIMEText(text)

    msg['Subject'] = subject
    msg['From'] = source
    msg['To'] = destination

    # Send the message via our own SMTP server, but don't include the
    # envelope header.
    s = smtplib.SMTP_SSL(server)
    s.login(source, password)
    s.sendmail(source, destination, msg.as_string())
    s.quit()

    return msg
