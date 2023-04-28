"""Задача O спринта 13.

Разность треш-индексов.
Гоша долго путешествовал и измерил площадь каждого из n островов Алгосов,
но ему этого мало! Теперь он захотел оценить,
насколько разнообразными являются острова в составе архипелага.

Для этого Гоша рассмотрел все пары островов
(таких пар, напомним, n * (n-1) / 2)
и посчитал попарно разницу площадей между всеми островами.
Теперь он собирается упорядочить полученные разницы,
чтобы взять k-ую по порядку из них.

Сложные тесты:
10_000 - 200_000, 500_000, 700_000 - из макс 10000 * 9999 / 2 = 49_995_000.
    Это в первой половине. Всегда искать только минимальные.
100_000 - 10, 50, 100.
"""
from typing import List, Tuple
import math


def input_data() -> Tuple[List[int], int]:
    """Получение исходные данные."""
    input()
    array = [int(number) for number in input().split()]
    k_distance = int(input())
    return array, k_distance


def min_distance_big_memory(areas: List[int], k_distance: int = 1):
    """Поиск min разницы между островами."""
    distances = []
    for i_area, area1 in enumerate(areas[:-1]):
        for area2 in areas[i_area+1:]:
            distances.append(abs(area1-area2))
    distances.sort()
    return distances[k_distance - 1]


def min_distance4(areas: List[int], k_distance: int = 1):
    """Поиск min разницы между островами."""
    counter = {}
    for i_area, area1 in enumerate(areas[:-1]):
        for area2 in areas[i_area+1:]:
            distance = abs(area1 - area2)
            if distance in counter:
                counter[distance] += 1
            else:
                counter[distance] = 1
    counter = sorted(counter.items(), key=lambda x: x[0])
    result = 0
    for key, value in counter:
        result += value
        if result >= k_distance:
            return key


def adding_item(array: List[int], element: int) -> bool:
    """Элемент добавляется по ранжиру.
    Если последний элемент меньше, чем element, то False.
    """
    k_item = len(array) - 1
    if element > array[k_item]:
        return False
    while k_item:
        if element >= array[k_item - 1]:
            break
        array[k_item] = array[k_item - 1]
        k_item -= 1
    array[k_item] = element
    return True


def min_distance3(areas: List[int], k_distance: int = 1):
    """Поиск min разницы между островами.

    Сортируем O(log(n)). и идем O(?) -> O(n) -
                                чем дальше, что будет проверять один элемент.
        0   1   2   3   4   5   6
    0   *
    1   1   *
    2   3   2   *
    3   6   5   4   *
    4  10   9   8   7   *
    5  15  14  13  12  11   *
    6  21  20  19  18  17  16   *
    сортировка O(k_distance * n)
    если k_distance большое - горлышко.
    """
    areas.sort()
    distances = [areas[-1]] * k_distance
    for i in range(1, len(areas)):
        for j in range(i-1, -1, -1):
            if not adding_item(distances, areas[i] - areas[j]):
                break
    return distances[-1]


def min_distance6(areas: List[int], k_distance: int = 1):
    """Поиск min разницы между островами.

    Сортируем O(log(n)). и идем O(?) -> O(n) -
                                чем дальше, что будет проверять один элемент.
        0   1   2   3   4   5   6
    0   *
    1   1   *
    2   7   2   *
    3  12   8   3   *
    4  16  13   9   4   *
    5  19  17  14  10   5   *
    6  21  20  18  15  11   6   *
    сортировка O(k_distance * n)
    если k_distance большое - горлышко.
    distances нужно делать словарем. Как проверять, что уже большие величины?
    """
    areas.sort()
    distances = [areas[-1]] * k_distance
    for i in range(1, len(areas)):
        for j in range(0, len(areas)-i):
            print(i + j, j)
    return distances[-1]


def get_limit_min(counter: dict, k_number: int):
    """Определение значение первых k_number минимальных чисел."""
    myiter = iter(sorted(counter.items(), key=lambda x: x[0]))
    while True:
        key, value = next(myiter)
        if k_number <= value:
            result = key
            break
        k_number -= value
    try:
        while True:
            key, _ = next(myiter)
            del counter[key]
    except StopIteration:
        return result


def get_limit_min2(counter: dict, k_number: int):
    """Определение значение первых k_number минимальных чисел."""
    for key, value in sorted(counter.items(), key=lambda x: x[0]):
        if k_number <= value:
            return key
        k_number -= value


def min_distance(areas: List[int], k_distance: int = 1):
    """Поиск min разницы между островами.

    Сортируем O(log(n)). и идем O(?) -> O(n) -
                                чем дальше, что будет проверять один элемент.
        0   1   2   3   4   5   6
    0   *
    1   1   *
    2   3   2   *
    3   6   5   4   *
    4  10   9   8   7   *
    5  15  14  13  12  11   *
    6  21  20  19  18  17  16   *
    сортировка O(k_distance * n)
    если k_distance большое - горлышко.
    """
    LINES_NOT_CHECK = 1
    lines_from_k_distance = math.ceil((math.sqrt(8*k_distance - 1) - 1)/2) + 1
    areas.sort()
    distances = {}
    max_i = min(len(areas), max(lines_from_k_distance, LINES_NOT_CHECK))
    for i in range(1, max_i):
        for j in range(i-1, -1, -1):
            distance = areas[i] - areas[j]
            if distance in distances:
                distances[distance] += 1
            else:
                distances[distance] = 1

    for i in range(max_i, len(areas)):
        limit = get_limit_min(distances, k_distance)
        for j in range(i-1, -1, -1):
            distance = areas[i] - areas[j]
            if distance >= limit:
                break
            if distance in distances:
                distances[distance] += 1
            else:
                distances[distance] = 1
    return get_limit_min(distances, k_distance)


def main():
    areas, k_distance = input_data()
    print(min_distance(areas, k_distance))


def test():
#    areas = [1, 3, 8, 5, 5, 12, 5]
#    print(min_distance(areas, 5), min_distance_big_memory(areas, 5))
#    areas = [1, 3, 8, 5, 5, 12, 5, 4, 7,2,14, 17]
#    print(min_distance(areas, 5), min_distance_big_memory(areas, 5))
#    assert min_distance(areas, 5) == min_distance_big_memory(areas, 5)
#    areas = [1, 3, 5]
#    assert min_distance(areas, 3) == min_distance_big_memory(areas, 3)
#    areas = [1, 3, 1]
#    assert min_distance(areas, 1) == min_distance_big_memory(areas, 1)
    areas = [626720, 853592, 348417, 567318, 935242, 535486, 861639, 736826,
             890527, 626634, 712042, 77047, 111794, 667378, 693993, 610358,
             201182, 534477, 964810, 732166, 58994, 216080, 384632, 595328,
             591949, 871924, 730970, 343972, 906001, 17383, 7445, 296797,
             33211, 328724, 668049, 240293, 659871, 90075, 649888, 664511,
             85680, 232443, 813910, 940087, 793794, 829976, 737034, 458682,
             167893, 612472, 328896, 804759, 281519, 257859, 312193, 163234,
             819560, 906058, 147834, 970099, 434811, 879239, 550138, 458584,
             190964, 687555, 980125, 817604, 444374, 899010, 780317, 303894,
             76323, 156851, 446647, 107095, 513535, 617367, 797334, 214062,
             426374, 587632, 493796, 460566, 654275, 843725, 677915, 351574,
             358909, 93783, 30365, 642969, 247652, 98956, 157187, 816101,
             614401, 361005, 370665, 700318, 542138, 417147, 103290, 167192,
             88303, 67293, 611434, 261606, 184346, 208401, 292603, 357748,
             614080, 887601, 821738, 69021, 986861, 903157, 176798, 645653,
             128952, 377912, 880429, 400132, 14648, 357355, 754544, 942837,
             53090, 292722, 577351, 115003, 219214, 598154, 413976, 791026,
             306175, 941587, 465380, 462470, 933341, 135508, 483309, 318573,
             758842, 632249, 688815, 602873]
#    areas = [1, 3, 8, 5, 5, 12, 5]
    print(min_distance(areas, 5), min_distance_big_memory(areas, 5))


if __name__ == '__main__':
    main()
