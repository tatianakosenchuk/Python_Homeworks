# 5. Реализовать функцию, возвращающую n шуток, сформированных из трех случайных слов, взятых из трёх списков(по одному из каждого)
# in
# 10 True
# out
# ['дом ночью мягкий', 'огонь завтра зеленый', 'лес вчера яркий',
#     'автомобиль сегодня веселый', 'город позавчера утопичный']
from random import choice, randrange
from random import choice

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра",
           "позавчера", "ночью", "когда-то", "где-то"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]


def Jokes(num, check=False):
    print(check)
    if check == True and (num > len(nouns) or num > len(adverbs) or num > len(adjectives)):
        print(f'Impossible to create {num} unique jokes')
    else:
        jlist = []
        cp_nouns, cp_adverbs, cp_adjectives = nouns, adverbs, adjectives
        for i in range(num):
            a, b, v = choice(cp_nouns), choice(
                cp_adverbs), choice(cp_adjectives)
            if check == True:
                jlist.append(f'{a} {b} {v}')
                cp_nouns.remove(a), cp_adverbs.remove(
                    b), cp_adjectives.remove(v)
            else:
                jlist.append(f'{a} {b} {v}')
        return jlist


print(Jokes(num=int(input('Enter quantity of jokes required: ')), check=True))


# def some_jokes(n: int, repeat: bool = False) -> list:
#     """
#     Функция возвращает случайные шутки, собранные из трех списков слов

#     :param n: количество шуток
#     :param repeat: уникальные/неуникальные
#     :return: список случайных шуток

#     """
#     no, adv, adj = nouns.copy(), adverbs.copy(), adjectives.copy()
#     list_of_j = []
#     list_min = min(no, adv, adj)

#     for i in range(len(list_min) % n if repeat else n):
#         num = randrange(len(list_min))
#         list_of_j.append(f"{no.pop(num)} {adv.pop(num)} {adj.pop(num)}" if repeat
#                          else f"{choice(nouns)} {choice(adverbs)} {choice(adjectives)}")
#     return list_of_j


# print(some_jokes(100, True))
# print(help(some_jokes))
# print(some_jokes.__doc__)
