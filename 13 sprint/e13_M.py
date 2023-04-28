"""Задача M спринта 13.

Золотая середина.
На каждом острове в архипелаге Алгосы живёт какое-то количество людей
или же остров необитаем (тогда на острове живёт 0 людей).
Пусть на i-м острове численность населения составляет ai.
Тимофей захотел найти медиану среди всех значений численности населения.
"""

def input_data():
    """Получение исходные данные."""
    a_n = input()
    b_n = input()
    array_a = tuple(map(int, input().split()))
    array_b = tuple(map(int, input().split()))
    return array_a, array_b


def input_data2():
    """Получение исходные данные."""
    _ = input()
    _ = input()
    array_a = [int(item) for item in input().split()]
    array_b = [int(item) for item in input().split()]
    return array_a, array_b


def get_median_slow(array_a, array_b):
    """Получение медиану общую двух упорядоченных массивов.
    Медленный, но наиболее понятный алгоритм."""
    array = array_a + array_b
    array.sort()
    len_array = len(array)
    half = len_array // 2
    if len_array % 2:
        return array[half]
    return (array[half-1] + array[half])/2


def get_median_order_array(first, second):
    if len(first) == len(second):
        return (first[-1] + second[0]) / 2
    length = len(first) + len(second)
    if len(first) > len(second):
        half = length // 2
        return first[half] if length % 2 else (first[half - 1] + first[half])/2
    half = length // 2 - len(first)
    return second[half] if length % 2 else (second[half - 1] + second[half])/2


def place_matching(len_a, len_b, k_place):
    """Место в первом массиве. Ищем второй. У обоих должны одинаковые
    количетво чисел слева и справа.
    [0 1 2 3] [0 1 2 3 4 5] - 2 2; 0 4
    [0 1 2 3] [0 1 2 3 4] - 2 (1 2)

    [0 1 2 3] [0 1 2 3 4 5] - 4+6-1=9; 9 - 1*2 - 1 = 6 -> 6/2 = 3
    [0 1 2 3] [0 1 2 3 4]   - 4+5-1=8; 8 - 1*2 - 1 = 5 -> 5/2 = 2.5
    """
    m_place = len_a + len_b - 2 - k_place * 2
    return m_place


def get_median(arr_a, arr_b):
    """Получение медиану общую двух упорядоченных массивов.

    Если меньший массив - пустой, то легко определяется медиану.
    Если левый элемент больше правого элемента другого массива,
    то легко определяется. Аналогично, если правый элемент меньше левого
    элемента левого элемента другого массива, то легко определяестя.
    Ищем в цикле:
    для суммрно-четных - берем серидину и сравниваем
        с соответствующую величину. От результата сдвигаемся
        слева или справа. Когда остались два соседние и ему сооответствующий,
        то находим медиану между четырми значения.
    для суммарно-нечетных - берем середину h1, у него два соответствия b1 и b2.
        Если b1 < h1 < b2, то найденный результат - h1. Если нет, сдвигаем
        или вправа или слева. Если остались два соседних элемента и
        не смогли медиану, то медиана в другом массиве. Результат - это общая
        соответсвующее значение для обоих соседей.
    """
    if len(arr_a) >= len(arr_b):
        big, small = arr_a, arr_b
    else:
        big, small = arr_b, arr_a

    len_small, len_big = len(small), len(big)
    lenghts = len_small + len_big
    is_odd = (len_small + len_big) % 2
    if not len_small:
        half = len_big // 2
        return big[half] if is_odd else (big[half - 1] + big[half]) / 2

    if small[-1] <= big[(len_big - len_small - 1) // 2]:
        return get_median_order_array(small, big)
    if len_small == len_big:
        if small[0] >= big[-1]:
            return get_median_order_array(big, small)
    elif small[0] >= big[lenghts // 2]:
        return get_median_order_array(big, small)

    left, right = 0, len_small - 1
    if is_odd:
        while True:
            half = (right + left) // 2
            value_small = small[half]
            value_big_1 = big[lenghts // 2 - 1 - half]
            if value_small == value_big_1:
                return value_small
            if value_small < value_big_1:
                left = half
            else:
                value_big_2 = big[lenghts // 2 - half]
                if value_small <= value_big_2:
                    return value_small
                right = half
            if right - left <= 1:
                return big[lenghts // 2 - left - 1]

    while right - left > 1:
        half = (right + left) // 2
        value_small = small[half]
        value_big = big[lenghts // 2 - 1 - half]
        if value_small == value_big:
            return value_small
        if value_small < value_big:
            left = half
        else:
            right = half
    return (max(small[left], big[lenghts // 2 - 1 - right])
            + min(small[right], big[lenghts // 2 - 1 - left])) / 2


def main():
    array_a, array_b = input_data()
    print(get_median(array_a, array_b))


def test():
    a = [0.1, 6.2, 6.3, 6.4]
    b = [4.1, 4.2, 4.3, 4.5, 7.2]
    median = get_median_slow(a, b)
    print(median, get_median(a, b))

if __name__ == '__main__':
    main()
