# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]
lst = [2, 3, 4, 5, 6]
result = []
lstlen = len(lst)
rangBorder = lstlen//2
if lstlen % 2 != 0:
    rangBorder += 1
for i in range(rangBorder):
    result.append(lst[i] * lst[lstlen-i-1])

print(f'{lst} -> {result}')