#! /usr/bin/env python

# Game "Dice-racing"
# The two cars move through the cells with numbers from 0 to 100
# The car moves as many cells as there are points on the rolled dice
# The dice is rolled and the cars move automatically
# The winner is the car that first reaches the cell number 100
# Minimal graphic -- only cell numbers are displayed


import time
from random import randint

# intro
print('DICE-RACING\n'
      '| The two cars move through the cells with numbers from 0 to 100\n'
      '| The car moves as many cells as there are points on the rolled dice\n'
      '| The dice is rolled and the cars move automatically\n'
      '| The winner is the car that first reaches the cell number 100\n'
      '| Minimal graphics -- only cell numbers are displayed\n') 

input("Enter to enjoy...\n")

# car 1 on start cell 0
car_1 = 0

# car 2 on start cell 0
car_2 = 0

print("START")
print("%3s%4s" % ("No1","No2"))

# if there are more than two cars, use the "or" operator
while (car_1 < 100) and (car_2 < 100):

    # pause to assess the location of the cars
    time.sleep(4)

    # rolled dice for car 1
    car_1 = car_1 + randint(1,6)

    # rolled dice for car 2
    car_2 = car_2 + randint(1,6)

    # display cell numbers
    print("%3d%4d" % (car_1, car_2))
    
print("FINISH")
