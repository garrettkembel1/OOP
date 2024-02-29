# The BankAccount class simulates a bank account.

class CellPhone:
    

# The __init__ method accepts an argument for
# the account's balance. It is assigned to
# the __balance attribute.

    def __init__(self, manufact, model, retail_price):
        self.__manufacturer = manufact
        self.__model = model
        self.__retail_price = retail_price
        

      # The deposit method makes a deposit into the
      # account.

    def set_manufact(self, manufact):
        self.__manufacturer = manufact

      # The withdraw method withdraws an amount
      # from the account.

    def set_model(self, model):
        self.__manufacturer = model

    def set_retail_price(self, retail_price):
        self.__retail_price = retail_price


      # The get_balance method returns the
      # account balance.

    def get_manufact(self):
        return self.__manufacturer
    
    def get_model(self):
        return self.__model
    
    def get_retail_price(self):
        return "${:,.2f}".format(self.__retail_price)

