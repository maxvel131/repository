#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      legolas
#
# Created:     12.04.2015
# Copyright:   (c) legolas 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------

class Parent(object):
    def implicit(self):
        print "PARENT implicit()"

class Child(Parent):
    pass

dad = Parent()
son = Child()

dad.implicit
son.implicit
