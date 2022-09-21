# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

# with open('file2.txt', 'w+') as data:
#     data.writelines('абвешка абв fsz wefef hello worldабв\n')
#     data.seek(0, 0)
#     print('Иcходный текст: ')
#     print(data.readlines())
#     data.seek(0, 0)
#     data.writelines(" ".join(filter(lambda x: 'абв' not in x, data.readline().split())))
#     data.seek(0, 0)
#     print('Итоговый текст: ')
#     print(data.readlines()[1:])

# _______________________________________________________________________

"""
Создайте программу для игры с конфетами человек против человека.
Условие задачи: На столе лежит 201 конфета. Играют два игрока делая ход друг после друга.
Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
Все конфеты оппонента достаются сделавшему последний ход.
Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
a) Добавьте игру против бота
b) Подумайте как наделить бота ""интеллектом""
"""

# import random
# candy = 201
# while (True):
#     print(f'Осталось {candy} конфет')
#     if (candy > 0):
#         print("\033[32m {}".format('Ход игрока!'))
#         player = int(input("\033[34m {}" .format('Сколько конфет хотите забрать?\n')))
#         while (True):
#             if player > 28:
#                 print("\033[31m {}" .format('Больше 28 конфет брать нельзя!'))
#                 player = int(input("\033[34m {}".format('Так сколько в итоге возьмете?\n')))
#             else:
#                 break
#         candy -= player
#         vinner = 'Ура, Вы победили!!!'
#     if (candy > 0):
#         print("\033[33m {}".format('Ход компьютера!'))
#         if (29 < candy < 58):
#             comp = (candy - 29)
#         elif (candy <= 28):
#             comp = candy
#         else:
#             comp = random.randrange(1, 28)
#         print("\033[33m {}" .format(f'Компьютер взял {comp} конфет!\033[0m'))
#         candy -= comp
#         vinner = 'Увы... Компьютер победил!'
#     else:
#         print("\033[36m {}" .format(f'{vinner}'))
#         break
# _______________________________________________________________________

# Создайте программу для игры в ""Крестики-нолики"".

# board = list(range(1,10))
# def draw_board(board):
#     print ("-" * 13)
#     for i in range(3):
#         print ("|", board[0+i*3], "|", board[1+i*3], "|", board[2+i*3], "|")
#         print ("-" * 13)
#
# def take_input(player_token):
#     valid = False
#     while not valid:
#         player_answer = input("Куда поставим " + player_token + "? ")
#         try:
#             player_answer = int(player_answer)
#         except:
#             print("Некорректный ввод. Вы уверены, что ввели число?")
#             continue
#         if player_answer >= 1 and player_answer <= 9:
#             if (str(board[player_answer-1]) not in "XO"):
#                 board[player_answer-1] = player_token
#                 valid = True
#             else:
#                 print("Эта клетка уже занята")
#         else:
#             print("Некорректный ввод. Введите число от 1 до 9 чтобы совершить ход.")
#
# def check_win(board):
#     win_coord = ((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6))
#     for each in win_coord:
#         if board[each[0]] == board[each[1]] == board[each[2]]:
#             return board[each[0]]
#     return False
#
# def main(board):
#     counter = 0
#     win = False
#     while not win:
#         draw_board(board)
#         if counter % 2 == 0:
#             take_input("X")
#         else:
#             take_input("O")
#         counter += 1
#         if counter > 4:
#             tmp = check_win(board)
#             if tmp:
#                 print (tmp, "выиграл!")
#                 win = True
#                 break
#         if counter == 9:
#             print ("Ничья!")
#             break
#     draw_board(board)
#
# main(board)

# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

# def zip(txt):
#     count = 1
#     res = ''
#     for i in range(len(txt)-1):
#         if txt[i] == txt[i+1]:
#             count += 1
#         else:
#             res = res + str(count) + txt[i]
#             count = 1
#     if count > 1 or (txt[len(txt)-2] != txt[-1]):
#         res = res + str(count) + txt[-1]
#     return res
#
# def unzip(txt):
#     number = ''
#     res = ''
#     for i in range(len(txt)):
#         if not txt[i].isalpha():
#             number += txt[i]
#         else:
#             res = res + txt[i] * int(number)
#             number = ''
#     return res
#
# text = input("Введите текст для кодировки: ")
# print(f"Текст после кодировки: {zip(text)}")
# print(f"Текст после дешифровки: {unzip(zip(text))}")

