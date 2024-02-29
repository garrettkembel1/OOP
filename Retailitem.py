# The BankAccount class simulates a bank account.

class Retailitem:
    

# The __init__ method accepts an argument for
# the account's balance. It is assigned to
# the __balance attribute.

    def __init__(self, desc, inv, price):
        self.__Description = desc
        self.__Units_In_Inventory = inv
        self.__Price = price
   
        

      # The deposit method makes a deposit into the
      # account.

    def set_Description(self, desc):
         self.__Description = desc

      # The withdraw method withdraws an amount
      # from the account.

    def set_Units_In_Inventory(self, inv):
        self.__Units_In_Inventory = inv

    def set_Price(self, Price):
        self.__Price = Price


      # The get_balance method returns the
      # account balance.

    def get_Description(self):
        return self.__Description
    
    def get_Units_In_Inventory(self):
        return self.__Units_In_Inventory
    
    def get_Price(self):
        return "${:,.2f}".format(self.__Price)
    


