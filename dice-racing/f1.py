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

## Параметры трассы
# Количество клеток трассы
track_cells = 100

# Повороты
turns = []

# Погода
weather = ""

# Место на финише -- инкременируется после каждого хода с пересечением финиша
places = 1

# Флаг пересечения финиша 
flag_places = 0

# Число секунд паузы между ходами для оценки ситуации на трассе
sleep = 4

# Список названий команд и их трёхбуквенных сокращений
names_teams = "Мерседес", "Феррари", "Рено", "Ред Булл", "МакЛарен", "Маруся"
short_names_teams = "МРСc", "ФЕР", "РЕН", "РБЛ", "МКЛ", "МАР"

## Создаём таблицу заезда

# Номер машины
# Команда
# Краткое имя команды
# Текущие шины
# Деградация шин
# Текущая клетка
# Финишная клетка
# Текущая передача
# Финишная передача
# Статус машины в гонке

# Список номеров машин 
numers = list(range(1, num_cars + 1))
# numers = list(n for n in range(num_cars))

# Список команд
teams = names_teams[:num_cars]
# teams = [names_teams[x] for x in range(num_cars)]
short_names = short_names_teams[:num_cars]

# Текущие шины
tires = [None]*num_cars
# tires = [None for _ in range(num_cars)]

# Текущая клетка
cell = [0]*num_cars

# Финишная клетка
end_cell = [None]*num_cars

# Текущая передача/скорость
transmission = [None]*num_cars

# Передача/скорость на финише
end_transmission = [None]*num_cars

# Деградация шин
tires_degradation = [None]*num_cars

# Статус машины в гонке
status = [" "]*num_cars

## Создаём шаблон полей для вывода в табличном виде номеров ячеек и инфо-строки
out_table = "{:>3}"+"{:>4}"*(num_cars - 1)

## Начало игры
flag_racing = 1 # флаг гонки вверху

## Функция броска игральной кости и передвижение по клеткам
def roll(x):
    return x + randint(1,6)

print("В гонке участвуют",num_cars,"машин")
print(out_table.format(*numers)) # выводим номера машин
print(out_table.format(*short_names)) # выводим короткие названия
print("СТАРТ!".center(4*num_cars))

while " " in status:
    # пауза чтобы оценить ситуацию в гонке
    time.sleep(4)
    # Бросаем кубик и передвигаем машинку
    for x in range(num_cars):
        if cell[x] < track_cells:
            cell[x] = cell[x] + randint(1,6)
        else:
            status[x] = "F"
    # cell = map(roll, cell)
    # cell = [points + randint(1,6) for points in cell if int(points) < 100]
    print(out_table.format(*cell))  # вывод информации о позиции на трассе
    print(out_table.format(*status)) # вывод информации о местах на финише
