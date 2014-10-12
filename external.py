#! /c/Python27/python
# -*- coding: utf-8 -*-
from nyanbot import nyanbot_function

@nyanbot_function('ping [me]')
def pong():
	print 'ping'
