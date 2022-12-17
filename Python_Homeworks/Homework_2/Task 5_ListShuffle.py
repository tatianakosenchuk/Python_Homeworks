# Реализуйте алгоритм перемешивания списка.

from random import randrange

n = int(input('Количество элементов списка '))
list_old = list(range(n))
list_new = []
print(list_old)
for i in range(n*10):
    index = randrange(n)
    if i == index:
        continue
    elif list_old[index] not in list_new:
        list_new.append(list_old[index])
    elif len(list_new) == n:
        break

print(list_new)
