# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике.
# Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для этого Петя делает две подсказки.
# Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.

# 4 4 -> 2 2
# 5 6 -> 2 3

from math import sqrt


s = int(input("S: "))
p = int(input("P: "))

sq = sqrt(p)
found = False
for x in range(1, 1 + int(sq)):
    if p % x == 0:
        y = int(p / x)
        if s == x + y:
            found = True
            break
if found:
    print(x, y)
else:
    print("не нашли таких чисел")
