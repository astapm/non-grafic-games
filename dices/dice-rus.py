#! /usr/bin/env python

# Игра "Игральные кубики" для командной строки
# Можно выбрать от 1 до 12 шестигранных кубиков
# После броска выводится очки на кубиках и общая сумма очков

from random import randint

# Вводим количество кубиков, но не более 12.
# По умолчвнию 1 кубик.
num_dices = input("Введите количество кубиков(макс. 12): ")
if num_dices.isdigit():
    num_dices = int(num_dices)
    if (num_dices > 12):
        num_dices = 1
else:
    num_dices = 1

print("Выбрано кубиков: ",num_dices,"\n")

# Бросаем кубики
choice = ""
while choice != "q":
    choice = input("Бросаем кубики <Ввод>, выход - <q> ")
    if choice != "q":
        sum_point = 0 # сумма очков всех кубиков
        for x in range(num_dices):
            point = randint(1,6)
            print("Кубик №",x + 1," :",point)
            sum_point += point
        print("Сумма очков всех кубиков :",sum_point,"\n")

print("Game Over!")
