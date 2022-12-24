# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# # Без использования встроенной функции преобразования, без строк.
# in
# 88
# out
# 1011000

# in
# 11
# out
# 1011

def Convert_To_Double(number):
    double_list=[]
    while number:
        double_list.insert(0,number%2)
        number//=2
    print(*double_list,sep='')
    return double_list
    

Convert_To_Double(int(input('Enter number ')))