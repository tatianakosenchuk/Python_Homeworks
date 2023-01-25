from logger import logging


def Check_enter(a):
    try:
        ch_a = int(a)
    except ValueError:
        try:
            ch_a = float(a)
        except ValueError:
            logging.warning(f'Incorrect data {a}')
            print(f"Incorrect input {a}! Enter a number!")
            exit()
        else:
            return ch_a
    else:
        return ch_a


def Check_complex(a):
    try:
        ch_a = int(a)
    except ValueError:
        logging.warning(f'Incorrect data {a}')
        print(f"Incorrect input {a}! Enter a number!")
        exit()
    else:
        return ch_a


def Zero_division_check(b):
    if b == 0:
        logging.warning('Incorrect data 0 for division')
        print(f"Incorrect input 0 for division!")
        exit()
    else:
        return b
