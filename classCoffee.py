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

class Coffee:
    def __init__(self):
        self.coffee8Gramm = coffee8Gramm = 8
        self.milk = milk = 150
        self.sugar = raw_input('How many spoons of sugar you need?')
        self.foam = foam = 50

    def espresso(self):
        self.structure = ['coffee8Gramm']
        print(self.structure)
        self.structure.append('cinnamon')
        print(self.structure)
        return

    def latte(self):
        print('Thank you for ordering our coffee!\n')
        self.structure1 = {'coffee8Gramm':8,
        'milk':150, 'foam':25}
        print(self.structure1)
        self.sentence = "The best latte you drink id you add cyrop!"
        print(self.sentence)
        self.sentence.replace('cyrop', 'CHOCOLATE')

    def capuccino(self):
        self.structure2 = {'coffee8Gramm':8,
        'foam':50}
        print(self.structure2)


cupOfCofee = Coffee()
cupOfCofee.espresso()

cupOfCofee.latte()







