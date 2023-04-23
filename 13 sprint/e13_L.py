"""Задача L спринта 13.

Два велосипеда.
Вася решил накопить денег на два одинаковых велосипеда — себе и сестре.
У Васи есть копилка, в которую каждый день он может добавлять деньги
(если, конечно, у него есть такая финансовая возможность).
В процессе накопления Вася не вынимает деньги из копилки.

У вас есть информация о росте Васиных накоплений — сколько у Васи
в копилке было денег в каждый из дней.

Ваша задача — по заданной стоимости велосипеда определить:
- первый день, в которой Вася смог бы купить один велосипед,
- и первый день, в который Вася смог бы купить два велосипеда.
Подсказка: решение должно работать за O(log n).
"""
from typing import Tuple

def input_data() -> Tuple[str, int]:
    """Получение исходные данные."""
    input()
    line = input()
    value = int(input())
    return line, value


def line_to_list(line: str) -> Tuple[int]:
    return tuple(map(int, line.split()))


def search_first_value_and_more(array: tuple, value: int) -> int:
    """Поиск в отсортированном массиве элемент, который не больше value."""
    first = 0
    last = len(array) - 1
    while last - first > 1:
        half = (first + last) // 2
        if array[half] >= value:
            last = half
        else:
            first = half
    if array[first] >= value:
        return first + 1
    return last + 1 if array[last] >= value else -1


def search_index(array: tuple, value: int, left: int, right: int) -> int:
    if right - left > 1:
        index = (right + left) // 2
        if array[index] >= value:
            return search_index(array, value, left, index)
        return search_index(array, value, index, right)
    if array[left] >= value:
        return left + 1
    return right + 1 if array[right] >= value else -1


def search_first_value_and_more_2(array: tuple, value: int) -> int:
    """Поиск в отсортированном массиве элемент, который не больше value."""
    return search_index(array, value, 0, len(array) - 1)


def main():
    shedule_str, cost = input_data()
    shedule = line_to_list(shedule_str)
    print(str(search_first_value_and_more(shedule, cost)),
          str(search_first_value_and_more(shedule, cost * 2)))


if __name__ == '__main__':
    main()
