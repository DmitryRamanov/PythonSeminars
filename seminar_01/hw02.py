# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
# НЕ ПОНЯЛ ТРЕБОВАНИЕ, ВЗЯЛ РЕШЕНИЕ С СЕМИНАРА2

for x in range(2):
    for y in range(2):
        for z in range(2):
            print(not (x or y or z) == (not x and not y and not z))
