# Напишите программу, удаляющую из текста все слова, содержащие "абв". В тексте используется разделитель пробел.
# in
# Number of words: 10

# out
# авб абв бав абв вба бав вба абв абв абв
# авб бав вба бав вба

from random import sample


def Get_Random_Words(origin, num=int(input('Enter qty of elements: '))):
    lst = [''.join(sample(origin, k=3))for _ in range(num)]
    print(*lst)
    return ''.join(lst)


def Remove_Word(set, origin):
    new_set = [''.join(i) for i in set if i != origin]
    print(*new_set)
    return ''.join(new_set)


origin_word = 'zov'
Remove_Word(Get_Random_Words(origin_word), origin_word)


# def list_rand_words(count: int, alp: str = 'абв'):
    #     return " ".join("".join(sample(alp, 3)) for _ in range(count))


# def simple_sentence(words: str) -> str:
#     # return " ".join(words.replace("абв", "").split())
#     return " ".join(i for i in words.split() if i != "абв")