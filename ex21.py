#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      legolas
#
# Created:     10.03.2015
# Copyright:   (c) legolas 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def add(a, b):
    print "ADDING %d + %d" % (a, b)
    return a + b
def subtract(a, b):
    print "SUBTRACTING %d - %d" % (a, b)
    return a - b
def multiply(a, b):
    print "MULTIPLYING %d * %d" % (a, b)
    return a * b
def divide(a, b):
    print "DIVIDING %d / %d" % (a, b)
    return a / b

print "Let's do some math with just functions!"

age = add(20, 7)
height = subtract(200, 25)
weight = multiply(40, 2)
iq = divide(250, 2)

print "Age: %d, Height: %d, Weight: %d, IQ: %d" % (age, height, weight, iq)

# A puzzle for the extra credit, type it in anyway
print "Here is a puzzle."

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))
print "That becomes: ", what, "Can you do it by hand?"










