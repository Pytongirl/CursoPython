from random import randint

class Dice:
    """A class representing a single dice"""

    def _init_(self, num_sides=6):
        self.num_sides = num_sides

    def roll(self):
        return randint (1,self.num_sides)
dice = Dice()

for x in range(100):
    print(dice.roll())