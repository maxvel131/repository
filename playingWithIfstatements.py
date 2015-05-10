#-------------------------------------------------------------------------------
# Name:        module3
# Purpose:
#
# Author:      legolas
#
# Created:     20.04.2015
# Copyright:   (c) legolas 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------

country = raw_input("Enter please your country:").upper()
language = raw_input("Enter please your native language:").upper()
city = raw_input("Enter please the capital of the country you are in:").upper()

if country =="BELARUS" and (language == "RUSSIAN" or language == "BELARUSSIAN"):
    print ("You're welcome to Minsk!")
    if city == "MINSK":
        print ("Enjoy the capital of the Belarus!")

if country == "UKRAINE" and (language == "RUSSIAN" or language == "UKRAINIAN"):
    print ("You're definitely in Kiev")
    if city == "KIEV":
        print ("Go to the Lavra!")

if country == "GERMANY" or country == "FRANCE":
    print("You're in the EU! You are lucky one! Enjoy it")
