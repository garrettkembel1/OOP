import random

# The Coin class simulates a coin that can
# be flipped.

class Insect:
    # The _ _init_ _ method initializes the
    # sideup data attribute with 'Heads'.

    def __init__(self,w,l,n): #(self) is requirment for every single instance
        self.wings = w
        self.legs = l
        self.flight = 0
        self.name = n


    # The toss method generates a random number
    # in the range of 0 through 1. If the number
    # is 0, then sideup is set to 'Heads'.
    # Otherwise, sideup is set to 'Tails'.

    def length_of_flight(self):
        self.flight = random.randint(1,10)

    # The get_sideup method returns the value
    # referenced by sideup.

    def get_flight(self):
            return self.flight
    
    def get_name(self):
            return self.name
    # The get_sideup method returns the value
    # referenced by sideup.

   
