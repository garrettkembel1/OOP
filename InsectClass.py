import random

# The Coin class simulates a coin that can
# be flipped.

class Insect:
    # The _ _init_ _ method initializes the
    # sideup data attribute with 'Heads'.

    def __init__(self): #(self) is requirment for every single instance
        self.wings = 2
        self.legs = 4
        self.flight = 0

    # The toss method generates a random number
    # in the range of 0 through 1. If the number
    # is 0, then sideup is set to 'Heads'.
    # Otherwise, sideup is set to 'Tails'.

    def length_of_flight(self):
        self.flight = random.randint(1,10)

    # The get_sideup method returns the value
    # referenced by sideup.

    def get_sideup(self):
            return self.flight
    # The get_sideup method returns the value
    # referenced by sideup.

   
