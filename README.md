A handy Python script that sends email notifications.

--------------------------------------------------------------------------------

Installation instructions:

  1. Set config file:
    - rename enotipy.cfg.example as enotipy.cfg
    - fill the blank fields in enotipy.cfg

  2. python setup.py install (this may require sudo privileges)

Usage:

In a bash shell run:

$ any_command; enoti.py

--------------------------------------------------------------------------------

To use only the notification utility:

>>> from enotipy import send_mail
>>> send_mail(subject, text, source, password, destination)
