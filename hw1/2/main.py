# Задача 2: Петя, Катя и Сережа делают из бумаги журавликов.
# Вместе они сделали S журавликов.
# Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали одинаковое количество журавликов, а Катя сделала в два раза больше журавликов,
#  чем Петя и Сережа вместе?
# 6 -> 1  4  1
# 24 -> 4  16  4
# 60 -> 10  40  10

origamiCount = int(input('Введите количество журавликов: '))
girl = 0
boy1 = 0
boy2 = 0
if origamiCount <= 0:
    print('Оригами пока не сделаны или введено некорректное число')
else:
    girl = origamiCount / 3 * 2
    boy1 = origamiCount/3/2
    boy2 = boy1
    print(f'Петр: {boy1} Катюха: {girl} Серега: {boy2}')