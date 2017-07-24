#!/usr/bin/env python

from distutils.core import setup

scripts = ['scripts/spoofer']
try:
    import fuse
    scripts.append('scripts/spoofer')
except ImportError:
    print "python-fuse not detected, not installing the spoofer."
    print "You can still use the spoofer for a ftp-like interface"
    pass

setup( name='Spoofer',
        version='1.0',
        description='Ip Spoofer',
        author='Anonymous',
        author_email='anonymous@anon.com',
        url='https://github.com/sqinfo/spoofer',
        packages=['spoofer'],
        scripts=scripts,
        )
