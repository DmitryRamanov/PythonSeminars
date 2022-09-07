# Орел и решко

stringEngValue = 'OOOOOOPPPOPOPPPPPP'.upper()
charToCalc = 'p'.upper()
countRepeatedCharToCalc = 0
maxCountRepeatedCharToCalc = 0
for i in stringEngValue:
    if i == charToCalc:
        countRepeatedCharToCalc +=1
        if maxCountRepeatedCharToCalc < countRepeatedCharToCalc:
            maxCountRepeatedCharToCalc = countRepeatedCharToCalc
    else:
        countRepeatedCharToCalc = 0
print(f'{stringEngValue} -> {maxCountRepeatedCharToCalc}')

