""" Задача: предложить улучшения кода для уже решённых задач:
С помощью использования **лямбд, filter, map, zip, enumerate, list comprehension """

# Задайте последовательность чисел. Напишите программу,
# которая выведет список неповторяющихся элементов исходной последовательности.
""" List comprehension """
# import numpy as np
# list_one = np.random.randint(0, 10, 20)
# print(list_one)
# list_two = []
# [list_two.append(x) for x in list_one if x not in list_two]
# print(list_two)
# list_three = list(set(list_one))
# print(list_three)
#____________________________________________________________________

# Задание 3 Задайте список из n чисел последовательности (1+1/n)^n и выведите на экран их сумму,
# округлённую до трёх знаков после точки
""" List comprehension """
# n = int(input('Введите число: '))
# print(round(sum([round((1 + 1 / x)**x, 3) for x in range(1, n + 1)]), 3))
#_____________________________________________________________________

# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример: - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
"""Lambda"""
# from functools import reduce
# my_list = list(map(int, input('Введите числа через пробел:\n').split()))
# res_list = my_list[1::2]
# print(reduce(lambda a, b: a + b, res_list))