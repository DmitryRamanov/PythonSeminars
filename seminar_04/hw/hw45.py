# Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.

def createfile(filename, polynomial):
    with open(filename, 'w') as file:
        file.write(polynomial)
    return

filename1 = 'hw45file1.txt'
filename2 = 'hw45file2.txt'

createfile(filename1, '10*2**2+15*2+13')
createfile(filename2, '3*5**2+7*5+20')

with open(filename1, 'r') as file:
    polynomial1 = file.read()

with open(filename2, 'r') as file:
    polynomial2 = file.read()

with open('hw45file_result.txt', 'w') as file:
     file.write(polynomial1 + '+' + polynomial2)
