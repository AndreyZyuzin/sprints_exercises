"""Задача P спринта 13.

Частичная сортировка.
После того, как Гоша узнал про сортировку слиянием и быструю сортировку,
он решил придумать свой метод сортировки,
который предполагал бы разделение данных на части.
Назвал он свою сортировку Частичной.
Этим методом можно отсортировать n уникальных чисел a1, a2, … , an,
находящихся в диапазоне от 0 до n - 1.
"""
from typing import List, Tuple


def input_data() -> List[int]:
    """Получение исходные данные."""
    input()
    array = [int(number) for number in input().split()]
    return array


def n_blocks(array: List[int]):
    """Сортировка по методу"""
    k_blocks = 0
    max_item = 0
    for k_item, item in enumerate(array):
        if item > max_item:
            max_item = item
        if k_item >= max_item:
            k_blocks += 1
    return k_blocks


def main():
    array = input_data()
    print(n_blocks(array))


def test():
    assert n_blocks([0, 1, 3, 2]) == 3
    assert n_blocks([3, 6, 7, 4, 1, 5, 0, 2]) == 1
    assert n_blocks([1, 0, 2, 3, 4]) == 4


if __name__ == '__main__':
    main()
