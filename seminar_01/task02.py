# 2. Напишите программу, которая на вход принимает 5 чисел и находит максимальное из них.
# Примеры:
# - 1, 4, 8, 7, 5 -> 8
# - 78, 55, 36, 90, 2 -> 90

numberValues = 5
values = []

#values = [int(i) for i in input().split(',',numberValues-1)]
for i in range(0, numberValues):
    values.append(int(input(f'Введите {i + 1} число: ')))

#max(values) - штатная функция полученя макс значения в списке
maxValue = values[0]
for i in values:
    if maxValue < i:
        maxValue = i

print(f'{values} -> {maxValue}')