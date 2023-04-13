"""Задача A. Ближайший ноль. id решение - 84895640, 84895702."""

import sys


def input_data() -> list:
    """Получение данных.

    Получаем бесполезное количество и требуемый список int.
    """
    _ = input()
    line = sys.stdin.readline().strip()
    return list(map(int, line.split()))


def output_data(data: list) -> None:
    """Вывод результирующих данных."""
    print(' '.join(map(str, data)))


def get_list_lengths_1(houses: list) -> list:
    """Получение списка длин до пустого дома.

    Нахождение пустых домов. O(N).
    Делим задачу на три части:
    до первого пустого дома - там обатная арифмитическая последовательность.
    между пустого дома до пустого дома - расчитыватся для каждого места
        расстояние до пустого места. и перется минимум из двух значений.
    от последнего дома - прямая арифмитическая последовательность.
    Все три части - О(N).
    """
    number_of_houses = len(houses)
    array_of_lengths = [0] * number_of_houses
    empty_houses = [house_i for house_i, house in enumerate(houses)
                    if house == 0]

    array_of_lengths[:empty_houses[0]] = range(empty_houses[0], 0, -1)

    for number_empty in range(1, len(empty_houses)):
        begin_range = empty_houses[number_empty - 1]
        end_range = empty_houses[number_empty]
        for current_place in range(begin_range, end_range):
            length = min(current_place - begin_range,
                         end_range - current_place)
            array_of_lengths[current_place] = length

    array_of_lengths[empty_houses[-1]:] = (
        range(number_of_houses - empty_houses[-1]))

    return array_of_lengths


def get_list_lengths_2(houses: list) -> list:
    """Получение списка длин до пустого дома.

    Идем по очереди начиная с первого дома и считаем количество домов и
    записываем в массив. Если нашли пустой дом, то счетчик обнуляется. O(N)
    Когда дошли до конца, то идем обратно и тоже считаем дома, но в массив
    элемент переписывается только, когда счетчик меньше старого значения. O(N)
    В начале обоих направлениях начальное значение должно быть большое.
    """
    number_of_houses = len(houses)
    array_of_lengths = [0] * number_of_houses
    counter = number_of_houses
    for number_house, house in enumerate(houses):
        counter = counter + 1 if house else 0
        array_of_lengths[number_house] = counter

    number_house = number_of_houses
    counter = number_of_houses
    while number_house:
        number_house -= 1
        counter = counter + 1 if houses[number_house] else 0
        if counter < array_of_lengths[number_house]:
            array_of_lengths[number_house] = counter
    return array_of_lengths


def main():
    """Запуск программы."""
    hauses = input_data()
    output_data(get_list_lengths_2(hauses))


if __name__ == '__main__':
    main()
