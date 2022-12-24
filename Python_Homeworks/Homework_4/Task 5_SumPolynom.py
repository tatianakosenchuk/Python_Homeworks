# Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов (в строку)

def Sum_Polynom(file1, file2):
    merged = ''
    with open('Homeworks/Python_Homeworks/Homework_4/PolyMerged.txt', 'a', encoding='utf-8') as new_file:
        with open(file1,encoding="utf-8") as first_file:
            with open(file2,encoding="utf-8") as second_file:
                if len(first_file.readlines()) == len(second_file.readlines()):
                    first_file.seek(0)
                    second_file.seek(0)
                    for line in first_file:
                        merged += line.replace('= 0\n', '')
                        for line in second_file:
                            merged += f'+ {line}'
                            break
                    new_file.write(merged)
                    return merged
                else:
                    new_file.write("Content of the files doesn't match")


Sum_Polynom('Homeworks/Python_Homeworks/Homework_4/Poly1.txt',
            'Homeworks/Python_Homeworks/Homework_4/Poly2.txt')
