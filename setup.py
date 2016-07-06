#!/usr/bin/env python
# enotipy setup script

from distutils.core import setup

# Package Version
from enotipy import __version__ as version

setup(
    name='enotipy',
    version=version,

    description=('A handy Python script that sends email notifications'),
    long_description=open('README.md').read(),
    author='enotipy developers - SlipGURU',
    author_email='samuele.fiorini@dibris.unige.it',
    maintainer='Samuele Fiorini',
    maintainer_email='samuele.fiorini@dibris.unige.it',
    url='https://github.com/samuelefiorini/enotipy.git',

    classifiers=[
        'Development Status :: Beta',
        'Environment :: Console',
        'Intended Audience :: Science/Research',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'License :: OSI Approved :: BSD License',
        'Topic :: Software Development',
        'Topic :: Scientific/Engineering :: Bio-Informatics',
        'Operating System :: POSIX',
        'Operating System :: Unix',
        'Operating System :: MacOS'
    ],
    license = 'new BSD',

    packages=['enotipy'],
    requires=['smtplib','email.mime'],
    scripts=['enotipy/enoti.py'],
    data_files=[('/etc/enotipy', ['enotipy.cfg'])]
)
