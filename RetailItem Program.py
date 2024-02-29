#This program demonstrates the BankAccount class.

import Retailitem as c



#CoinClass is name of file CoinClass.py - need to import file to use code


# The main function.

       # Create an object from the Coin class.
Jacket = c.Retailitem('Jacket',12,59.95)
Designer_Jeans = c.Retailitem('Designer Jeans',40,34.95)
Shirt = c.Retailitem('Shirt',20,24.95)  # this creates an instance called 'my_coin' of the class 'Coin()'

#Jacket.length_of_flight()
#Designer_Jeans.length_of_flight()
#Shirt.length_of_flight()

print(f'Item 1 is the {Jacket.get_Description()} has an inventory of {Jacket.get_Units_In_Inventory()}, and a price of  {Jacket.get_Price()}.')
print(f'Item 2 is the {Designer_Jeans.get_Description()} has an inventory of {Designer_Jeans.get_Units_In_Inventory()}, and a price of  {Designer_Jeans.get_Price()}.')
print(f'Item 3 is the {Shirt.get_Description()} has an inventory of {Shirt.get_Units_In_Inventory()}, and a price of  {Shirt.get_Price()}.')


       # Display the side of the coin that is facing up.
      
