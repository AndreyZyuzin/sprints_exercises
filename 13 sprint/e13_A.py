"""Задача A спринта 13.

Генератор скобок.
Рита по поручению Тимофея наводит порядок в правильных скобочных
последовательностях (ПСП), состоящих только из круглых скобок ().
Для этого ей надо сгенерировать все ПСП длины 2n в алфавитном
порядке —– алфавит состоит из ( и )
и открывающая скобка идёт раньше закрывающей.

Помогите Рите —– напишите программу, которая по заданному n выведет
все ПСП в нужном порядке.
"""
from typing import List


def input_data() -> int:
    """Получение исходные данные."""
    return int(input())


def bracket_sequences(k_left: int, k_right=None, prefix: str = ''):
    """Рекурсивная функция, которая генерирует различные комбинации скобок."""
    if k_right is None:
        k_right = k_left
    if k_right == 0:
        bracket_sequences.array.append(prefix)
        return
    if k_left > 0:
        bracket_sequences(k_left - 1, k_right, ')' + prefix)
    if k_left < k_right:
        bracket_sequences(k_left, k_right - 1, '(' + prefix)


bracket_sequences.array = []


def output_data(array: list):
    """Отображение множество в столбец по алфавитном порядке."""
    print('\n'.join(sorted(array)))


def main():
    level = input_data()
    bracket_sequences(level)
    output_data(bracket_sequences.array)


if __name__ == '__main__':
    main()
