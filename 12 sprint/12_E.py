"""Задача D спринта 12.

Поиск дела в списке.
"""
import sys
from typing import Tuple


class Node:
    def __init__(self, value, next_item=None, previous_item=None):
        self.value = value
        self.next_item = next_item
        if next_item:
            next_item.previous_item = self
        self.previous_item = previous_item
        if previous_item:
            previous_item.next_item = self


def input_data() -> Node:
    """Получение исходных данных"""
    input()
    head = None
    for line in sys.stdin:
        node = Node(line.strip(), head)
        head = node
    return head


def solution2(node: Node) -> None:
    """Отображение элементов связного списка в обратном порядке."""
    if not node:
        return
    while node.next_item:
        node = node.next_item
    while node:
        print(node.value)
        node = node.previous_item


def solution(node: Node) -> None:
    """Отображение элементов связного списка в обратном порядке."""
    if not node:
        return
    while node:
        print(node.value)
        node = node.next_item


def test():
    node3 = Node("node3", None)
    node2 = Node("node2", node3)
    node1 = Node("node1", node2)
    node0 = Node("node0", node1)
    solution(node0)
#   node3 -> node2 -> node1 -> node0


def main():
    """Запуск программы."""
    head = input_data()
    solution(head)


if __name__ == '__main__':
    main()
