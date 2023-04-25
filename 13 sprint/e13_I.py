"""Задача I спринта 13.

Любители конференций.
На IT-конференции присутствовали студенты из разных вузов со всей страны.
Для каждого студента известен ID университета, в котором он учится.

Тимофей предложил Рите выяснить, из каких k вузов на конференцию пришло
больше всего учащихся.
"""
from typing import List
from collections import Counter


def input_data():
    """Получение исходные данные."""
    _ = input()
    array = get_ints_input()
    k_response = int(input())
    return array, k_response


def get_ints_input() -> List[int]:
    """Получение массив int из строки инпута."""
    return [int(item) for item in input().split()]


def get_count_students(students: List[int]) -> Counter:
    """Получение количество студентов по вузах."""
    return Counter(students)


def output(types: Counter, numbers: int):
    """Отобразить первых id по убыванию."""
    list_types = sorted(types.items(), key=lambda item: item[1], reverse=True)
    print(' '.join([str(item[0]) for item in list_types[:numbers]]))


def main():
    students, k_response = input_data()
    count_students = get_count_students(students)
    output(count_students, k_response)


if __name__ == '__main__':
    main()
