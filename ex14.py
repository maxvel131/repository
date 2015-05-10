#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      legolas
#
# Created:     21.02.2015
# Copyright:   (c) legolas 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------

from sys import argv

script, user_name = argv
prompt = '> '

print "Hi %s, I am the %s script." % (script, user_name)
print "I would like to ask you a few questions."
print "Do you like my %s?" % user_name
likes = raw_input(prompt)
lives = raw_input(prompt)

print "Where do you live %s?" % user_name
computer = raw_input(prompt)

print"""
Alright, so you said %r about liking me.
You live in %r. Not sure where that is.
And you have %s computer. Nice.
""" % (likes, lives, computer)





