"""Задача E спринта 13.

Покупка домов.
Тимофей решил купить несколько домов на знаменитом среди разработчиков
Алгосском архипелаге. Он нашёл n объявлений о продаже,
где указана стоимость каждого дома в алгосских франках.
А у Тимофея есть k франков. Помогите ему определить,
какое наибольшее количество домов на Алгосах он сможет приобрести
за эти деньги.
"""
from typing import List


def input_data():
    """Получение исходные данные."""
    _, money = get_ints_input()
    costs = get_ints_input()
    return money, costs


def get_ints_input() -> List[int]:
    """Получение массив int из строки инпута."""
    return [int(item) for item in input().split()]


def get_max_houses(money: int, costs: List[int]) -> int:
    """Получение max количество домов за данные деньги.

    10: 2 3 4 4
    Алгоритм:
    Сортируем и считаем на сколько хватает.
    """
    costs.sort()
    result = 0
    for cost in costs:
        if cost > money:
            return result
        money -= cost
        result += 1
    return result


def main():
    money, costs = input_data()
    print(str(get_max_houses(money, costs)))


if __name__ == '__main__':
    main()
