# # Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.


def Simple_Multipliers(num=int(input("Enter number "))):
    multipliers = []
    k = 2
    while num != 1:
        if num % k == 0:
            multipliers.append(k)
            num //= k
        else:
            k += 1
    print(multipliers)
    return multipliers


Simple_Multipliers()


# Вариант с формированием таблицы простых чисел:
# simple_table = []
# multipliers = []
# for i in range(2, num):
#     if i == 2 or i == 3 or i % 2 and i % 3 != 0:
#         simple_table.append(i)
# for k in simple_table:
#         if num % k == 0:
#             multipliers.append(k)
#             num //= k
#         elif num==1:
#             break
#         else:
#             continue
# print(multipliers)
