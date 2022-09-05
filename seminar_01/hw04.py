# Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти(x и y).

from zoneinfo import available_timezones


value = int(input('Введите номер четверти [1..4]: '))
available_quarters = [1,2,3,4]
while not (value in available_quarters):
    print('Введено не корректное значение, повторите ввод!')
    value = int(input('Введите номер четверти [1..4]: '))

result = None
if value == 1:
    result = 'x > 0 and y > 0'
elif value == 2:
    result = 'x < 0 and y > 0'
elif value == 3:
    result = 'x < 0 and y < 0'
elif value == 4:
    result = 'x > 0 and y < 0'
else:
    result = 'диапазон возможных координат не определен'

print(f'{value} -> {result}')
