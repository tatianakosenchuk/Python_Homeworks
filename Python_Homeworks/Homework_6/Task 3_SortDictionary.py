# Написать функцию, аргументы имена сотрудников, возвращает словарь, ключи — первые буквы имён, значения — списки, содержащие имена, начинающиеся с соответствующей буквы.
# in
# "Иван", "Мария", "Петр", "Илья", "Марина", "Петр", "Алина", "Бибочка"
# out
# {'А': ['Алина'], 'Б': ['Бибочка'], 'И': ['Иван', 'Илья'],
#     'М': ['Марина', 'Мария'], 'П': ['Петр', 'Петр']}


def Sort_dictionary(lst):
    result = {}
    for i in sorted(lst):
        result.setdefault(i[0], []).append(i)
        # if i[0] not in result:
        #     result[i[0]] = [i]
        # else:
        #     result[i[0]].append(i)
        #     result[i[0]] +=[i] - lj,добавляет в конец списка
    return result


# def thesaurus(*args):
#     if "" not in args:
#         return {ch: list(names) for ch, names in groupby(sorted(args), key=lambda i: i[0]) if ch}
#     return "Error"

# def thesaurus(*args):
#     if "" not in args:
#         return {ch[0]: list(filter(lambda el: el.startswith(ch[0]), args)) for ch in sorted(args)}
#     return "Error"
# nms = input('Enter emploees names: ').split()
print(Sort_dictionary(nms))
