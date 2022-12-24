# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100 -range) многочлена
# и записать в файл многочлен степени k.
# Пример:
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0


from random import randrange, choice


def Polynom(k, file_path):
    if k > 0:
        with open(file_path, 'a+', encoding='utf-8') as my_file:
            signs = ['+', '-']
            polynom = ''
            for i in range(k, -1, -1):
                koef = randrange(11)
                if i > 1 and koef != 0:
                    polynom += f'{koef}*x^{i} {choice(signs)} '
                elif i > 1 and koef == 0:
                    polynom += ''
                elif i == 1:
                    polynom += f'{koef}*x {choice(signs)} '
                elif i == 0 and koef != 0:
                    polynom += f'{koef} = 0'
                elif i == 0 and koef == 0:
                    polynom += ' = 0'
            my_file.write(polynom + '\n')
        return polynom


for i in range(2):
    Polynom(int(input('Enter a natural degree for calculation ')),
            'Homeworks/Python_Homeworks/Homework_4/Poly1.txt')

for i in range(2):
    Polynom(int(input('Enter a natural degree for calculation ')),
            'Homeworks/Python_Homeworks/Homework_4/Poly2.txt')
