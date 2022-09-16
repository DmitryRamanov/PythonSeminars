# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100)
# многочлена и записать в файл многочлен степени k.
# Пример:
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
import random

k: int = 5  # степень многочлена
print('Степень многочлена =', k)
coefficient_a, coefficient_b, coefficient_c = random.randint(0, 100), random.randint(0, 100), random.randint(0, 100)
print('Коэффициенты:', coefficient_a, coefficient_b, coefficient_c)
file = open('hw44file.txt', 'w')
polynomial = f'{coefficient_a}*x**{k} + {coefficient_b}*x + {coefficient_c} = 0'
print('Многочлен:', polynomial)
file.write(polynomial)
file.close()




