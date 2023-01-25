import exept
from logger import logging


def sum(a, b):
    s = a+b
    logging.info(f'{a} + {b} = {s}')
    return s


def sub(a, b):
    s = a-b
    logging.info(f'{a} - {b} = {s}')
    return s


def mult(a, b):
    m = a*b
    logging.info(f'{a} * {b} = {m}')
    return m


def div1(a, b):
    d1 = a/b
    logging.info(f'{a} / {b} = {d1}')
    return d1


def div2(a, b):
    d2 = a//b
    logging.info(f'{a} // {b} = {d2}')
    return div2


def div3(a, b):
    d3 = a % b
    logging.info(f'{a} % {b} = {d3}')
    return d3


def pow(a, b):
    p = a**b
    logging.info(f'{a} ^ {b} = {p}')
    return p


def sqrt(a):
    sq = a**0.5
    logging.info(f'sqrt({a}) = {sq}')
    return sq
