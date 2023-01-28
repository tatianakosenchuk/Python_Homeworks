import options
from logger import logging


file_path1 = '/home/tatkosen/Рабочий стол/Учёба/Python/Python_Homeworks/Python_Homeworks/Homework_8_Database/Readers.csv'
file_path2 = '/home/tatkosen/Рабочий стол/Учёба/Python/Python_Homeworks/Python_Homeworks/Homework_8_Database/Books.csv'


def Database_main_menu():
    while True:
        main_choice = input("\nБаза данных библиотеки:\n"
                            "\nВыберите раздел:\n"
                            "\n1 - Список читателей\n"
                            "2 - Список книг\n"
                            "0 - Выход\n")
        if int(main_choice) in range(1,3):
            Actions_menu(main_choice)
        elif int(main_choice) == 0:
            logging.info("Exit programm")
            exit()
        else:
            logging.warning("Incorrect main menu input")
            print(f"\nПожалуйста выберите корректный раздел.\n")


def Actions_menu(main_choice):
    global file_path1, file_path2
    logging.info(f"Start actions menu")
    while True:
        if int(main_choice) == 1:
            file_path = file_path1
        if int(main_choice) == 2:
            file_path = file_path2
        action_choice = input("\nВыберите требуемое действие:\n"
                              "1 - Просмотр всех данных\n"
                              "2 - Поиск данных\n"
                              "3 - Добавление записи\n"
                              "4 - Редактирование записи\n"
                              "5 - Удаление записи\n"
                              "6 - Выгрузка/Загрузка данных\n"
                              "0 - Возврат на предыдущий экран\n")
        if int(action_choice) == 1:
            options.Show_data(file_path)
            Return_menu()
        elif int(action_choice) == 2:
            options.Search_record(file_path)
            Return_menu()
        elif int(action_choice) == 3:
            options.Add_record(file_path)
            Return_menu()
        elif int(action_choice) == 4:
            options.Change_record(file_path)
            Return_menu()
        elif int(action_choice) == 5:
            options.Delete_record(file_path)
            Return_menu()
        elif int(action_choice) == 6:
            Menu_load_upload(file_path)
            Return_menu()
        elif int(action_choice) == 0:
            logging.info('Exit actions menu')
            Database_main_menu()
        else:
            logging.warning("Incorrect actions menu input")
            print(f"\nПожалуйста выберите корректное действие.")


def Menu_load_upload(file_path):
    while True:
        logging.info(f"Start menu Выгрузка/Загрузка данных")
        up_load_choice = input(f"\nВыберите требуемое действие:\n"
                               f"1 - Выгрузка данных\n"
                               f"2 - Загрузка данных\n"
                               "0 - Возврат на предыдущий экран\n")
        if int(up_load_choice) == 1:
            options.Load_data(file_path)
            Return_menu()
        elif int(up_load_choice) == 2:
            options.Upload_data(file_path)
            Return_menu()
        elif int(up_load_choice) == 0:
            logging.info('Exit menu load/upload')
            Actions_menu()
        else:
            logging.warning("Incorrect actions menu input")
            print(f"\nПожалуйста выберите корректное действие.")

def Return_menu():
    rep_or_fin=input("\nВы желаете продолжить работу?\n"
                     "1 - Да\n"
                     "2 - Нет (выход из программы)\n")
    if int(rep_or_fin)==1:
        Database_main_menu()
    else:
        exit()