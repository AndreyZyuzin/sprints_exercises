"""Задача B спринта 13.

Комбинации.
На клавиатуре старых мобильных телефонов каждой цифре соответствовало
несколько букв. Примерно так:

2:'abc',
3:'def',
4:'ghi',
5:'jkl',
6:'mno',
7:'pqrs',
8:'tuv',
9:'wxyz'

Вам известно в каком порядке были нажаты кнопки телефона, без учета повторов.
Напечатайте все комбинации букв, которые можно набрать
такой последовательностью нажатий.
"""
from typing import List

accord_digit_letter = {
    '2': 'abc',
    '3': 'def',
    '4': 'ghi',
    '5': 'jkl',
    '6': 'mno',
    '7': 'pqrs',
    '8': 'tuv',
    '9': 'wxyz'
}

def input_data() -> str:
    """Получение исходные данные."""
    return input()


def get_combinations(digits: str, prefix: str = ''):
    """Получение буквенные комбинации."""
    if not digits:
        print(prefix, end=' ')
        return
    for letter in accord_digit_letter[digits[0]]:
        get_combinations(digits[1:], prefix + letter)


def main():
    digits = input_data()
    get_combinations(digits)


if __name__ == '__main__':
    main()
