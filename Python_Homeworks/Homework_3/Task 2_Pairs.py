# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# in
# 4
# out
# [2, 5, 8, 10]
# [20, 40]

# in
# 5
# out
# [2, 2, 4, 8, 8]
# [16, 16, 4]

from random import sample


def Rand_list(len_list):
    num_list = sample(range(1, len_list*2), k=len_list)
    return num_list


def Mltpl_pairs(num_list):
    mult_list = []
    length = len(num_list)
    for i in range(length//2):
        mltpl = num_list[i]*num_list[length-1]
        length -= 1
        mult_list.append(mltpl)
    if len(num_list) % 2 != 0:
        mult_list.append(num_list[len(num_list)//2])

    return mult_list


array = Rand_list(int(input('Enter array length ')))
print(array)
print(Mltpl_pairs(array))
