"""Задача I спринта 13 hash.

Общий подмассив.
Гоша увлёкся хоккеем и часто смотрит трансляции матчей.
Чтобы более-менее разумно оценивать силы команд, он сравнивает очки,
набранные во всех матчах каждой командой.

Гоша попросил вас написать программу, которая по результатам игр
двух выбранных команд найдёт наибольший по длине отрезок матчей,
когда эти команды зарабатывали одинаковые очки.

Рассмотрим первый пример:
Результаты первой команды: [1 2 3 2 1].
Результаты второй команды: [3 2 1 5 6].
Наиболее продолжительный общий отрезок этих массивов имеет
длину 3 –— это [3 2 1].
"""


def input_data():
    """Получение исходные данные."""
    input()
    arr1 = input()
    input()
    arr2 = input()
    return arr1, arr2


def get_numbers(line: str) -> list:
    return list(map(int, line.split()))


def get_indexes(arr: list, value: int) -> list:
    """Получаем для всех значений массива свои индексы."""
    return [index for index, item in enumerate(arr) if item == value]

def get_length_sequence(arr1, arr2, current_max=0) -> int:
    """Получаем саммую длинную последовательность в обоих массивах."""
    if current_max >= len(arr1) or current_max >= len(arr2):
        return current_max
    if len(arr1) < len(arr2):
        arr1, arr2 = arr2, arr1
    middle1 = len(arr1) // 2
    items = get_indexes(arr2, arr1[middle1])
    if items:
        for item in items:
            len_right = 1
            while (item+len_right < len(arr2)
                   and middle1+len_right < len(arr1)
                   and arr1[middle1+len_right] == arr2[item+len_right]
                   ):
                len_right += 1
            len_left = -1
            while (item+len_left >= 0
                   and middle1+len_left >= 0
                   and arr1[middle1+len_left] == arr2[item+len_left]
                   ):
                len_left -= 1
            if len_right-len_left-1 > current_max:
                current_max = len_right-len_left-1
    len_left = get_length_sequence(arr1[:middle1], arr2, current_max)
    if len_left > current_max:
        current_max = len_left
    len_right = get_length_sequence(arr1[middle1+1:], arr2, current_max)
    if len_right > current_max:
        current_max = len_right
    return current_max




def test():
    line1, line2 = '1 3 2 1 3 2 2', '1 4 3 2 1'
    line1, line2 = '1 3 2 1 3 2 2 1 2', '1 4 3 2 1'
    arr1, arr2 = get_numbers(line1), get_numbers(line2)
    assert get_length_sequence(arr1, arr2) == 3

    line1, line2 = '1 3 2 1 3 2 2 1 2', '11 14 13 12 11'
    arr1, arr2 = get_numbers(line1), get_numbers(line2)
    assert get_length_sequence(arr1, arr2) == 0

    line1, line2 = '1 3 2 1 3 2 2 1 2', '1 1 3 2 1'
    arr1, arr2 = get_numbers(line1), get_numbers(line2)
    assert get_length_sequence(arr1, arr2) == 4

    line1, line2 = '1 3 1 1 1 1 1 1 2 1 2 2 2 2 2 2 2 2 2 2', '1 1 1 1 3 2 1'
    arr1, arr2 = get_numbers(line1), get_numbers(line2)
    assert get_length_sequence(arr1, arr2) == 4



def main():
    line1, line2 = input_data()
    arr1, arr2 = get_numbers(line1), get_numbers(line2)
    print(get_length_sequence(arr1, arr2))



if __name__ == '__main__':
    main()
