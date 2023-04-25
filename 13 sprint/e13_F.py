"""Задача F спринта 13.

Периметр треугольника.
Перед сном Рита решила поиграть в игру на телефоне. Дан массив целых чисел,
в котором каждый элемент обозначает длину стороны треугольника.
Нужно определить максимально возможный периметр треугольника,
составленного из сторон с длинами из заданного массива.
Помогите Рите скорее закончить игру и пойти спать.

Напомним, что из трёх отрезков с длинами a ≤ b ≤ c можно составить треугольник,
если выполнено неравенство треугольника: c < a + b.
"""
from typing import List


def input_data():
    """Получение исходные данные."""
    _ = input()
    array = get_ints_input()
    return array


def get_ints_input() -> List[int]:
    """Получение массив int из строки инпута."""
    return [int(item) for item in input().split()]


def get_max_perimetr(edges: List[int]) -> int:
    """Получение max периметр наибольшего треугольника.

    Алгоритм:
    Сортируем в обратную сторону, находим первого подходящего и считаем.
    """
    edges.sort(reverse=True)
    for k_edges in range(len(edges) - 2):
        if edges[k_edges] < edges[k_edges + 1] + edges[k_edges + 2]:
            return sum(edges[k_edges:k_edges+3])
    return 0


def main():
    edges = input_data()
    print(str(get_max_perimetr(edges)))


if __name__ == '__main__':
    main()
