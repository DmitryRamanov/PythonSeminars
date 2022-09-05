# 4. Напишите программу, которая будет принимать на вход дробь и показывать первую цифру дробной части числа.
# *Примеры: *
# - 6, 78 -> 7
# - 5 -> нет
# - 0, 34 -> 3

value = str(float(input('Введите число: ')))
listValue = value.split('.')
#print(listValue)

if listValue[1] == '0':
      result = 'нет'
else:
    result = listValue[1][0]

print(f'{value} -> {result}')

# value = float(input('Введите число: '))
# print(int((value * 10) % 10))

# d1 = int((d*10) % 10)
# print(d1)
