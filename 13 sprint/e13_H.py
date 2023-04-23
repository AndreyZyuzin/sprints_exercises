"""Задача H спринта 13.

Большое число.
Вечером ребята решили поиграть в игру «Большое число».
Даны числа. Нужно определить, какое самое большое число можно из них составить.
"""
from typing import List


def input_data() -> str:
    """Получение исходные данные."""
    input()
    return input()


def line_to_array(line: str) -> List[str]:
    """Преобразовние сторки в список чисел."""
    return line.split()


def output(numbers: List[str]):
    """Отоброжение результата."""
    return ''.join(numbers)


def sort(numbers: List[str]):
    """Сортикровка пузырьком."""
    is_done = False
    for k_determinate in range(len(numbers) - 1, 0, -1):
        index = 0
        while index < k_determinate:
            if (numbers[index] + numbers[index + 1]
                < numbers[index + 1] + numbers[index]):
                is_done = False
                numbers[index], numbers[index + 1] = (numbers[index + 1],
                                                      numbers[index])
            index += 1
        if is_done:
            break
        is_done = True
    return numbers


def main():
    line = input_data()
    numbers = line_to_array(line)
    numbers = sort(numbers)
    print(output(numbers))


if __name__ == '__main__':
    main()
