"""Финальная задача B спринта 13. (5kyu). id решения - 86337460, 86340780.

Эффективная быстрая сортировка.
Нужна сортировка для таблицы соревнование.
Параметры участников:
- количество решённых задач Pi
- размер штрафа Fi.
Преимущество у куго решено больше задач. При равенстве, у кого меньший штрафом.
При равенстве по алфавиту.

Требования сортировки:
- алгоритм быстрой сортировки;
- не может потреблять O(n) дополнительной памяти для промежуточных данных.

"""
from typing import List


def input_data() -> List[dict]:
    """Получение исходные данные."""
    n_line = int(input())
    array = [None] * n_line
    for k_line in range(n_line):
        name, n_exersices, penalty = input().split()
        array[k_line] = {'name': name,
                         'n_exersices': int(n_exersices),
                         'penalty': int(penalty)}
    return array


def is_more(item_1, item_2) -> bool:
    """Сравнеие двух элементов.
    Если item_1 > item_2, то True.
    """
    if item_1['n_exersices'] > item_2['n_exersices']:
        return True
    if item_1['n_exersices'] < item_2['n_exersices']:
        return False
    if item_1['penalty'] < item_2['penalty']:
        return True
    if item_1['penalty'] > item_2['penalty']:
        return False
    return item_1['name'] < item_2['name']


def quick_sort(array, left=0, right=None):
    """Быстрая сортировка.

    Аллгоритм:
    Последний элемент задаем опорным. Сохраняем его в отдельную переменную.
    Добавляем переменные для первого и конечного индекса (ноль и предпоследний)
    Перемещаемся слева направа до первого элемента, который больше опорного.
    Полученный элемент перемещается в индекс, который был опорным.
    Индекс элемента, который был сохранен, становится новым пустым элементом.
    Новый владелец ищем справа налево и ищем первый элемент меньше опорного.
    Найденный элемент перемещается в бывший пустой элемент.
    Все продолжается, когда индексы первого и последнего элемента совпадает.
    Он является пустым элементом. Поэтому возращаем значение опорного элемента.
    Теперь элементы до опорного рекурсивно вызываются в текущую функцию.
    То же происходит с элементами после опорного.
    """
    if right is None:
        right = len(array) - 1

    empty_index = right
    pivot = array[empty_index]

    first, last = left - 1, right

    while True:
        while first < last:
            first += 1
            if is_more(array[first], pivot):
                continue
            array[empty_index] = array[first]
            empty_index = first
            break
        else:
            break

        while first < last:
            last -= 1
            if not is_more(array[last], pivot):
                continue
            array[empty_index] = array[last]
            empty_index = last
            break
        else:
            break
    array[empty_index] = pivot

    if empty_index - left > 1:
        quick_sort(array, left, empty_index - 1)
    if right - empty_index > 1:
        quick_sort(array, empty_index + 1, right)


def quick_sort2(array, left=0, right=None):
    """Быстрая сортировка.

    То же самое, что quick().
    Вместо каскада while, заменена меняющая функция от события.
    """
    def go_from_left_to_right():
        """Проверяем один элемент при направление слева направа."""
        nonlocal first, empty_index
        first += 1
        if is_more(array[first], pivot):
            return go_from_left_to_right
        array[empty_index] = array[first]
        empty_index = first
        return go_from_right_to_left

    def go_from_right_to_left():
        """Проверяем один элемент при направление слева направа."""
        nonlocal last, empty_index
        last -= 1
        if not is_more(array[last], pivot):
            return go_from_right_to_left
        array[empty_index] = array[last]
        empty_index = last
        return go_from_left_to_right

    if right is None:
        right = len(array) - 1

    empty_index = right
    pivot = array[empty_index]

    first, last = left - 1, right

    go_step = go_from_left_to_right

    while first < last:
        go_step = go_step()
    array[empty_index] = pivot

    if empty_index - left > 1:
        quick_sort2(array, left, empty_index - 1)
    if right - empty_index > 1:
        quick_sort2(array, empty_index + 1, right)


def output(records: List[dict]):
    for record in records:
        print(record['name'])


def main():
    records = input_data()
    quick_sort2(records)
    output(records)


if __name__ == '__main__':
    main()
