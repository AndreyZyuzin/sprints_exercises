"""Задача M спринта 13.

Золотая середина.
На каждом острове в архипелаге Алгосы живёт какое-то количество людей
или же остров необитаем (тогда на острове живёт 0 людей).
Пусть на i-м острове численность населения составляет ai.
Тимофей захотел найти медиану среди всех значений численности населения.
"""
from typing import List, Tuple


def input_data():
    """Получение исходные данные."""
    _ = input()
    _ = input()
    array_a = get_ints_input()
    array_b = get_ints_input()
    return array_a, array_b


def get_ints_input() -> List[int]:
    """Получение массив int из строки инпута."""
    return [int(item) for item in input().split()]


def get_median(array_a: List[int], array_b: List[int]) -> float:
    """Получение медиану общую двух упорядоченных массивов.
    Решение должно работать за O(log(k+m))

    a = [9, 10]
    b = [4, 4, 5, 7, 7, 7, 8, 9, 9, 10]
    Если len(a) == 2 и len(b) == 10, то не зависимо от элементов a,
    b может быть лишь 3, 4, 5, 6 индекс. 0, 1, 2, 7, 8, 9
    b_left = (b_n - a_n - 1) // 2       ; (10-2-1) // 2 = 3
    b_right = (b_n + a_n) // 2          ; (10+2) // 2 = 6

    0, 5 - 2 и 2      0 1 2 3 4 и 0 1 2 3 4
    0, 6 - 2 и 3    0 1 2 3 4 5 и 0 1 2 3 4 5
    1, 5 - 1 и 3    * 0 1 2 3 4 и 0 1 2 3 4 *
    1, 6 - 2 и 3    * 0 1 2 3 4 5 и 0 1 2 3 4 5 *
    2, 5 - 1 и 3    * * 0 1 2 3 4 и 0 1 2 3 4 * *
    2, 6 - 1 и 4  * * 0 1 2 3 4 5 и 0 1 2 3 4 5 * *
    """
    if len(array_a) > len(array_b):
        big = array_a
        small = array_b
    else:
        big = array_b
        small = array_a

    len_big = len(big)
    len_small = len(small)
    if len_big < len_small + 2:
        left_big, right_big = 0, len_big - 1
    else:
        left_big = (len_big - len_small - 1) // 2
        right_big = (len_big + len_small) // 2
    left_small, right_small = 0, len_small - 1

    while right_small - left_small > 1:
        half_big = (left_big + right_big) // 2
        half_small = (left_small + right_small) // 2
        value_half_big, value_half_small = big[half_big], small[half_small]
        # print('63: ', big[left_big:right_big + 1], small[left_small:right_small + 1])
        if value_half_big == value_half_small:
            return value_half_big
        if value_half_big < value_half_small:
            size_cuting = min(half_big - left_big, right_small - half_small)
            left_big += size_cuting
            right_small -= size_cuting
        else:
            size_cuting = min(right_big - half_big, half_small - left_small)
            right_big -= size_cuting
            left_small += size_cuting
    # print('74: ', big[left_big:right_big + 1], small[left_small:right_small + 1])
    arr = sorted(big[left_big:right_big + 1]
                 + small[left_small:right_small + 1])
    len_arr = len(arr)
    half = len_arr//2
    if len_arr % 2:
        return arr[half]
    return (arr[half-1] + arr[half]) / 2


def main():
    array_a, array_b = input_data()
    print(get_median(array_a, array_b))


def test():
    a = [1, 2]
    b = [3, 4]
    assert get_median(a, b) == 2.5


if __name__ == '__main__':
    main()
