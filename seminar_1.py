# Задача на выходные дни:
# num_day = int(input('Введите день недели\n'))
# if num_day == 6 or num_day == 7:
#     print('Yes')
# elif num_day == num_day in range(1, 6):
#     print('No')
# else:
#     print('Error')
#_________________________________________________________

# Проверка истинности утверждения:
# for x in range (2):
#     for y in range (2):
#         for z in range (2):
#             print(x,y,z)
#             print(not (x or y or z) == (not x) and (not y) and (not z))
#__________________________________________________________

# Номер четверти:
# def coordinates(a,b):
#     if a == 0:
#         print('x cannot be 0')
#         while a == 0:
#             a = int(input('Введите координаты x:\n'))
#     elif b == 0:
#         print('y cannot be  0')
#         while b == 0:
#             b = int(input('Введите координаты y:\n'))        
#     return a,b
# def quarter(coord):
#     if coord[0] > 0 and coord[1] > 0:
#         print('1 Четверть')
#     elif coord[0] < 0 and coord[1] > 0:
#         print('2 Четверть')
#     elif coord[0] < 0 and coord[1] < 0:
#         print('3 Четверть')
#     elif coord[0] > 0 and coord[1] < 0:
#         print('4 Четверть')
# quarter(coordinates(int(input('Введите x:\n')),int(input('Введите y:\n'))))
#__________________________________________________________

#Диапазон координат:
# def coord(quarter):
#     if quarter == 1:
#         print('x > 0 and y > 0')
#     elif quarter == 2:
#         print('x < 0 and y > 0')
#     elif quarter == 3:
#         print('x < 0 and y < 0')
#     elif quarter == 4:
#         print('x > 0 and y < 0')
#     else:
#         print('Error')
# coord(int(input('Введите номер четверти:\n')))
#_________________________________________________________

#Расстояние между точками:
# A = [int(input('Введите координату "x" точки A:\n')), int(input('Введите координату "y" точки A:\n'))]
# B = [int(input('Введите координатy "x" точки B:\n')), int(input('Введите координатy "y" точки B:\n'))]
# print (round( (((A[0]-B[0])**2) + ((A[1]-B[1])**2)) **0.5, 3))