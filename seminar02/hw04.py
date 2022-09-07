# Задайте список из N элементов, заполненных числами из промежутка[-N, N]. 
# Найдите произведение элементов на указанных позициях. 
# Позиции хранятся в файле file.txt в одной строке одно число.

valueN = abs(int(input('Введите значение N: ')))
lst = []
for i in range(-valueN, valueN+1):
    lst.append(i)

multiplicationValue = 1
positions = []
f = open('text.txt', 'r')
for line in f:
    line = line.replace('\n', '')
    if line.isdigit():
        positions.append(line)
        multiplicationValue *= lst[int(line)-1]
print(f'{lst} -> {positions} -> {multiplicationValue}')