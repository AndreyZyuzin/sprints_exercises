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
from dataclasses import dataclass


@dataclass
class Member:
    """Участник соревнования."""
    name: str
    n_exersices: int
    penalty: int

    def __gt__(self, other):
        """Сравнеие двух элементов."""
        if self.n_exersices > other.n_exersices:
            return True
        if self.n_exersices < other.n_exersices:
            return False
        if self.penalty < other.penalty:
            return True
        if self.penalty > other.penalty:
            return False
        return self.name < other.name

    def __lt__(self, other):
        """Сравнеие двух элементов."""
        if self.n_exersices < other.n_exersices:
            return True
        if self.n_exersices > other.n_exersices:
            return False
        if self.penalty > other.penalty:
            return True
        if self.penalty < other.penalty:
            return False
        return self.name > other.name


def input_data() -> List[Member]:
    """Получение исходные данные."""
    n_line = int(input())
    array = [None] * n_line
    for k_line in range(n_line):
        name, n_exersices, penalty = input().split()
        array[k_line] = Member(name, int(n_exersices), int(penalty))
    return array


def quick_sort(members, left=0, right=None):
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
        right = len(members) - 1

    empty_index = right
    pivot = members[empty_index]

    first, last = left - 1, right

    while True:
        while first < last:
            first += 1
            if members[first] > pivot:
                continue
            members[empty_index] = members[first]
            empty_index = first
            break
        else:
            break

        while first < last:
            last -= 1
            if members[last] < pivot:
                continue
            members[empty_index] = members[last]
            empty_index = last
            break
        else:
            break
    members[empty_index] = pivot

    if empty_index - left > 1:
        quick_sort(members, left, empty_index - 1)
    if right - empty_index > 1:
        quick_sort(members, empty_index + 1, right)


def quick_sort2(members, left=0, right=None):
    """Быстрая сортировка.

    То же самое, что quick().
    Вместо каскада while, заменена меняющая функция от события.
    """
    def go_from_left_to_right():
        """Проверяем один элемент при направление слева направа."""
        nonlocal first, empty_index
        first += 1
        if members[first] > pivot:
            return go_from_left_to_right
        members[empty_index] = members[first]
        empty_index = first
        return go_from_right_to_left

    def go_from_right_to_left():
        """Проверяем один элемент при направление слева направа."""
        nonlocal last, empty_index
        last -= 1
        if members[last] < pivot:
            return go_from_right_to_left
        members[empty_index] = members[last]
        empty_index = last
        return go_from_left_to_right

    if right is None:
        right = len(members) - 1

    empty_index = right
    pivot = members[empty_index]

    first, last = left - 1, right

    go_step = go_from_left_to_right

    while first < last:
        go_step = go_step()
    members[empty_index] = pivot

    if empty_index - left > 1:
        quick_sort2(members, left, empty_index - 1)
    if right - empty_index > 1:
        quick_sort2(members, empty_index + 1, right)


def output(members: List[Member]):
    for member in members:
        print(member.name)


def main():
    members = input_data()
    quick_sort(members)
    output(members)


if __name__ == '__main__':
    main()
