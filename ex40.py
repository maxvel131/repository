#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      legolas
#
# Created:     03.04.2015
# Copyright:   (c) legolas 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------

class Song(object):
    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print line

happy_bday = Song(["Happy Birthday to you",
                 "I don't want to get sued",
                 "So I'll stop right there"])

bulls_on_parade = Song(["They rally around the family",
                      "With pockets full of the shells"])

happy_bday.sing_me_a_song()
bulls_on_parade.sing_me_a_song()


