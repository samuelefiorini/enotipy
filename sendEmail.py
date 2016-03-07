#!/usr/bin/python
import os
import smtplib # Import smtplib for the actual sending function
import ConfigParser

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

def main():
    # Open a plain text file for reading.  For this example, assume that
    # the text file contains only ASCII characters.
    msg = MIMEText('Done!')

    # Get the configurations
    conf = getConfig()

    # me == the sender's email address
    # you == the recipient's email address
    msg['Subject'] = 'Your experiment is over'
    msg['From'] = conf['sourcemail']
    msg['To'] = conf['destinationmail']

    # Send the message via our own SMTP server, but don't include the
    # envelope header.
    s = smtplib.SMTP_SSL(conf['smtp'])
    s.login(conf['sourcemail'], conf['password'])
    s.sendmail(conf['sourcemail'], conf['destinationmail'], msg.as_string())
    s.quit()

if __name__ == '__main__':
    main()
