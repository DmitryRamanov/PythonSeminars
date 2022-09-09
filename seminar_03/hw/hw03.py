# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между
# максимальным и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

lst = [1.1, 1.2, 3.1, 5, 10.01]
minValue,maxValue,tempValue = 1,0,0
# (1.1//1)
for i in lst:
    tempValue = abs(i - i//1)
    if tempValue < minValue:
        minValue = tempValue
    if tempValue > maxValue:
        maxValue = tempValue

print(f'{lst} -> {maxValue-minValue}')