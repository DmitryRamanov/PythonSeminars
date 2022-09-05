# 5. Напишите программу, которая принимает на вход число и проверяет, кратно ли оно 5 и 10 или 15, но не 30.

value = int(input('Введите число: '))

result = ((value % 5 == 0 and value % 10 == 0) or (
    value % 15 == 0)) and not (value % 30 == 0)

print(f'{value} -> {result}')