#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      legolas
#
# Created:     01.05.2015
# Copyright:   (c) legolas 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------

class CoffeeMaker:

    def __init__(self, sugar, cinnamon):
        self.cost = cost = 10
        self.sugar = sugar
        self.cinnamon = cinnamon

    def espresso(self):
        print("""Dear customer, you have ordered espresso coffee!\n""")
        self.sugar = input('How many spoons of sugar you like?')

        if 1 == self.sugar <=3 :
            print ("I wish it's enough for you!")
        else:
            print ("You eat too much sugar man!")

        self.cinnamon = raw_input("Would you like some cinnamon?").upper()

        if self.cinnamon == 'YES' and (1 == self.sugar <=3):
            print("Please enjoy your espresso with cinnamon and sugar!")
        else:
            print("Please enjoy your espresso with cinammon!\n\n")
        print('Have a great day and I hope to see you soon!\n')
        print('____________________________________________')
        return

coffeeCup = CoffeeMaker(1,1)
coffeeCup.espresso()
