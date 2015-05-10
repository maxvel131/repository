#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      legolas
#
# Created:     29.03.2015
# Copyright:   (c) legolas 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------

from sys import exit

def gold_room():
    print "This room is fool of gold. How much do you take?"

    next = raw_input("> ")
    if "0" in next or "1" in next:
        how_much = int(next)
    else:
        dead("Man learn to type a number.")

    if how_much <= 50:
        print "Nice! You are not greedy. You win!"
        exit(0)
    else:
        dead("You are greedy bastard!")

def bear_room():
    print "There is a bear here!"
    print "The bear has a bunch of honey."
    print "The fat bear is infront of another door."
    print "How are you going to move the bear?"
    bear_moved = False

    while True:
        next = raw_input("> ")

        if next == "take honey":
            dead("The bear looks at you than slaps your face off.")
        elif next == "taunt bear" and not bear_moved:
            print "The bear has moved from the door. You can go through it now."
            bear_moved = True
        elif next == "taunt bear" and bear_moved:
            dead("The bear get pissed off and chews your leg off.")
        elif next == "open door" and bear_moved:
            gold_room()
        else:
            print "I got no idea what that means."

def cthulhu_room():
    print "Here you see the great evil Cthulhu."
    print "He, it, whatever stares at you and you go insane."
    print "Do you flee for your life or eat your head."

    next = raw_input("> ")
    if "flee" in next:
        start()
    elif "head" in next:
        dead("Well that was tasty!")
    else:
        cthulhu_room()
def dead(why):
    print why, "Good job!"
    exit(0)

def start():
    print "You are in a dark room."
    print "There is a door to your right and left."
    print "Which one do you take?"

    next = raw_input("> ")

    if next == "left":
        bear_room()
    elif next == "right":
        cthulhu_room()
    else:
        dead("You stamble arounf the room until you starve.")

start()



