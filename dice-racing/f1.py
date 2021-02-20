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

# Параметры трассы
# Количество клеток трассы
track_cells = 100

# Повороты
turns = []

# Погода
weather = ""

# Список названий команд и их трёхбуквенных сокращений
names_teams = ["Мерседес", "Феррари", "Рено", "Ред Булл", "МакЛарен", "Маруся"]
short_names_teams = ["Мер", "Фер", "Рен", "Ред", "Мак", "Мар"]

# Создаём таблицу заезда
# Список номеров машин 
numers = list(range(1, num_cars + 1))
# numers = list(n for n in range(num_cars))
names = []
short_names = []
tires = []
cells = []
end_point = []


