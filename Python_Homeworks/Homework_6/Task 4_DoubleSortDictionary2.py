# Функция принимает в качестве аргументов строки в формате «Имя Фамилия», возвращает словарь, ключи — первые буквы фамилий, значения — словари, реализованные по схеме предыдущего задания.
# in
# "Иван Сергеев", "Инна Серова", "Петр Алексеев",
# "Илья Иванов", "Анна Савельева", "Юнона Ветрякова",
# "Борис Аркадьев", "Антон Серов", "Павел Анисимов"
# out
# {'С': {'А': ['Анна Савельева', 'Антон Серов'], 'И': ['Иван Сергеев', 'Инна Серова']}, 'А': {'Б': ['Борис Аркадьев'], 'П': [
#     'Павел Анисимов', 'Петр Алексеев']}, 'И': {'И': ['Илья Иванов']}, 'В': {'Ю': ['Юнона Ветрякова']}}


def Double_sort_dictionary(lst):
    nnames = [lst[i-1]+' '+lst[i] for i in range(1, len(lst), 2)]
    print(nnames)
    sdict = {}
    for i in sorted(nnames):
        sdict.setdefault(i.split()[1][0], {}).setdefault(
            i.split()[0][0], []).append(i)
    return sdict


names = input('Enter emploees names and surnames: ').split()
print(Double_sort_dictionary(names))


# def thesaurus_adv(*args):
#     s_n_sort = {}
#     for s_n in args:
#         s_n_sort.setdefault(s_n.split()[1][0], {}).setdefault(
#             s_n.split()[0][0], []).append(s_n)
#     return dict(OrderedDict(sorted(s_n_sort.items(), key=lambda x: x[0])))
