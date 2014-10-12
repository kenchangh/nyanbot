#! /c/Python27/python
# -*- coding: utf-8 -*-
"""
    nyanbot.scripts
    ~~~~~~~~~~~~~~~

    Default scripts for nyanbot.
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


"""
def register(script):
    import script
"""
