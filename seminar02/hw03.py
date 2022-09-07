# Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.
valueN = abs(int(input('Введите число N: ')))
lst = []
sum = 0
for i in range(1,valueN+1):
    calcValue = round((1 + 1/i)**i,2)
    lst.append(calcValue)
    sum += calcValue

print(f'{lst} -> {sum}')