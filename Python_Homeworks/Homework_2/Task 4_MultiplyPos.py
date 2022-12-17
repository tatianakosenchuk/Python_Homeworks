# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях.
# Позиции хранятся в файле file.txt в одной строке одно число.

n = int(input('Количество элементов списка '))
pos1 = int(input('pos1 '))
pos2 = int(input('pos2 '))
array = list(range(-n, n+1))
print(array)
if pos1 and pos2 in range(len(array)+1):
    print(array[pos1-1]*array[pos2-1])
else:
    print('Нет значения с таким индексом')
