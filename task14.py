# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2**k), не превосходящие числа N.
#
# Ввод:
# 6
# Вывод
# 1 2 4
# Ввод
# 24
# Вывод
# 1 2 4 8 16

n = input('Введите число: ')
n = int(n)
res = 1
pow = 1
while res <= n:
    print(res, end = ' ')
    res = 2**pow
    pow += 1