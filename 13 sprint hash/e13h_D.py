"""Задача D спринта 13 hash.

Кружки.
В компании, где работает Тимофей, заботятся о досуге сотрудников
и устраивают различные кружки по интересам.
Когда кто-то записывается на занятие, в лог вносится название кружка.

По записям в логе составьте список всех кружков,
в которые ходит хотя бы один человек.
"""
import sys


def input_data():
    _ = input()
    arr = [line.strip() for line in sys.stdin]
    return arr


def hash(s: str, a: int, m: int):
    result = 0
    for si in s:
        result = (result * a + ord(si)) % m
    return result


def test():
    arr = ['вышивание крестиком', 'рисование мелками на парте', 'настольный керлинг', 'настольный керлинг', 'кухня африканского племени ужасмай', 'тяжелая атлетика', 'таракановедение', 'таракановедение']
    hobbies = set()
    print(arr)
    for index, item in enumerate(arr):
        if item not in hobbies:
            hobbies.add(item)
            continue
        arr[index] = None
    for item in arr:
        if item is not None:
            print(item)


def main():
    arr = input_data()
    hobbies = set()
    for index, item in enumerate(arr):
        if item not in hobbies:
            hobbies.add(item)
            continue
        arr[index] = None
    for item in arr:
        if item is not None:
            print(item)


if __name__ == '__main__':
    main()
