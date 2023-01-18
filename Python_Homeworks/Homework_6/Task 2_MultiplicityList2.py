# Для чисел в пределах от 20 до N найти числа, кратные 20 или 21. Use comprehension.
# in
# 100
# out
# [20, 21, 40, 42, 60, 63, 80, 84, 100]

def Multiplicity(num=int(input("Enter N: "))):
    ls = [i for i in range(20, num+1)]
    newls = [ls[i]
             for i in range(len(ls)) if not ls[i] % 20 or not ls[i] % 21]
    return newls


print(Multiplicity())
