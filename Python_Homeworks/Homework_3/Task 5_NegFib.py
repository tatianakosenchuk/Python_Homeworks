# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Негафибоначчи

# in
# 8
# out
# -21 13 -8 5 -3 2 -1 1 0 1 1 2 3 5 8 13 21

# in
# 5
# out
# 5 -3 2 -1 1 0 1 1 2 3 5

def Fib(num):
    if num in [1, 2]:
        return 1
    else:
        return Fib(num-1) + Fib(num-2)

def Neg_Fib(num):
    num1, num2 = 1, -1
    if num == 1:                       
        return 1
    elif num == 2:                       
        return -1
    else:
       return Neg_Fib(num-2)-Neg_Fib(num-1)

num_ent=int(input('Enter number '))
list_Fib = [0]
for i in range(1, num_ent + 1):
    list_Fib.append(Fib(i))
    list_Fib.insert(0, Neg_Fib(i))
print(list_Fib)




