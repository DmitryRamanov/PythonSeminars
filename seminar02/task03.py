# Напишите программу, которая принимает на вход число N и выдаёт последовательность из N членов.
# Пример:
# - Для N = 5: 1, -3, 9, -27, 81
valueN = abs(int(input('Введите число N: ')))
result = 0
for i in range(1,valueN + 1):
    if i == 1:
        result = 1
    else:
        result *= -3
    print(result,end=', ')