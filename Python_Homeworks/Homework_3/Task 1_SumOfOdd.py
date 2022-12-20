# Задайте список, состоящий из произвольных чисел, количество задаёт пользователь.
# Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётных позициях(не индексах).
# in
# 5
# out
# [10, 2, 3, 8, 9]
# 22

# in
# 4
# out
# [4, 2, 4, 9]
# 8

from random import sample


def Rand_list(len_list):
    num_list = sample(range(1, len_list*2), k=len_list)
    return num_list


def SumOddPositions(array):
    sum = 0
    for i in range(0, len(array), 2):
        sum += array[i]
    return sum


new_list = Rand_list(int(input('Enter list length ')))
print(new_list)
print(SumOddPositions(new_list))
