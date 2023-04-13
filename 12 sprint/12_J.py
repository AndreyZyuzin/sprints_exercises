"""Задача I спринта 12.

Стек - Max.
"""
import sys
from typing import Any


class Node:
    """Элемент связного списка."""
    def __init__(self, value: Any, node_next=None) -> None:
        self.value = value
        self.next = node_next

    def __str__(self):
        return f'{self.value} ({self.next.value if self.next else None})'


class MyLinkedQueue:
    def __init__(self):
        self.__head = None

    def get(self) -> Any:
        if not self.__head:
            print('error')
            return
        print(self.__head.value)
        self.__head = self.__head.next

    def put(self, value: Any):
        if not self.__head:
            self.__head = Node(value)
            return
        node = self.__head
        while node.next:
            node = node.next
        node.next = Node(value)

    def size(self) -> int:
        """Определение размер очереди."""
        count = 0
        node = self.__head
        while node:
            node = node.next
            count += 1
        print(count)


def test():
    """Тестирование связного списка."""
    node0 = Node('node0')
    node1 = Node('node1', node0)
    node2 = Node('node2', node1)
    node3 = Node('node3', node2)
    print(f'node3: {node3}')
    print(f'node2: {node2}')
    print(f'node1: {node1}')
    print(f'node0: {node0}')
    assert node2.next == node1
    assert node2.next.next == node0
    assert node3.next.next.next == node0



def main():
    """Запуск программы."""
    input()
    queue = MyLinkedQueue()
    for line in sys.stdin:
        commands = line.strip().split()
        command = commands[0]
        if command == 'put':
            queue.put(int(commands[1]))
        if command == 'get':
            queue.get()
        if command == 'size':
            queue.size()



if __name__ == '__main__':
    main()
