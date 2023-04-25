"""Задача D спринта 13.

Печеньки.
К Васе в гости пришли одноклассники. Его мама решила угостить ребят печеньем.

Но не всё так просто. Печенья могут быть разного размера. А у каждого ребёнка
есть фактор жадности —– минимальный размер печенья, которое он возьмёт.
Нужно выяснить, сколько ребят останутся довольными в лучшем случае,
когда они действуют оптимально.

Каждый ребёнок может взять не больше одного печенья.
"""
from typing import List


def input_data():
    """Получение исходные данные."""
    _ = input()
    greed_factors = get_ints_input()
    _ = input()
    size_cookies = get_ints_input()
    return greed_factors, size_cookies


def get_ints_input() -> List[int]:
    """Получение массив int из строки инпута."""
    return [int(item) for item in input().split()]


def number_of_satisfied(greed_factors: List[int],
                        size_cookies: List[int]) -> int:
    """Получение количество довольных.

    cookies: 1 1 1 3 5
    greed:   1     2 2 4
    unheppy:           *
    Алгоритм:
    Сортируем оба массива. Идем с маленького, ищем подходящее печенье.
    Когда массив печений исчерпан, считаем сколько осталось.
    """
    greed_factors.sort()
    size_cookies.sort()
    k_child = 0
    k_cookies = -1
    while k_child < len(greed_factors):
        while k_cookies + 1 < len(size_cookies):
            k_cookies += 1
            if greed_factors[k_child] <= size_cookies[k_cookies]:
                break
        else:
            return k_child
        k_child += 1
    return len(greed_factors)


def main():
    greed_factors, size_cookies = input_data()
    print(str(number_of_satisfied(greed_factors, size_cookies)))


if __name__ == '__main__':
    main()
