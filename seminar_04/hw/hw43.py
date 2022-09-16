# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

values = [int(i) for i in input('Введите последовательность чисел: ').split()]
# print(values)
result = []
for item in values:
    # print(f'{item} -> {values.count(item)}')
    if values.count(item) == 1:
        result.append(item)
print(result)
