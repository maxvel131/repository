#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      legolas
#
# Created:     16.05.2015
# Copyright:   (c) legolas 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------
class Employee:
# The function __init__() is a initializer or constructor.
# If not present it will be called implicitly to form the object.
# If created implicitly it will do a whatever is there in the function's body.
# Self has to be passed explicitly.
    def __init__(self, name, position,rank):
        self.name = name
        self.position = position
        self.rank = rank

        if self.rank == 1:
            self.basic_income=10000

        elif self.rank == 2:
            self.basic_income = 9000

        else:
            self.basic_income = 8000
        self.allowance = 500

    def __str__(self):
        return "NAME: " + self.name +"\nPOSITION" + self.position

    def bonus(self, overtime):
        self.overtime = overtime
        self.bonus = 500*overtime

    def income(self):
        self.income = self.basic_income + self.allowance + self.bonus
        return self.income

empl1 = Employee("Mykhailo","programmer", 1)

empl1.bonus(12)
print(empl1)
print(empl1.name +" " + "earns" + " " + str(empl1.income()))