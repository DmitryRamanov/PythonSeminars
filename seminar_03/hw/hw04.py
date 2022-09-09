# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

value,result = 45,''
print(bin(value))
while True:
    result = str(value % 2) + result
    value //= 2
    if value == 0:
        break
print(result)