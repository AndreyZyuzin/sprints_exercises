"""Финальная задача A спринта 13. (5kyu). id решения - 86312891.

Поиск в сломанном массиве.
Есть упорядочный массив, но минимальный элемент сдвинут на несколько элементов.
Требуется найти искомый элемент со сложностью O(log n).
"""
from typing import Tuple


def input_data() -> Tuple[int, list]:
    """Получение исходные данные."""
    input()
    target = int(input())
    array = [int(item) for item in input().split()]
    return target, array


def broken_search(nums: list, target: int) -> int:
    """Поиск элемента в упорядоченном массиве со сдвижкой.
    В массиве только уникальные элементы.

    target < arr[0] - то ищем в конце, иначе - в начале.
    ищем 5
    [* * 10 * * 6] - 10 > 6, значит 10 - это конец массива. ищем справо.
    [* *  2 * * 6] - 2 < 6, значит 2 - это начало массива. ищем справо.
    [* *  6 * * 10] - 6 < 10, значит 6 - это начало массива. ищем слева.
    [* *  12 * * 3] - 12 > 3, значит 12 - это конец массива. ищем слева.
    last < target < current - ищем слева
    target < current < last - слева
    current < last < target - слева
    last < current < target - справа
    target < last < current - справа
    current < target < last - справа
    """
    length = len(nums)
    last = nums[length - 1]
    if last == target:
        return length - 1
    left = 0
    right = length - 2
    while right > left:
        current_index = (right + left) // 2
        current = nums[current_index]
        if current == target:
            return current_index
        if (current < target < last
            or target < last < current
            or last < current < target):
            left = current_index + 1
        else:
            right = current_index - 1
    return left if nums[left] == target else -1


def main():
    target, arr = input_data()
    print(broken_search(arr, target))


if __name__ == '__main__':
    main()
