# Задача №3:
# Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.
# Пример:
# 10 -> 1 2 4 8

square = int(input('Введите число на котором нужно остановиться: '))
i = 1
while (i < square):
    print(i)
    i *= 2
