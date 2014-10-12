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
from scripts import get_commands
from grammar import create_grammars, match_grammars


def raise_invalid_command(command):
    raise Exception(
        'Command {} is invalid or not registered'.format(command)
    )


COMMANDS = get_commands()

def run_command(user_command):
    """
    Runs the nyanbot commands.
    """
    valid_command = False
    for command in COMMANDS:
        # matched could be dictionary or False
        matched = match_grammars(user_command,
            create_grammars(command))
        # if matched: might not work, might be {}
        if matched != False:
            vars_to_values = matched  # clearer naming
            function = COMMANDS[command]
            # It's empty, which is {}
            if vars_to_values:
                variables = vars_to_values.keys()
                for var in variables:
                    value = vars_to_values[var]
                    function(value)
            # Just run without parameters
            else:
                function()
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
