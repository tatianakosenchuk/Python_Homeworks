# Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента. Use comprehension.
# in
# 9
# out
# [15, 16, 2, 3, 1, 7, 5, 4, 10]
# [16, 3, 7, 10]

from random import sample


def Get_random_list(elqty=int(input('Enter quantity of elements: '))):
    lst = sample(range(1, elqty*3), k=elqty)
    return lst


def Greater_values_list(ls):
    newls = [ls[i+1] for i in range(len(ls)-1) if ls[i+1] > ls[i]]
    return newls


l = Get_random_list()
print(l)
print(Greater_values_list(l))
