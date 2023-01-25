from logger import logging
import exept
import mode_calc as calc


def Calc_interface():
    while True:
        logging.info("Calculator started")
        num_type = main_menu()
        if int(num_type) not in range(3):
            logging.warning(
                f"Operation menu: wrong item {num_type} selected")
            print("Error! Please select correct option\n")
        elif int(num_type) == 0:
            logging.info('Exit programm')
            exit()
        elif int(num_type) == 1:
            logging.info('Rational numbers mode is selected')
            op_type = menu_operation()
            logging.info('Operation menu started')
            if int(op_type) not in range(7):
                logging.warning(
                    f"Operation menu: wrong item {op_type} selected")
                print("Error! Please select correct option\n")
            elif int(op_type) == 0:
                logging.info("Return to main menu")
                main_menu()
            else:
                if int(op_type) == 6:
                    a = enter_ratio_nums(1)
                    print(calc.sqrt(a))
                    exit()
                else:
                    a, b = enter_ratio_nums(2)
                    if int(op_type) == 1:
                        logging.info('Sum is selected')
                        print(calc.sum(a, b))
                        exit()
                    elif int(op_type) == 2:
                        logging.info('Sub is selected')
                        print(calc.sub(a, b))
                        exit()
                    elif int(op_type) == 3:
                        logging.info('Mult is selected')
                        print(calc.mult(a, b))
                        exit()
                    elif int(op_type) == 5:
                        logging.info('Pow is selected')
                        print(calc.pow(a, b))
                        exit()
                    elif int(op_type) == 4:
                        exept.Zero_division_check(b)
                        div_type = menu_div_rational()
                        logging.info('Div menu is started')
                        if int(num_type) == 0:
                            logging.info('Return to operation menu')
                            menu_operation()
                        elif int(div_type) == 1:
                            logging.info("/ is selected")
                            print(calc.div1(a, b))
                            exit()
                        elif int(div_type) == 2:
                            logging.info("// is selected")
                            print(calc.div2(a, b))
                            exit()
                        elif int(div_type) == 3:
                            logging.info("% is selected")
                            print(calc.div3(a, b))
                            exit()
        elif int(num_type) == 2:
            logging.info('Complex numbers mode is selected')
            op_type = menu_operation()
            logging.info('Operation menu started')
            if int(op_type) == 0:
                logging.info("Return to main menu")
                main_menu()
            else:
                if int(op_type) == 6:
                    a = enter_complex_nums(1)
                    print(calc.sqrt(a))
                    exit()
                else:
                    a, b = enter_complex_nums(2)
                    if int(op_type) == 1:
                        logging.info('Sum is selected')
                        print(calc.sum(a, b))
                        exit()
                    elif int(op_type) == 2:
                        logging.info('Sub is selected')
                        print(calc.sub(a, b))
                        exit()
                    elif int(op_type) == 3:
                        logging.info('Mult is selected')
                        print(calc.mult(a, b))
                        exit()
                    elif int(op_type) == 5:
                        logging.info('Pow is selected')
                        print(calc.pow(a, b))
                        exit()
                    elif int(op_type) == 4:
                        exept.Zero_division_check(b)
                        logging.info("div is selected")
                        print(calc.div1(a, b))
                        exit()


def main_menu():
    num_type = input("\nCalculator programm is started!\n"
                     "Select calculation mode:\n"
                     "1 - rational numbers\n"
                     "2 - complex numbers\n"
                     "0 - exit\n")
    try:
        int(num_type)
    except ValueError:
        print("Error! Please select correct option\n")
        exit()
    else:
        return num_type


def menu_operation():
    op_type = input("Select operation:\n"
                    "1 - sum\n"
                    "2 - sub\n"
                    "3 - mult\n"
                    "4 - div\n"
                    "5 - pow\n"
                    "6 - sqrt\n"
                    "0 - previous menu\n")
    try:
        int(op_type)
    except ValueError:
        print("Error! Please select correct option\n")
        exit()
    else:
        return op_type


def menu_div_rational():
    div_type = input("Select operation:\n"
                     "1 - /\n"
                     "2 - //\n"
                     "3 - %\n"
                     "0 - previous menu\n")
    try:
        int(div_type)
    except ValueError:
        print("Error! Please select correct option\n")
        exit()
    else:
        return div_type


def enter_ratio_nums(qty):
    if qty == 1:
        a = input("Enter number:\n")
        while not exept.Check_enter(a):
            break
        return exept.Check_enter(a)
    elif qty == 2:
        a, b = input("Enter 1 number:\n"), input(
            "\nEnter 2 number:\n")
        while not exept.Check_enter(a) and not exept.Check_enter(b):
            break
        return exept.Check_enter(a), exept.Check_enter(b)


def enter_complex_nums(qty):
    if qty == 1:
        try:
            a, b = input("Enter real part of 1 number:\n"), input(
                "\nEnter imaginary part of 1 number:\n")
            comp1 = complex(exept.Check_complex(a), exept.Check_complex(
                b))
        except ValueError:
            pass
        else:
            return comp1
    elif qty == 2:
        try:
            a, b, c, d = input("Enter real part of 1 number:\n"), input("\nEnter imaginary part of 1 number:\n"), input(
                "\nEnter real part of 2 number:\n"), input("\nEnter imaginary part of 2 number:\n")
            comp1, comp2 = complex(exept.Check_complex(a), exept.Check_complex(
                b)), complex(exept.Check_complex(c), exept.Check_complex(d))
        except ValueError:
            pass
        else:
            return comp1, comp2
