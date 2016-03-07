#!/usr/bin/python
"""
enotipy: A handy Python script that sends email notifications.
"""
import os
import ConfigParser
import argparse

from enotipy._core import send_mail

def getConfig():
    Config = ConfigParser.ConfigParser()
    Config.read(os.path.join("/etc/enotipy","enotipy.cfg"))
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

    msg = send_mail(subject, text, conf['sourcemail'], conf['password'],
                                   conf['destinationmail'], conf['smtp'])

    print("From:\t{}\nTo:\t{}\n\n{}".format(msg['From'], msg['To'], msg.get_payload()))

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-s', metavar='string', type=str, default='auto',
                   help="subject of the email")
    parser.add_argument('-m', metavar='string', type=str, default='auto',
                   help="body of the email")
    args = parser.parse_args()

    # Parse input arguments
    if args.s == 'auto':
        subject = "enotipy: Your experiment is done"
    else:
        subject = args.s

    if args.m == 'auto':
        body = "Done!"
        tail = "Email sent by enotipy"
        link = "https://samuele_fiorini@bitbucket.org/samuele_fiorini/enotipy.git"
        text = "\n".join((body,"-"*len(link),tail,link))
    else:
        text = args.m

    main(subject, text)
