#! /usr/bin/env python

# Простая non-grafic гоночная игра с игральным кубиком
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
      '| Минимальная графика -- выводятся только номера клеток\n')

# Вводим количество машин в гонке
num_cars = input("Введиите количество машин в гонке (2-6): ")
if num_cars.isdigit():
    num_cars = int(num_cars)
    if (num_cars > 6) or (num_cars < 2):
        num_cars = 2
else:
    num_cars = 2

# Создаём лист номеров машинок типа "#1","#2" etc.
list_numcars = []
for x in range(num_cars):
    temp = "#" + str(x+1)
    list_numcars.append(temp)

# Создаём лист для записи номера ячейки после каждого хода для каждой машинки 
list_cars = [0]
for x in range(num_cars):
    list_cars.append(0)

# Создаём лист мест на финише. В начале лист пустой
list_places = [" "]
for x in range(num_cars):
    list_places.append(" ")

# Создаём шаблон полей для вывода в табличном виде номеров ячеек
out_table = "{:>3}"
for x in range(num_cars -1):
    out_table = out_table + "{:>4}"

# Место на финише -- инкременируется после каждого хода с пересечением финиша
places = 1 
flag_places = 0 # флаг пересечения финиша

# Начало игры
flag_racing = 1 # флаг гонки вверху

print("В гонке участвуют",num_cars,"машин")
print(out_table.format(*list_numcars)) # выводим номера машин
print("СТАРТ!".center(4*num_cars))

while flag_racing:
    # Ход всех машинок
    flag_racing = 0 # флаг гонки внизу

    # пауза чтобы оценить ситуацию в гонке
    time.sleep(4)

    # Бросаем кубики и перемещвем машинку по ячейкам.
    # Если машинка в первый раз достигает 100 очков
    # записываем её место в лист мест на финише 
    for x in range(num_cars):
        list_cars[x] = list_cars[x] + randint(1,6)
        if (list_cars[x] >= 100) and (list_places[x] == " "):
            list_places[x] = places
            flag_places = 1

    print(out_table.format(*list_cars))  # вывод информации о позиции на трассе
    print(out_table.format(*list_places)) # вывод информации о местах на финише
    # инкрементируем место на финише для следующего пересечения
    # и опускаем флаг пересечения финиша
    if flag_places == 1:
        places += 1
        flag_places = 0

    # Продолжаем гонку, если хоть одна машинка не пересекла финиш
    for x in range(num_cars):
        if list_places[x] == " ":
            flag_racing = 1

print("ФИНИШ!".center(4*num_cars))
print(out_table.format(*list_places)) # результаты гонки



