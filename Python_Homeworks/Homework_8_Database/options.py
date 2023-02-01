import csv
import exception
from os import path
from logger import logging
from tabulate import tabulate


def Show_data(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        print(tabulate([a for a in [row.replace('\n', '').split(',')
                                    for row in f.readlines()]]))


def Search_record(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        search_ID = input(f'\nВведите ID для поиска:\n')
        data = list(csv.reader(f))
        f.seek(0)
        if exception.ID_check(search_ID, data):
            print(tabulate([a for a in [row for row in data if row[0] ==
                  search_ID]], headers=f.readline().replace('\n', '').split(',')))

        else:
            logging.warning("Incorrect ID for search")
            print(f"\nID {search_ID} нет в базе данных.\n")


def Add_record(file_path):
    with open(file_path, 'r+', encoding='utf-8') as f:
        data = list(csv.reader(f))
        new_ID = str(int(data[-1][0]) + 1)
        f.seek(0)
        header = f.readline().replace('\n', '').split(',')
        new_row = [input(f"Enter {header[i]} value: ")
                   for i in range(1, len(header))]
        new_row.insert(0, new_ID)
        csv.writer(f, delimiter=",").writerow(new_row)


def Change_record(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        change_ID = input(f'\nВведите ID для редактирования:\n')
        data = list(csv.reader(f))
        f.seek(0)
        header = f.readline().replace('\n', '').split(',')
        while True:
            if exception.ID_check(change_ID, data):
                print(tabulate([a for a in [exception.ID_check(change_ID, data)]], headers=header))
                print(
                    *(f"\n{list(enumerate(header))[i]}" for i in range(1, len(header))))
                field_change = input(
                    f"\nВведите номер поля для внесения изменений:\n")
                index_change = int(field_change)
                if index_change in range(1, len(header)):
                    data[data.index(exception.ID_check(change_ID, data))][index_change] = input(
                        f"\nВведите новое значение поля {data[0][index_change]}\n")
                    open(file_path, 'w').close()
                    with open(file_path, 'w', encoding='utf-8')as new_f:
                        for row in data:
                            csv.writer(new_f).writerow(row)
                    break
                else:
                    logging.warning("Incorrect ID for change")
                    print("\nПожалуйста выберите корректный номер поля.\n")
            else:
                logging.warning("Incorrect field for change")
                print(f"\nID {change_ID} нет в базе данных.\n")


def Delete_record(file_path):
    with open(file_path, 'r+', encoding='utf-8') as f:
        delete_ID = input(f'\nВведите ID для удаления:\n')
        data = list(csv.reader(f))
        if exception.ID_check(delete_ID, data):
            for row in data:
                if row[0] == delete_ID:
                    confirm = input(f"\nВы действительно желаете удалить запись?\n"
                                    f"{row}\n"
                                    "1 - Да\n"
                                    "0 - Нет\n")
                    if int(confirm) == 1:
                        open(file_path, 'w').close()
                        with open(file_path, 'w', encoding='utf-8')as new_f:
                            for row in data:
                                if row[0] != delete_ID:
                                    csv.writer(new_f).writerow(row)
                    else:
                        break
        else:
            logging.warning("Incorrect ID for deletition")
            print(f"\nID {delete_ID} нет в базе данных.\n")


def Load_data(file_path):
    f_format = 0
    while True:
        load_format = input(f'\nВыберите формат выгружаемого файла:\n'
                            '1 - csv\n'
                            '2 - txt\n')
        try:
            l_f = int(load_format) in range(1, 3)
        except:
            logging.warning("Incorrect loading format")
            print("\nПожалуйста выберите корректный формат файла.\n")
        else:
            load_path = input('\nВведите путь для сохранения файла:\n')
            if path.exists(load_path):
                file_name = input('\nВведите имя файла:\n')
                if int(load_format) == 1:
                    f_format = '.csv'
                elif int(load_format) == 2:
                    f_format = '.txt'
                with open(file_path, 'r+', encoding='utf-8') as f:
                    with open(str(file_name) + str(f_format), 'w+', encoding='utf-8') as new_f:
                        for row in csv.reader(f):
                            csv.writer(new_f).writerow(row)
                        exit()
            else:
                logging.warning("Incorrect file path for loading")
                print("\nПожалуйста введите корректный путь для сохранения файла.\n")


def Upload_data(file_path):
    while True:
        upload_path = input('\nВведите путь для загружаемого файла:\n')
        if path.exists(upload_path):
            with open(upload_path, 'r', encoding='utf-8') as up_file:
                open(file_path, 'w').close()
                with open(file_path, 'w', encoding='utf-8')as f:
                    for row in csv.reader(up_file):
                        csv.writer(f).writerow(row)
            exit()
        else:
            logging.warning("Incorrect file path for upload")
            print("\nПожалуйста введите корректный путь для загружаемого файла.\n")
