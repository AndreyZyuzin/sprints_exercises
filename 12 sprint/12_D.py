"""Задача D спринта 12.

Поиск дела в списке.
"""
import sys
from typing import Tuple


class Node:
    def __init__(self, value, next_item=None):
        self.value = value
        self.next_item = next_item


def input_data() -> Tuple[Node, str]:
    """Получение исходных данных"""
    head = None
    number = int(input())
    for _ in range(number):
        node = Node(sys.stdin.readline().strip(), head)
        head = node
    element_search = input()
    return head, element_search


def solution(head, element_search):
    """Отображение элементов связного списка был удален элемент."""
    number_node = 0
    while head:
        if head.value == element_search:
            return number_node
        number_node += 1
        head = head.next_item
    return -1


def test():
    node3 = Node("node3", None)
    node2 = Node("node2", node3)
    node1 = Node("node1", node2)
    node0 = Node("node0", node1)
    assert solution(node0, 'node0') == 0
    assert solution(node0, 'node1') == 1
    assert solution(node0, 'node3') == 3
    assert solution(node0, 'node') == -1


def main():
    """Запуск программы."""
    head, element_search = input_data()
    print(str(solution(head, element_search)))


if __name__ == '__main__':
    main()
