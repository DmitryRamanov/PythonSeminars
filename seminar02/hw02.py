# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

def CalcNewValue(value):
    if value == 1:
        return 1
    return value * CalcNewValue(value - 1)

valueN = int(input('Введите значение N: '))
for i in range(1, valueN + 1):
    print(CalcNewValue(i),end=', ')
