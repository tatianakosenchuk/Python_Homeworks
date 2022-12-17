# Задайте список из n чисел последовательности (1+1/n)**n и выведите на экран их сумму.


n = int(input('Количество элементов списка '))
list_n = []
sum = 0
for i in range(1, n+1):
    element = round((1+1/i)**i, 3)
    list_n.append(element)
    sum += element
print(list_n)
print(sum)
