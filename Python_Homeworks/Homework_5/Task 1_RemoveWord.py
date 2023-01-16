# Напишите программу, удаляющую из текста все слова, содержащие "абв". В тексте используется разделитель пробел.
# in
# Number of words: 10

# out
# авб абв бав абв вба бав вба абв абв абв
# авб бав вба бав вба

from random import sample


def Get_Random_Words(origin, num=int(input('Enter qty of elements: '))):
    lst = [''.join(sample(origin, k=3))for i in range(num)]
    print(*lst)
    return lst


def Remove_Word(set, origin):
    new_set = [''.join(i) for i in set if i != origin]
    print(*new_set)
    return new_set


origin_word = 'zov'
Remove_Word(Get_Random_Words(origin_word), origin_word)
