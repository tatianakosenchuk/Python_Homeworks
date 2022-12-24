# Вычислить число c заданной точностью d
# Пример:
# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$


from decimal import Decimal, ROUND_CEILING


def Round_number(num=Decimal(input("Enter number ")), d=Decimal(input("Enter required accuracy '0.0001' "))):
    if num >= 0:
        round_num = num.quantize(d, ROUND_CEILING)
        print(round_num)
        return round_num
    else:
        print('Negative numbers are not allowed')


Round_number()
