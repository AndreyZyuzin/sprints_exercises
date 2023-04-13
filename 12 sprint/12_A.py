"""Задача A спринта 12.

Транспонировать матрицу.
"""
import sys
from typing import Tuple, List


def input_data() -> Tuple[list, int, int]:
    """Получение данных.

    Данные сразу отправляем в одномерный массив.
    """
    number_n, number_m = int(input()), int(input())
    array = number_n * number_m * [0]
    for number_row in range(number_n):
        line = sys.stdin.readline().strip()
        start_row = number_row * number_m
        end_row = start_row + number_m
        array[start_row:end_row] = list(map(int, line.split()))
    return array, number_n, number_m


def print_transpose_matrix(array: list,
                           number_n: int,
                           number_m: int = None) -> None:
    """Отображение как транспарированную матрицу"""
    if len(array) == 0:
        return
    if not number_m:
        number_m = len(array) // number_n
    tmp_vector = [None] * number_m
    tmp_str = ''
    for number_row in range(number_n):
        for number_column in range(number_m):
            tmp_vector[number_column] = str(
                array[number_column * number_n + number_row])
        tmp_str += ' '.join(tmp_vector) + '\n'
    print(tmp_str)


def input_matrix() -> List[list]:
    """Получение данных."""
    number_n, _ = int(input()), input()
    matrix = [None] * number_n
    for number_row in range(number_n):
        line = sys.stdin.readline().strip()
        matrix[number_row] = list(map(int, line.split()))
    return matrix


def transpose_matrix(matrix: List[list]) -> List[list]:
    """Транспонирование матрицы."""
    number_n = len(matrix)
    number_m = len(matrix[0]) if number_n else 0
    new_matrix = [None] * number_m
    for row_i in range(number_m):
        new_matrix[row_i] = [None] * number_n
        for column_i in range(number_n):
            new_matrix[row_i][column_i] = matrix[column_i][row_i]
    return new_matrix


def print_matrix(matrix: List[list]) -> None:
    """Отображение матрицы."""
    number_n = len(matrix)
    tmp_str = ''
    for number_row in range(number_n):
        tmp_str += ' '.join(map(str, matrix[number_row])) + '\n'
    print(tmp_str)


def main():
    """Запуск программы"""
    # matrix = input_matrix()
    # matrix = transpose_matrix(matrix)
    # print_matrix(matrix)
    array, len_n, len_m = input_data()
    print_transpose_matrix(array, len_m)

if __name__ == '__main__':
    main()
