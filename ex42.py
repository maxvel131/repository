#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      legolas
#
# Created:     07.04.2015
# Copyright:   (c) legolas 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------

## Animal is-a object(yes, sort of confusing) look at the extra credit
class Animal(object):
    pass

## Dog is-a class of class Animal
class Dog(Animal):

    def __init__(self, jeck):
        ## defining a function with a parameter Jeck
        self.jeck = jeck

## Cat is-a class of slass Animal
class Cat(Animal):

    def __init__(self, meow):
        ## defining a function with a parameter Meow
        self.meow = meow

## creating a class Person
class Person(object):
    ## Person ia-a class
    def __init__(self, name):
        self.name = name
        ## Person has-a pet of some kind
        self.pet = None

class Employee(Person):
    def __init__(self, name, salary):
        ## what is this strange magic?
        super(Employee, self).__init__(name)
        ## class super which has-a relationship with class Person
        self.salary = salary

## fish is-a object
class Fish(object):
    pass
## class salmon has-a relationship with class fish
class Salmon(object):
    pass
## class halibut has-a relationship with class fish
class Halibut(object):
    pass

## rover is-a dog
rover = Dog("Rover")
## satan is-a cat
satan = Cat("Satan")
## mary is-a person
mary = Person("Mary")
## ??
mary.pet = satan
##??
frank = Employee("Frank", 12000)
## ??
frank.pet = rover

flipper = Fish()

## ??
crouse = Salmon()

## ??
harry = Halibut()
























