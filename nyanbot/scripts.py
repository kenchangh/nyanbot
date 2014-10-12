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


def nyanbot_function(pattern):
    def decorator(function):
        COMMANDS[pattern] = function
        return function
    return decorator


def image_me(image):
    fetcher = urllib2.build_opener()
    print 'Searching for image...'
    search_url = "http://ajax.googleapis.com/ajax/services/search/"\
                 "images?v=1.0&q=" + image + "&start=0"
    response = fetcher.open(search_url)
    _json = simplejson.load(response)

    image_url = _json['responseData']['results'][0]['unescapedUrl']
    print 'Loading image...'
    # Make into stream buffer to trick Image.open
    s = StringIO(urllib.urlopen(image_url).read())
    Image.open(s).show()


COMMANDS = {
    'image/img [me] <image>': image_me,
}
