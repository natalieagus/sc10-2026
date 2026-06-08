## OOP implementation of turn-based game
import random

# create a blueprint of an object
class Stats:
    def __init__(self, attack=0, defense=0):
        # set up the attributes
        self.attack = attack
        self.defense = defense

    def add_stats(self, other):
        # this function receives two Stats objects
        # need to create a NEW Stats containing the combi of both stats attributes
        return Stats(self.attack + other.attack, self.defense + other.defense)

    @property
    def power(self): # whenever you @property, make sure the func only has 1 arg
        # the purpose of this is to report a combi of attributes
        # and not to DO something (unlike regular methods)
        return self.attack + self.defense # power is a computed PROPERTY


    @property
    def dbl_stats(self):
        # this is a weird property function although it will technically run
        # property is usually used to report a value in a clean manner/compute a value on the fly
        # not to APPLY something to the instance
        self.attack = self.attack * 2
        self.defense = self.defense * 2
        return self.attack + self.defense

stat_one = Stats(10, 20) # instantiating a Stats object with 10 attack and 20 defense
stat_two = Stats(20, 30) # another instance of Stats object with 20 attack and 30 defense
stat_three = stat_one.add_stats(stat_two) # calling a method in the Stats class
print(stat_two.power)
