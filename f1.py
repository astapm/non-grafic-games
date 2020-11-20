#! /usr/bin/env python3

# Game "Dice-racing"
# The cars move through the cells with numbers from 0 to 100
# The car moves as many cells as there are points on the rolled dice
# The dice is rolled and the cars move automatically
# The winner is the car that first reaches the cell number 100
# Minimal graphic -- only cell numbers are displayed


import time
from random import randint

# intro
print('DICE-RACING\n'
      '| The cars move through the cells with numbers from 0 to 100\n'
      '| The car moves as many cells as there are points on the rolled dice\n'
      '| The dice is rolled and the cars move automatically\n'
      '| The winner is the car that first reaches the cell number 100\n'
      '| Minimal graphics -- only cell numbers are displayed\n') 

input("Enter to enjoy...\n")

# car A on start cell 0
car_a = 0

# car B on start cell 0
car_b = 0

print("START")
print("A B")

# if there are more than two cars, use the "or" operator
while (car_a < 100) and (car_b < 100):

    # rolled dice for car A
    car_a = car_a + randint(1,6)

    # rolled dice for car B
    car_b = car_b + randint(1,6)

    # display cell numbers
    print(car_a, car_b)

    # pause to assess the location of the cars
    time.sleep(4)
    
print("FINISH")