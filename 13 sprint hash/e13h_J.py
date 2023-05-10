"""Задача J спринта 13 hash.

Сумма четвёрок.
У Гоши есть любимое число S. Помогите ему найти все уникальные четвёрки
чисел в массиве, которые в сумме дают заданное число S.
"""


def input_data():
    """Получение исходные данные."""
    input()
    number = int(input())
    array = [int(item) for item in input().split()]
    return number, array


def get_array_sum_s(s: int, array: list) -> list:
    from itertools import combinations
    arr = set()
    for numbers in combinations(array, 4):
        if sum(numbers) == s:
            arr.add(numbers)
    return arr


def test():
    line = '1 0 -1 0 2 -2'
    array = sorted([int(item) for item in line.split()])
    s = 0
    result = sorted(get_array_sum_s(s, array))
    print(len(result))
    for item in result:
        print(' '.join(map(str, item)))


def main():
    s, array = input_data()
    result = sorted(get_array_sum_s(s, sorted(array)))
    print(len(result))
    for item in result:
        print(' '.join(map(str, item)))


if __name__ == '__main__':
    test()
