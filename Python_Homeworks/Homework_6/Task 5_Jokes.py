# 5. Реализовать функцию, возвращающую n шуток, сформированных из трех случайных слов, взятых из трёх списков(по одному из каждого)
# in
# 10 True
# out
# ['дом ночью мягкий', 'огонь завтра зеленый', 'лес вчера яркий',
#     'автомобиль сегодня веселый', 'город позавчера утопичный']
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
