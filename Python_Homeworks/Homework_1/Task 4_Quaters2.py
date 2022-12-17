#4. Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).
#*Пример:*
#- 1 -> x > 0, y > 0
#- 8 -> нет такой четверти

qtr = int(input("Введите номер четверти"))
if qtr not in range(1,5):
    print("Нет такой четверти")
elif qtr==1:
    print("Диапазон координат: x(0;+бесконечность), y(0;+бесконечность)")
elif qtr==2:
    print("Диапазон координат: x(-бесконечность;0), y(0;+бесконечность)")
elif qtr==3:
    print("Диапазон координат: x(-бесконечность;0), y(-бесконечность;0)")
else:
    print("Диапазон координат: x(0;+бесконечность), y(-бесконечность;0)")