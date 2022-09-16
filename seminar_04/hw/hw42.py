# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

valueN: int = abs(int(input('Задайте положительное натуральное число: ')))
lst = []
# for i in range(2, valueN):
i: int = 2
while i <= valueN:
    if valueN % i == 0:
        lst.append(i)
        valueN /= i
        i = 2
    else:
        i += 1

print(lst)
