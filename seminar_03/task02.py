# В текстовом файле посчитать количество строк, 
# а также для каждой отдельной строки определить количество в ней символов и слов.

f = open('textfile.txt','r')
countLines = 0
countwordsInLines = []
countCharsInLines = []
for line in f:
    countLines+=1
    if line != '\n':
        countwordsInLines.append(line.count(' ') + 1)
    else:
        countwordsInLines.append(0)
    countCharsInLines.append(line.count('') -2)
f.close()
print(countLines)
print(countwordsInLines)
print(countCharsInLines)
