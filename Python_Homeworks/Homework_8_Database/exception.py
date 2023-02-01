
import options
from logger import logging
import csv
import exception
from os import path
from logger import logging
from tabulate import tabulate

def ID_check(ID,data):
    for row in data:
        if row[0] == ID:
            return row
        else:
            logging.warning("Incorrect ID for deletition")
            print(f"\nID {ID} нет в базе данных.\n")