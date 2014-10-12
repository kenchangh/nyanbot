#! /c/Python27/python
# -*- coding: utf-8 -*-
"""
    nyanbot.chatbot
    ~~~~~~~~~~~~~~~

Usage:
  chatbot.py <command>...

Options:
  -h --help     Show this screen.
  -v --version  Show version.
"""

from docopt import docopt
from scripts import COMMANDS
from grammar import create_grammars, match_grammars


def raise_invalid_command(command):
    raise Exception(
        'Command {} is invalid or not registered'.format(command)
    )


def run_command(user_command):
    """
    Runs the nyanbot commands.
    """
    valid_command = False
    for command in COMMANDS:
        # matched could be dictionary or False
        matched = match_grammars(user_command,
            create_grammars(command))
        if matched:
            vars_to_values = matched  # clearer naming
            function = COMMANDS[command]
            variables = vars_to_values.keys()
            for var in variables:
                value = vars_to_values[var]
                function(value)
            valid_command = True
            break
        # command not registered or invalid
    if not valid_command:
        raise_invalid_command(user_command)


if __name__ == '__main__':
    args = docopt(__doc__, version='Nyanbot 0.1')
    try:
        user_command = args['<command>']
    # Command not present
    except KeyError:
        raise Exception('No command given!')
    # ['image', 'me', 'yolo'] => 'image me yolo'
    user_command = ' '.join(user_command)
    run_command(user_command)

    
