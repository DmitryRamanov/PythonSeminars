# Реализуйте алгоритм перемешивания списка
import random

lst = [i for i in input('Введите числа, разделяя из пробелом: ').split(' ')]
# print(lst)

newlst = []
for i in range(len(lst)):
    chosenStr = random.choice(lst)
    newlst.append(chosenStr)
    lst.remove(chosenStr)

print(newlst)