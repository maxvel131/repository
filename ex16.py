#-------------------------------------------------------------------------------
# Name:        ??????1
# Purpose:
#
# Author:      legolas
#
# Created:     04.03.2015
# Copyright:   (c) legolas 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------


from sys import argv

script, filename = argv

print "We are going to erase %r." % (filename)
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN"

raw_input("?")

print "Opening the file..."
target = open(filename, 'w')

print "Truncating the file. Goodbye!"
target.truncate()

print "Now I am going to write these to the file."

line1 = raw_input("line1: ")
line2 = raw_input("line2: ")
line3 = raw_input("line3: ")

print "I am going to write these to the file."

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print "And finally, we close it."
target.close()












