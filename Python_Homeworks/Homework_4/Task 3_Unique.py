# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

from collections import Counter


def Get_list(n=int(input('Enter qty of list elements '))):
    if n <= 0:
        print('Zero or negative values are not allowed')
    else:
        user_input = input(f'Enter {n} elements divided by space ')
        new_list = []
        result = user_input.split(maxsplit=n)
        if len(result) < n:
            print(f'Qty of entered numbers is less than {n}')
        else:
            for i in range(len(result)):
                result[i] = result[i].strip(" ,:;'-!/><\=+@#$%^&*)(_+=|~?}{][")
                if result[i].replace('-', '', 1).isdigit():
                    new_list.append(int(result[i]))
        print(new_list)
        return new_list


def Get_Unique(user_list):
    unique_list = []
    a = Counter(user_list)
    for i in user_list:
        if a[i] == 1:
            unique_list.append(i)
    print(unique_list)
    return unique_list


Get_Unique(Get_list())
