#! /usr/bin/env python

# Command line dice game 
# You can choose from 1 to 12 hex dice 
# After the roll, the points on the dice and the total amount of points are displayed 

from random import randint

# Enter the number of dices, but no more than 12
# Default 1 dice 
num_dices = input("Enter the number of dices (max. 12): ")
if num_dices.isdigit():
    num_dices = int(num_dices)
    if (num_dices > 12):
        num_dices = 1
else:
    num_dices = 1

print("Selected dices: ",num_dices,"\n")

# Roll the dice
choice = ""
while choice != "q":
    choice = input("Roll the dice <Enter>, exit - <q>")
    if choice != "q":
        sum_point = 0 # сумма очков всех кубиков
        for x in range(num_dices):
            point = randint(1,6)
            print("Dice #",x + 1," :",point)
            sum_point += point
        print("The sum of the points of all dice :",sum_point,"\n")

print("Game Over!")
