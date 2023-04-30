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


def update_destances(counter: dict, k_dist: int):
    """Определение значение первых k_dist минимальных чисел."""
    keys = (sorted(counter.keys()))
    k_key = 0
    while True:
        key_pred = keys[k_key]
        value_pred = counter[key_pred]
        k_key += 1
        if k_dist <= value_pred:
            result = key_pred
            break
        key_next = keys[k_key]
        k_dist -= value_pred    
    while k_key < len(keys):
        del counter[keys[k_key]]
        k_key += 1
    return result


def min_distance(areas: List[int], k_distance: int = 1):
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
    """
    areas.sort()
    min_pass = areas[-1]
    result = areas[-1]
    n = len(areas)
    distances = {}
    lines_from_k_distance = math.ceil(
        (2*n - 1 - math.sqrt(4*n*n - 4*n + 1 - 8*k_distance))/2
    )

    for j in range(0, len(areas) - lines_from_k_distance):
        distance = areas[lines_from_k_distance+j] - areas[j]
        if distance < min_pass:
            min_pass = distance
        if distance in distances:
            distances[distance] += 1
        else:
            distances[distance] = 1

    for i in range(lines_from_k_distance - 1, 0, -1):
        max_pass = 0
        for j in range(0, len(areas)-i):
            distance = areas[i+j] - areas[j]
            if distance <= min_pass:
                distances[min_pass] += 1
                continue
            if distance > max_pass:
                max_pass = distance
            if distance in distances:
                distances[distance] += 1
            else:
                distances[distance] = 1
        if max_pass <= min_pass:
            k_distance -= (2*n - i) * (i - 1) // 2
            break

    result = update_destances(distances, k_distance)
    for i in range(lines_from_k_distance + 1, len(areas)):
        min_pass = areas[-1]
        for j in range(0, len(areas)-i):
            distance = areas[i+j] - areas[j]
            if distance >= result:
                continue
            if distance < min_pass:
                min_pass = distance
            if distance in distances:
                distances[distance] += 1
            else:
                distances[distance] = 1
        # min_pass полученных после прохода. В следующим проходе не могут
        # быть значения ниже этого. Можно засуммировать значения с
        # маленькими ключами. Если полученные результаты минимум остравов
        # ниже min_pass, то следует прекратить. результаты не изменятся.
        result = update_destances(distances, k_distance)
        if result <= min_pass:
            return result
    return result


def update_destances2(counter: dict, k_dist: int, minimum: int):
    """Определение значение первых k_dist минимальных чисел."""
    keys = (sorted(counter.keys()))
    k_key = 0
    while True:
        key_pred = keys[k_key]
        value_pred = counter[key_pred]
        k_key += 1
        if k_dist <= value_pred:
            result = key_pred
            break
        key_next = keys[k_key]
        if key_next > minimum:
            k_dist -= value_pred
            continue
        counter[key_next] += value_pred
        del counter[key_pred]
    while k_key < len(keys):
        del counter[keys[k_key]]
        k_key += 1
    return result


def min_distance2(areas: List[int], k_distance: int = 1):
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
    """
    areas.sort()
    result = min_pass = areas[-1]
    n = len(areas)
    distances = {}
    lines_from_k_distance = math.ceil(
        (2*n - 1 - math.sqrt(4*n*n - 4*n + 1 - 8*k_distance))/2
    )
    for j in range(0, len(areas) - (lines_from_k_distance)):
        distance = areas[lines_from_k_distance+j] - areas[j]
        if distance < min_pass:
            min_pass = distance
        if distance in distances:
            distances[distance] += 1
        else:
            distances[distance] = 1

    for i in range(1, lines_from_k_distance):
        for j in range(0, len(areas)-i):
            distance = areas[i+j] - areas[j]
            if distance <= min_pass:
                distances[min_pass] += 1
                continue
            if distance in distances:
                distances[distance] += 1
            else:
                distances[distance] = 1

    result = update_destances2(distances, k_distance, min_pass)
    for i in range(lines_from_k_distance + 1, len(areas)):
        min_pass = areas[-1]
        for j in range(0, len(areas)-i):
            distance = areas[i+j] - areas[j]
            if distance >= result:
                continue
            if distance < min_pass:
                min_pass = distance
            if distance in distances:
                distances[distance] += 1
            else:
                distances[distance] = 1
        # min_pass полученных после прохода. В следующим проходе не могут
        # быть значения ниже этого. Можно засуммировать значения с
        # маленькими ключами. Если полученные результаты минимум остравов
        # ниже min_pass, то следует прекратить. результаты не изменятся.
        result = update_destances2(distances, k_distance, min_pass)
        if result <= min_pass:
            return result
    return result


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
    k = 5466
    # areas = [1, 3, 8, 5, 5, 12, 5]; k = 15
    # areas = [21, 97, 54, 59, 97, 36, 51, 99, 77, 99, 76, 75, 13, 73, 86, 21, 27, 29, 55, 57]; k = 125
    # k, areas = 400, [303, 977, 983, 158, 50, 152, 155, 468, 633, 154, 100, 581, 142, 512, 338, 510, 424, 932, 417, 487, 928, 122, 385, 772, 664, 597, 941, 633, 105, 991, 182, 321, 309, 184, 401]


    print(min_distance_big_memory(areas, k), min_distance(areas, k))


if __name__ == '__main__':
    main()
