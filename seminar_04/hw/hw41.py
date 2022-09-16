# Вычислить число c заданной точностью d
# Пример:
# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$
import math

d: float = 0.0001
i: int = 0  # точность значения
while d * 10**i != 1:
    i += 1

pi: float = math.pi
print(pi)
result: float = int(pi * 10 ** i)/ float(10 ** i)
print(result)
