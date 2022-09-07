# Напишите программу, в которой пользователь будет задавать две строки, 
# а программа - определять количество вхождений одной строки в другой.

strWhereSearch = input('Введите строку, где будем искать: ')
strWhatSearch = input('Введите строку, которую будем искать: ')

lenStrWhatSearch = len(strWhatSearch)
lenStrWhereSearch = len(strWhereSearch)
numberOfOccurrences = 0
i = 0
while (i <= lenStrWhereSearch - lenStrWhatSearch):
    if strWhatSearch == strWhereSearch[i:i + lenStrWhatSearch]:
        numberOfOccurrences += 1
    i += 1
print(numberOfOccurrences)