#This program demonstrates the BankAccount class.

import CellPhoneClass as c


    
def main():
       # Create an object from the Coin class.
       my_phone= c.CellPhone('Apple', 'iPhone15', 1099) 
       my_phone.set_retail_price (999)
       
       #mosquito = c.Insect(2,4,'Mosquito')
       #housefly = c.Insect(2,4,'Housefly')    # this creates an instance called 'my_coin' of the class 'Coin()'

       # Display the side of the coin that is facing up.
       print('Company Name:', my_phone.get_manufact())    
       print('Phone Model:', my_phone.get_model())    
       print('Phone Price:', my_phone.get_retail_price())    # notice you do not have to supply the argument/parameter

       # Toss the coin.
       #print('I am going to toss the coin ten times:')
       #for count in range(10):
           #my_coin.toss()

           

     
           
           # Display the side of the coin that is facing up.
           #print('This side is up:', my_coin.get_sideup())

           



# Call the main function.
main()
