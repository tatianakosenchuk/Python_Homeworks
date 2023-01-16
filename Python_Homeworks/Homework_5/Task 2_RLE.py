# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.Входные и выходные данные хранятся в отдельных текстовых файлах.

# in
# Enter the name of the file with the text:
# 'text_words.txt'
# Enter the file name to record:
# 'text_code_words.txt'
# Enter the name of the file to decode:
# 'text_code_words.txt'

# out
# aaaaavvvvvvvvvvvvvvvvvvvvvvvvvvvvvssssDDDdddFFggggOOiiiaa
# vvvvvvvvvvvbbwwPPuuuTTYyWWQQ

# out in file
# 'text_words.txt'
# aaaaavvvvvvvvvvvvvvvvvvvvvvvvvvvvvssssDDDdddFFggggOOiiiaa
# vbbwwPPuuuTTYyWWQQ

# 'text_code_words.txt'
# 5a29v4s3D3d2F4g2O3i2a1
# 1v2b2w2P3u2T1Y1y2W2Q

from itertools import groupby
from os import path


def RLE_Encode(file1=input('Enter the name of the file with the text: '), file2=input('Enter the file name to record: ')):
    check1, check2 = path.exists(file1), path.exists(file2)
    if check1 and check2:
        with open(file1, 'r', encoding='utf-8') as text:
            with open(file2, 'w', encoding='utf-8') as code:
                values = [list(key) for item, key in groupby(text.read())]
                rle = (''.join(str(len(a))+a[0] for a in values))
                code.write(rle)
            return rle
    elif not check1:
        print(f'\n{file1} DOES NOT EXIST!')
    elif not check2:
        print(f'\n{file2} DOES NOT EXIST!')


def RLE_Decode(file1=input('Enter the name of the file to decode: '), file2=input('Enter the file name to record: ')):
    check1, check2 = path.exists(file1), path.exists(file2)
    if check1 and check2:
        with open(file1, 'r', encoding='utf-8') as rle:
            with open(file2, 'w', encoding='utf-8') as decode:
                dec, digits = '', ''
                for i in rle.read():
                    if i.isdigit():
                        digits += i
                    else:
                        dec += int(digits)*i
                        digits = ''
                decode.write(dec)
            return dec
    elif not check1:
        print(f'\n{file1} DOES NOT EXIST!')
    elif not check2:
        print(f'\n{file2} DOES NOT EXIST!')


# RLE_Encode()
RLE_Decode()
