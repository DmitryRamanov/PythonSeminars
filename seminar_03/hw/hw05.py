# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

valueK = abs(int(input("Введите число: ")))
lst = [0]
if valueK >= 1:
    lst.insert(0, 1)
    lst.append(1)
    if valueK > 1:
        valuePrev2, valuePrev1 = 0, 1
        for i in range(2, valueK+1):
            lst.append(valuePrev1 + valuePrev2)
            (valuePrev2, valuePrev1) = (valuePrev1, valuePrev1 + valuePrev2)
            lst.insert(0, (-1) ** (i + 1) * valuePrev1)

print(lst)