#! /usr/bin/env python3

# Игра "Гонки"
# Машинки ходят по клеткам с номерами от 0 до 100
# Машинка передвигантся на столько клеток, сколько выпадает очков на брошенном кубике
# Кубик бросается и машинка передвигается автоматически
# Побеждает машинка, которая первой доберётся до клетки №100
# Минимальная графика - выводятся только номера ячеек
# Максимальная реиграбельность

import time
from random import randint

# Вводим количество машин в гонке
num_cars=0
while(num_cars > 6) or (num_cars < 2):
    num_cars = input("How many cars (2-6)?: ")
    if num_cars.isdigit():
        num_cars = int(num_cars)
    else:
        num_cars = 2

# Создаём лист номеров ячеек для машинок
list_cars = [0]
for x in range(num_cars):
    list_cars.append(0)

# Создаём лист мест на финише
list_places = [0]
for x in range(num_cars):
    list_places.append(0)

# Создаём лист номеров для номеров машинок
list_numcars = []
for x in range(num_cars):
    temp = "#" + str(x+1)
    list_numcars.append(temp)

# Создаём шаблон для вывода номеров ячеек
out_table = "{:>3}"
for x in range(num_cars -1):
    out_table = out_table + "{:>4}"

places = 1
flag_places = 0

# Поднимаем флаг гонки
flag_racing = 1

print("В гонке участвуют",num_cars,"машин")
print(out_table.format(*list_numcars))
print("START!".center(4*num_cars))

while flag_racing:
    # Ход всех машинок
    flag_racing = 0
    # пауза чтобы оценить ситуацию в гонке
    time.sleep(4)
    count = 0
    while(count < num_cars):
        list_cars[count] = list_cars[count] + randint(1,6)
        if (list_cars[count] >= 100) and (list_places[count] == 0):
            list_places[count] = places
            flag_places = 1
            print(out_table.format(*list_places))
        count += 1
    print(out_table.format(*list_cars))
    if flag_places == 1:
        places += 1
        flag_places = 0
    count = 0
    while(count < num_cars):
        if list_places[count] == 0:
            flag_racing = 1
        count += 1

print("ФИНИШ".center(4*num_cars))
print(out_table.format(*list_places))
