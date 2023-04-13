import sys

number = int(input())


def is_degree_of_four(number: int) -> bool:
    """Определяет является ли число степенью четверки.

    В двоичной 4**n: 0b 1 00 00 ... 00
    Должны все быть нулями, и количество нулей должны быть четными
    """
    number2 = bin(number)[3:]
    if len(number2) % 2:
        return False
    for symbol in number2:
        if symbol != '0':
            return False
    return True


print(str(is_degree_of_four(number)))
