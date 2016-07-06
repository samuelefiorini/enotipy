# enotipy
A handy Python script that sends email notifications.

--------------------------------------------------------------------------------

Installation instructions:

  1. Set config file:
    - rename enotipy.cfg.example as enotipy.cfg
    
      ``mv enotipy.cfg.example enotipy.cfg``

    - fill the blank fields in enotipy.cfg
    
      ``vim enotipy.cfg``

  2. Install enotipy
  
     ``python setup.py install``

Usage: in a bash shell run

``any_command; enoti.py``

--------------------------------------------------------------------------------

To use only the notification utility:

``from enotipy import send_mail``

``send_mail(subject, text, source, password, destination)``
