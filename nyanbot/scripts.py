#! /c/Python27/python
# -*- coding: utf-8 -*-
"""
    nyanbot.scripts
    ~~~~~~~~~~~~~~~

    Default scripts for nyanbot.

    NOTE:
        Never use underscore in front of command names.
        It just fucks things up somehow.
        No:  _help
        Yes: help_
"""

import urllib
import urllib2
import simplejson
from cStringIO import StringIO
from PIL import Image


def ping():
    print 'pong'


def search_me(term, search_type='web'):
    fetcher = urllib2.build_opener()
    print "Searching for '{}'...".format(term)
    term = urllib.quote(term)
    search_url = "http://ajax.googleapis.com/ajax/services/search/"\
                 + search_type + "?v=1.0&q=" + term + "&start=0"
    response = fetcher.open(search_url)
    _json = simplejson.load(response)
    url = _json['responseData']['results'][0]['unescapedUrl']
    if search_type == 'web':
        print url
    return url


def image_me(image_name):
    image_url = search_me(image_name, search_type='images')
    print 'Loading image...'
    # Make into stream buffer to trick Image.open
    s = StringIO(urllib.urlopen(image_url).read())
    Image.open(s).show()


def rules():
    rules = [
      "1. A robot may not injure a human being or, through inaction, allow a human being to come to harm.",
      "2. A robot must obey any orders given to it by human beings, except where such orders would conflict with the First Law.",
      "3. A robot must protect its own existence as long as such protection does not conflict with the First or Second Law."
    ]
    print '\n'.join(rules)


def echo(message):
    print message


def help_():
    print 'yo'

"""
def register(script):
    import script
"""
