#! /c/Python27/python
# -*- coding: utf-8 -*-
"""
    nyanbot.chatbot
    ~~~~~~~~~~~~~~~

    Usage:
      chatbot.py <command>

    Options:
      -h --help     Show this screen.
      -v --version  Show version.
"""

import docopt
from grammar import create_grammars, match_grammars


if __name__ == '__main__':
    args = docopt(__doc__, version='Nyanbot 0.1')
    try:
        grammars = create_grammars(args['<command>'])
    # KeyError from '<command>'
    except KeyError:
        pass

