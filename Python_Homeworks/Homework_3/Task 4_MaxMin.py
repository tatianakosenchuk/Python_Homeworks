# Задайте список из произвольных вещественных чисел, количество задаёт пользователь.
# Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# in
# 5
# out
# [5.16, 8.62, 6.57, 7.92, 9.22]
# Min: 0.16, Max: 0.92. Difference: 0.76

# in
# 3
# out
# [9.26, 8.5, 1.14]
# Min: 0.14, Max: 0.5. Difference: 0.36

from random import uniform


def Rand_list(len_list):
    num_list = []
    for i in range(len_list):
        element = round(uniform(0, 10), 2)
        num_list.append(element)
    return num_list


def Max_Mix_fractional(array):
    max = min = array[0] % 1
    for i in range(1,len(array)):
        if array[i] % 1 > max:
            max = array[i] % 1
        if array[i] % 1 < min:
            min = array[i] % 1
    return f"Max: {round(max,2)}, Min: {round(min,2)}. Difference: {round(max-min,2)}"


new_list = Rand_list(int(input('Enter length ')))
print(new_list)
print(Max_Mix_fractional(new_list))
