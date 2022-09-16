# Вычислить число c заданной точностью d
# Пример: - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$

# a = float(input('Введите число:\n'))
# n = len(input('Введите число для заданной точности:\n').split('.')[1])
# print(f"The value is: {a:.{n}f}")
#  ______________________________________________________________________

# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

# def get_primmary_factors(n):
#     factors = list()
#     devisor = 2
#     while (n // devisor >= 1):
#         if not n % devisor:
#             factors.append(devisor)
#             n = n // devisor
#         else:
#             devisor += 1
#     return factors
# print(list(set(get_primmary_factors(int(input('Введите число: '))))))
# ______________________________________________________________________

# Задайте последовательность чисел. Напишите программу,
# которая выведет список неповторяющихся элементов исходной последовательности.

# import numpy as np
# list_one = np.random.randint(0, 10, 20)
# print(list_one)
# list_two = []
# [list_two.append(x) for x in list_one if x not in list_two]
# print(list_two)
# list_three = list(set(list_one))
# print(list_three)
# ______________________________________________________________________

# Задана натуральная степень k. Сформировать случайным образом список коэффициентов
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример: - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

# import random
# def ratios(k):
#     lst = [random.randint(0, 101) for i in range(k + 1)]
#     return lst
# def create_str(sp):
#     lst = sp[::-1]
#     wr = ''
#     if len(lst) < 1:
#         wr = 'x = 0'
#     else:
#         for i in range(len(lst)):
#             if i != len(lst) - 1 and lst[i] != 0 and i != len(lst) - 2:
#                 wr += f'{lst[i]}x^{len(lst) - i - 1}'
#                 if lst[i + 1] != 0:
#                     wr += ' + '
#             elif i == len(lst) - 2 and lst[i] != 0:
#                 wr += f'{lst[i]}x'
#                 if lst[i + 1] != 0:
#                     wr += ' + '
#             elif i == len(lst) - 1 and lst[i] != 0:
#                 wr += f'{lst[i]} = 0'
#             elif i == len(lst) - 1 and lst[i] == 0:
#                 wr += ' = 0'
#     return wr
# k = int(input("Введите натуральную степень k = "))
# koef = ratios(k)
# with open('ratio.txt', 'w') as data:
#     data.write(create_str(koef))
# ______________________________________________________________________

