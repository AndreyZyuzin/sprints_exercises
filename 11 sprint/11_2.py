"""
Задача B. Ловкость рук. id решение - 84926817.

Описание алгоритма.
Все клавиши равноправные и не важны их местоположение.
Поэтому помещаем их в один массив. (O(N))
Считаем количество всех типа клавиш.
Используем класс Counter из стандартной библиотеке. (O(N))
Находим при каких типах клавиш возможно их нажать. (O(K))
"""
import sys
from collections import Counter


def input_data() -> tuple[int, Counter]:
    """Получение данных."""
    number = int(input())
    counter = Counter()
    for _ in range(4):
        counter.update(sys.stdin.readline().strip())
    return number, counter


def output_data(data: int) -> None:
    """Вывод результирующих данных."""
    print(str(data))


def count_elements_in_dictinary(elements: dict,
                                chars: str,
                                limit: int) -> int:
    """Подсчет элементов в словаре, которые ограничены пределом."""
    print(type(chars))
    result = 0
    for char in chars:
        if 0 < elements.get(char, 0) <= limit:
            result += 1
    return result


def main():
    """Запуск программы."""
    number_of_fingers_one_man, counter_keys = input_data()

    score = count_elements_in_dictinary(
        counter_keys,
        '123456789',
        2 * number_of_fingers_one_man)

    output_data(score)


if __name__ == '__main__':
    main()
