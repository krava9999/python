# Задача 18: Требуется найти в массиве A[1..N] самый близкий по
# величине элемент к заданному числу X. Пользователь в первой строке
# вводит натуральное число N – количество элементов в массиве. В
# последующих строках записаны N целых чисел Ai
# Последняя строка содержит число X

n = int(input("Сколько элементов массива должно быть?: "))
nums = [9, 8, 7]
# for i in range(1, n+1):
#     nums.append(i)
# print(nums)
x = int(input('Какое число ищем?: '))
if nums[0] >= x:
    print(f'Ближайшее соседнее число для {x} это {nums[0]}')
elif nums[len(nums)-1] <= x:
    print(f'Ближайшее соседнее число для {x} это {nums[len(nums)-1]}')
else:
    for i in nums:
        if i == x-1 or i == x-1:
            print(f'Ближайшее соседнее число {i}')
