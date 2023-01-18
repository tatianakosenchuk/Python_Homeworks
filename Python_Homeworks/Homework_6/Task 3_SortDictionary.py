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
    return result


nms = input('Enter emploees names: ').split()
print(Sort_dictionary(nms))
