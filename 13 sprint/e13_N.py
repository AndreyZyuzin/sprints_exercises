"""Задача N спринта 13.

Клумбы.
Алла захотела, чтобы у неё под окном были узкие клумбы с тюльпанам.
На схеме земельного участка клумбы обозначаются просто горизонтальными
отрезками, лежащими на одной прямой. Для ландшафтных работ было
нанято n садовников. Каждый из них обрабатывал какой-то отрезок на схеме.
Процесс был организован не очень хорошо, иногда один и тот же отрезок
или его часть могли быть обработаны сразу несколькими садовниками.
Таким образом, отрезки, обрабатываемые двумя разными садовниками,
сливаются в один. Непрерывный обработанный отрезок затем станет клумбой.
Нужно определить границы будущих клумб.
"""
import sys
from typing import List



def input_data2():
    """Получение исходные данные."""
    input()
    array = set()
    for line in sys.stdin:
        array.add(tuple(int(number) for number in line.strip().split()))
    return array


def input_data() -> List[list]:
    """Получение исходные данные."""
    input()
    array = []
    for line in sys.stdin:
        array.append([int(number) for number in line.strip().split()])
    return array


def merge(intervals):
    """Слияние меленьких участков в большие."""
    length = len(intervals)

    if length == 1:
        return intervals

    half = length // 2
    left = merge(intervals[:half])
    right = merge(intervals[half:])

    array = [] * length

    l, r, k = 0, 0, 0
    while l < len(left) and r < len(right):
        if left[l][0] <= right[r][0]:
            print(left, array)
            array[k] = left[l]
            l += 1
        else:
            array[k] = right[r]
            r += 1
        k += 1

    while l < len(left):
        array[k] = left[l]
        l += 1
        k += 1

    while r < len(right):
        array[k] = right[r]
        r += 1
        k += 1

    return array


def merge2(intervals: List[list]) -> List[list]:
    """Слияние меленьких участков в большие."""
    intervals.sort(key=lambda interval: interval[0])
    result = [intervals[0]]
    for k_interval in range(1, len(intervals)):
        if intervals[k_interval][0] > result[-1][1]:
            result.append(intervals[k_interval])
            continue
        if intervals[k_interval][1] > result[-1][1]:
            result[-1][1] = intervals[k_interval][1]
    return result


def merge3(intervals: List[list]) -> List[list]:
    """Слияние меленьких участков в большие."""
    intervals.sort(key=lambda interval: interval[0])
    support_intervals = []
    for interval in intervals:
        for second_interval in support_intervals:
            if interval[0] <= second_interval[1]:
                if interval[1] > second_interval[1]:
                    second_interval[1] = interval[1]
                break
        else:
            support_intervals.append(interval)
    return support_intervals


def output(array: List[list]):
    """Отображение результата."""
    for item in array:
        print(' '.join(map(str, item)))


def main():
    intervals = input_data()
    intervals = merge2(intervals)
    output(intervals)


if __name__ == '__main__':
    main()
