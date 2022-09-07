# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# - 6782 -> 23
# - 0,56 -> 11

value = float(input('Введите число: '))
valueStr = str(value)
result = 0
for i in range(len(valueStr)):
    # print(valueStr[i:i+1])
    if valueStr[i:i+1].isdigit():
        result += int(valueStr[i:i+1])

print(f'{value} -> {result}')