#! /usr/bin/env python

# Простая non-grafic гоночная игра
# В основе игры передвижение фишек по клеткам с помощью игрального кубика
# Игральный кубик реализован с помощью random.randint(1,6)
# Машинки ходят по клеткам с номерами от 0 до 100
# Кубик бросается и машинка передвигается автоматически
# Минимальная графика -- выводятся только номера ячеек
# Между ходами пауза посредством time.sleep(), чтобы оценить ситуацию


import time
from random import randint

# intro
print('ДАЙС-ГОНКИ\n'
      '| От двух до шести машинок ходят по клеткам с номерами от 0 до 100\n'
      '| Машинка едет на столько клеток, сколько выпало очков на брошенном кубике\n'
      '| Бросок кубика и передвижение машинки происходит автоматически\n'
      '| Побеждает машинка, которая первой доберётся до клетки 100\n'
      '| Минимальная графика -- выводятся только номера ячеек\n')

# Вводим количество машин в гонке
num_cars = input("Введиите количество машин в гонке (2-6): ")
if num_cars.isdigit():
    num_cars = int(num_cars)
    if (num_cars > 6) or (num_cars < 2):
        num_cars = 2
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

# Создаём лист номеров машинок
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

    for x in range(num_cars):
        list_cars[x] = list_cars[x] + randint(1,6)
        if (list_cars[x] >= 100) and (list_places[x] == 0):
            list_places[x] = places
            flag_places = 1
            print(out_table.format(*list_places))

    print(out_table.format(*list_cars))
    if flag_places == 1:
        places += 1
        flag_places = 0

    for x in range(num_cars):
        if list_places[x] == 0:
            flag_racing = 1

print("ФИНИШ".center(4*num_cars))
print(out_table.format(*list_places))

