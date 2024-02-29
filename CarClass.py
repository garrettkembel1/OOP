# The BankAccount class simulates a bank account.

class Car:
    

# The __init__ method accepts an argument for
# the account's balance. It is assigned to
# the __balance attribute.

    def __init__(self, model, make, n):
        self.__year_model = model
        self.__make = make
        self.__speed = n
   
        

      # The deposit method makes a deposit into the
      # account.

    def set_year_model(self, model):
         self.__year_model = model

      # The withdraw method withdraws an amount
      # from the account.

    def set_make(self, make):
        self.__make = make

    def set_speed(self, speed):
        self.__speed = 0

    def accelerate (self):
        self.__speed += 5

    def brake (self):
        self.__speed -= 5


      # The get_balance method returns the
      # account balance.

    def get_year_model(self):
        return self.__year_model
    
    def get_make(self):
        return self.__make
    
    def get_speed(self):
        return self.__speed
    

