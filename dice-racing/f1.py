#! /usr/bin/env python

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
      '| The two to six cars move through the cells with numbers from 0 to 100\n'
      '| The car moves as many cells as there are points on the rolled dice\n'
      '| The dice is rolled and the cars move automatically\n'
      '| The winner is the car that first reaches the cell number 100\n'
      '| Minimal graphics -- only cell numbers are displayed\n') 

# Enter the number of cars in the race 
num_cars = input("Enter the number of cars in the race  (2-6): ")
if num_cars.isdigit():
    num_cars = int(num_cars)
    if (num_cars > 6) or (num_cars < 2):
        num_cars = 2
else:
    num_cars = 2

# Create a list of car numbers like "# 1", "# 2" etc. 
list_numcars = []
for x in range(num_cars):
    temp = "#" + str(x+1)
    list_numcars.append(temp)

# Create a list for recording the cell number of the car after each move
list_cars = [0]
for x in range(num_cars):
    list_cars.append(0)

# Create a list of places at the finish line. At the beginning the sheet is empty 
list_places = [" "]
for x in range(num_cars):
    list_places.append(" ")

# Create a field template for displaying cell numbers in tabular form 
out_table = "{:>3}"
for x in range(num_cars -1):
    out_table = out_table + "{:>4}"

# Finish position - incremented after each move crossing the finish line 
places = 1 
flag_places = 0 # finish crossing flag 

# Начало игры
flag_racing = 1 # race flag at the up 

print("Participating in the race ",num_cars,"cars")
print(out_table.format(*list_numcars)) # display car numbers 
print("START!".center(4*num_cars))

while flag_racing:
    # Making the move of all machines 
    flag_racing = 0 # race flag at the down

    # Pause to assess the situation in the race 
    time.sleep(4)

    # Throw the dice and move the machine across the cells. 
    # If the car reaches 100 points for the first time 
    # write its place in the list of places at the finish
    for x in range(num_cars):
        list_cars[x] = list_cars[x] + randint(1,6)
        if (list_cars[x] >= 100) and (list_places[x] == " "):
            list_places[x] = places
            flag_places = 1

    # displaying information about the position on the track 
    print(out_table.format(*list_cars))
    # display of information about places at the finish 
    print(out_table.format(*list_places))
    # increment the place at the finish line until the next car
    # and lower the flag of crossing the finish line 
    if flag_places == 1:
        places += 1
        flag_places = 0

    # Continue the race if at least one car has not crossed the finish line 
    for x in range(num_cars):
        if list_places[x] == " ":
            flag_racing = 1

print("FINISH!".center(4*num_cars))
print(out_table.format(*list_places)) # результаты гонки

