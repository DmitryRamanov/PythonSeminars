def GetInfoForFridge(numberOfFridge):
    result = input(f'Введите код из (5-100 символов) для {numberOfFridge} холодильника: ').lower()
    lenResult = len(result)
    
    while lenResult < 5 or lenResult > 100:
        print('Введеный код холодильника, не соот-вует допустимой длинне. Повторите ввод!')
        result = input(f'Введите код из (5-100 символов) для {numberOfFridge} холодильника: ').lower()
        lenResult = len(result)
    
    return result

numerOfFridges = abs(int(input('Введите кол-во холодильников: ')))
fridges = []
# fridges = [i for i in input('Введите код холодильника: ').split(',',numerOfFridges)]
for i in range(1, numerOfFridges + 1):
    fridges.append(GetInfoForFridge(i))

result = []
wordForSearch = 'anton'
for fridgeCode in fridges:
    prevCharIndex = 0
    curCharIndex = -1
    for i in wordForSearch:
        curCharIndex = fridgeCode.find(i, prevCharIndex)
        if curCharIndex == -1 or curCharIndex < prevCharIndex:
            prevCharIndex = 0
            curCharIndex = -1
            break
        prevCharIndex = curCharIndex
        curCharIndex = -1
    if prevCharIndex > 0:
        result.append(fridges.index(fridgeCode) + 1)

print(fridges)
print(result)