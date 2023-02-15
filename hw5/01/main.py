# Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.

a = int(input('--> '))
b = int(input('--> '))


def square(a, b, value=1):
    if b == 0:
        return value
    value *= a
    return square(a, b-1, value)


print(square(a, b))
