#! /c/Python27/python
# -*- coding: utf-8 -*-
"""
    nyanbot.scripts
    ~~~~~~~~~~~~~~~

    Default scripts for nyanbot.
"""

import json
import urllib
import urllib2
import simplejson
from cStringIO import StringIO
from PIL import Image


def nyanbot_function(pattern):
    def decorator(function):
        with open('commands.json', 'r+') as f:
            commands = json.loads(f.read())
            commands[pattern] = function
            f.write(json.dumps(commands))
        return function
    return decorator


def ping():
    print 'pong'


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


def get_commands():
    with open('commands.json', 'r') as f:
        commands = json.loads(f.read())
        # Convert all strings into functions
        commands.update((pattern, globals()[command]) 
            for pattern, command in commands.items())
        return commands
