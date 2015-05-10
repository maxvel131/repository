#-------------------------------------------------------------------------------
# Name:        module3
# Purpose:
#
# Author:      legolas
#
# Created:     21.04.2015
# Copyright:   (c) legolas 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import turtle
numberSteps = 5
for steps in range(numberSteps):
    turtle.forward(50)
    turtle.color('dark green')
    turtle.right(60)
    for secondstep in range(numberSteps):
        turtle.color('red')
        turtle.forward(100)
        turtle.right(60)



