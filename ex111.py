#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      legolas
#
# Created:     30.03.2015
# Copyright:   (c) legolas 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------

hour = int(raw_input("Enter hour "))
minute = int(raw_input("Enter minute "))
sec = int(raw_input("Enter second "))

currentTime = hour, minute, sec

print "The current time is: " , currentTime

print "The time in seconds since midnight is", \
    (currentTime[0]* 3600 + currentTime[1]*60 + currentTime[2])