"""Задача B спринта 12.

Отобразить список дел.
"""
import sys

LOCAL = True

if LOCAL:
    class Node:
        def __init__(self, value, next_item=None):
            self.value = value
            self.next_item = next_item


def solution(node):
    """Отображение элементов связного списка."""
    while node:
        print(node.value)
        node = node.next_item

def test():
    node3 = Node("node3", None)
    node2 = Node("node2", node3)
    node1 = Node("node1", node2)
    node0 = Node("node0", node1)
    solution(node0)
    # Output is:
    # node0
    # node1
    # node2
    # node3


def main():
    """Запуск программы."""
    head = None
    input()
    for line in sys.stdin:
        node = Node(line.strip(), head)
        head = node
    solution(head)


if __name__ == '__main__':
    main()
