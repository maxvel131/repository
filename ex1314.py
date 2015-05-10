#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      legolas
#
# Created:     01.03.2015
# Copyright:   (c) legolas 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------

from sys import argv

script, project, story = argv
prompt = ">>> "

print "This is a %s which has a %s , little story." % (project, story)
print "Okay, let's start your %s!!!!" %(story)

print "Could you tell me your name please?"
name = raw_input(prompt)

# First I need to ask question and then write in an answer, after prompt

print "How old are you %s?" % (name)
years = raw_input(prompt)

# Here is the same, more questions, more variable I have to create

print "Oooooookay, let's continue, you become more interesting for me %s)))" %(name)
print "Which is your favorite colour?"
colour = raw_input(prompt)

# Again questions and again new answers

print "Tell me please about your size %s?" % (name)
size = raw_input(prompt)

# Here is gonna be the final conclusion and information, after all Fragen got Antworten.

print "I didn't expect it.....that's interesting!!!!!!"

print "Okay, last question, for you %s, tell me where would you like to go, I mean the city?" % (name)
city = raw_input(prompt)

print """ Okay %s this is a little  %s about you,
you're %s years old, and you have %s which is my favorite,
besides, you your favorite colour is %s, mmmmm such a good cvolour))) Okay and the last thing,
about it! you will go to the %s after somebody will read your %s on "www.buyTICKETforme.com"
.....Good Luck!.""" % (name, story, years,
size, colour, city, story)

# Some Antworten can be stupid and will not fit to the text

# I am going to create a txt file......fuck...I am boring, not today....

