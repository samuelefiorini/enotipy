#!/usr/bin/python
"""
enotipy:
A handy Python script that sends email notifications.
"""
import os
import smtplib # Import smtplib for the actual sending function
import ConfigParser
import argparse

# Import the email modules we'll need
from email.mime.text import MIMEText

def getConfig():
    Config = ConfigParser.ConfigParser()
    Config.read(os.path.join(os.getcwd(),"enotipy.cfg"))
    # Get the configurations as dictionary
    configs = {}
    for section in Config.sections():
        options = Config.options(section)
        for option in options:
            try:
                configs[option] = Config.get(section, option)
                if configs[option] == -1:
                    DebugPrint("skip: %s" % option)
            except:
                print("exception on %s!" % option)
                configs[option] = None
    return configs

def main(subject, text):
    # Get the configurations from cfg file
    conf = getConfig()

    # Open a plain text file for reading.  For this example, assume that
    # the text file contains only ASCII characters.
    msg = MIMEText(text)

    msg['Subject'] = subject
    msg['From'] = conf['sourcemail']
    msg['To'] = conf['destinationmail']

    # Send the message via our own SMTP server, but don't include the
    # envelope header.
    s = smtplib.SMTP_SSL(conf['smtp'])
    s.login(conf['sourcemail'], conf['password'])
    s.sendmail(conf['sourcemail'], conf['destinationmail'], msg.as_string())
    s.quit()

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-s', metavar='{string}', type=str, default='auto',
                   help="subject of the email")
    parser.add_argument('-m', metavar='{string}', type=str, default='auto',
                   help="body of the email")
    args = parser.parse_args()

    # Parse input arguments
    if args.s == 'auto':
        subject = "enotipy: Your experiment is over"
    else:
        subject = args.s

    if args.m == 'auto':
        tmp = "Email sent by enotipy"
        text = "Done!\n"+"-"*len(tmp)+"\nhttp://repo"
    else:
        subject = args.s

    main(subject, text)
