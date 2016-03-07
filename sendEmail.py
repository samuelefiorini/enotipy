#!/usr/bin/python
# Import smtplib for the actual sending function
import smtplib

# Import the email modules we'll need
from email.mime.text import MIMEText



def main():
    # Open a plain text file for reading.  For this example, assume that
    # the text file contains only ASCII characters.
    msg = MIMEText('Done!')

    # me == the sender's email address
    # you == the recipient's email address
    msg['Subject'] = 'Your experiment is over'
    msg['From'] = 'experim.done@gmail.com'
    msg['To'] = 'samuele.fiorini@gmail.com'

    # Send the message via our own SMTP server, but don't include the
    # envelope header.
    s = smtplib.SMTP_SSL('smtp.gmail.com')
    s.login('experim.done', 'compbio309')
    s.sendmail('experim.done@gmail.com', 'samuele.fiorini@gmail.com', msg.as_string())
    s.quit()

if __name__ == '__main__':
    main()
