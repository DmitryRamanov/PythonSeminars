# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
# Пример:
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

from math import sqrt

def getPointCoordinat():
    x = int(input('Введите координату x: '))
    y = int(input('Введите координату y: '))
    point = [x,y]
    return point

print('Введите координаты точки A')
pointA = getPointCoordinat()

print('Введите координаты точки B')
pointB = getPointCoordinat()

result = round(sqrt((pointB[0] - pointA[0])**2 + (pointB[1] - pointA[1])**2),3)
print(f'A({pointA}); B({pointB}) -> {result}')
