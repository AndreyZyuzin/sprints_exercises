"""Задача B спринта 13.

Пузырёк.
Сортировка пузырьком.
"""
from typing import List

def input_data() -> str:
    """Получение исходные данные."""
    input()
    return input()


def line_to_array(line: str) -> List[int]:
    """Преобразовние сторки в список чисел."""
    return [int(item) for item in line.split()]


def sorting(numbers: List[int]):
    """Сортикровка пузырьком, отображая шаги."""
    is_done = False
    for k_determinate in range(len(numbers) - 1, 0, -1):
        index = 0
        while index < k_determinate:
            if numbers[index] > numbers[index + 1]:
                is_done = False
                numbers[index], numbers[index + 1] = (numbers[index + 1],
                                                      numbers[index])
            index += 1
        if is_done:
            return
        is_done = True
        print(' '.join(map(str, numbers)))


def main():
    line = input_data()
    numbers = line_to_array(line)
    sorting(numbers)


if __name__ == '__main__':
    main()
