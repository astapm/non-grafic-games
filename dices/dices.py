#! /usr/bin/env python

# Game "Dices"

from random import randint

# Вводим количество кубиков
# но не более 25. По умолчвнию 1 кубик
num_dices = input("Введиите количество кубиков(макс. 25): ")
if num_dices.isdigit():
    num_dices = int(num_dices)
    if (num_dices > 25):
        num_dices = 1
else:
    num_dices = 1

print("Выбрано кубиков: ",num_dices,"\n")

# Бросаем кубики
choice = ""
while choice != "q":
    choice = input("Бросаем кубики? <любая клавиша>, <q> - выход ")
    if choice != "q":
        sum_point = 0 # сумма очков всех кубиков
        for x in range(num_dices):
            point = randint(1,6)
            print("Кубик №",x," :",point)
            sum_point += point
        print("Сумма очков всех еубиков :",sum_point,"\n")


print("Game Over!")
