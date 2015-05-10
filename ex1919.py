#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      legolas
#
# Created:     09.03.2015
# Copyright:   (c) legolas 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def coffee_and_tea (coffee_types, tea_sorts, additional):
    print "We have %d." % coffee_types
    print "We also have %d." % tea_sorts
    print "Also additional %d.\n" % additional

print "General amount of coffee and tea:\n"
coffee_and_tea(150, 90, 25)

capuchino = 25
espresso = 15
tea = 17

coffee_and_tea(capuchino, espresso, tea)

print "Some more info:\n"
capuchino1 = 26
espresso1 = 16
tea1 = 18

coffee_and_tea(capuchino1, espresso1, tea1)

print "Let's make some math:\n"
coffee_and_tea(17+15, 25+17, 25+15+17)

print "Let's make another math:\n"
coffee_and_tea(capuchino1+1, tea1-1, espresso1+1)
