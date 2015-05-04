#-------------------------------------------------------------------------------
# Name:        module4
# Purpose:
#
# Author:      legolas
#
# Created:     27.04.2015
# Copyright:   (c) legolas 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import turtle

class Circle:
    def __init__(self, r):
        self.pi = pi = 3.141
        self.r = r

    def squareArea (self):
        description = 'Caution! Add numbers in cm!'
        print(description)
        print(self.pi * (self.r * self.r))
        return

    def circleLength (self):
        print(2 * self.pi * self.r)
        return

    def circleDraw(self):
        for circle in range (36):
             turtle.forward(self.r)
             turtle.right(10)

firstData = Circle(15)
secondData = Circle(15)
thirdData = Circle(15)

thirdData.circleDraw()
firstData.squareArea()
secondData.circleLength()

