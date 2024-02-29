#This program demonstrates the BankAccount class.

import CarClass as c



#CoinClass is name of file CoinClass.py - need to import file to use code


# The main function.
def main():

       # Create an object from the Coin class.
    my_car = c.Car(2011,'Toyota 4Runner',45)
  # this creates an instance called 'my_coin' of the class 'Coin()'
    print('\n')
    print(f'The vehicle is a {my_car.get_year_model()} {my_car.get_make()}, and a has a beginning speed of {my_car.get_speed()}.')

    print('\n')
    print("Accelerating:")
    for i in range(5):
        my_car.accelerate()
        print("Current speed:", my_car.get_speed())
        

    
    print('\n')
    print("Braking:")
    for i in range(5):
        my_car.brake()
        print("Current speed:", my_car.get_speed())
       # Display the side of the coin that is facing up.
      
main()