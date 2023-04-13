"""Задача C спринта 12.

Отобразить список дел.
"""
import sys

LOCAL = True

if LOCAL:
    class Node:
        def __init__(self, value, next_item=None):
            self.value = value
            self.next_item = next_item


def print_linked_list(node):
    while node:
        print(node.value)
        node = node.next_item


def solution2(head, number_element):
    """Отображение элементов связного списка был удален элемент."""
    if number_element == 0:
        print_linked_list(head.next_item)
        return head.next_item
    node = head
    while True:
        if number_element <= 1:
            break
        number_element -= 1
        node = node.next_item
    node.next_item = node.next_item.next_item
    print_linked_list(head)
    return head


def solution(head, number_element):
    """Отображение элементов связного списка был удален элемент."""
    if number_element == 0:
        print_linked_list(head.next_item)
        return head.next_item
    node = head
    while number_element > 1:
        number_element -= 1
        node = node.next_item
    node.next_item = node.next_item.next_item
    print_linked_list(head)
    return head

def test():
    node3 = Node("node3", None)
    node2 = Node("node2", node3)
    node1 = Node("node1", node2)
    node0 = Node("node0", node1)
    new_head = solution(node0, 1)
    assert new_head is node0
    assert new_head.next_item is node2
    assert new_head.next_item.next_item is node3
    assert new_head.next_item.next_item.next_item is None
    # result is node0 -> node2 -> node3


def test2():
    node3 = Node("node3", None)
    node2 = Node("node2", node3)
    node1 = Node("node1", node2)
    node0 = Node("node0", node1)
    new_head = solution(node0, 0)
    assert new_head is node1
    assert new_head.next_item is node2
    assert new_head.next_item.next_item is node3
    assert new_head.next_item.next_item.next_item is None
    # result is node1 -> node2 -> node3


def test3():
    node1 = Node("node1", None)
    node0 = Node("node0", node1)
    new_head = solution(node0, 0)
    assert new_head is node1
    assert new_head.next_item is None
    # result is node1


def test4():
    node1 = Node("node1", None)
    node0 = Node("node0", node1)
    new_head = solution(node0, 1)
    assert new_head is node0
    assert new_head.next_item is None
    # result is node0


def main():
    """Запуск программы."""
    head = None
    number = int(input())
    for _ in range(number):
        node = Node(sys.stdin.readline().strip(), head)
        head = node
    number = int(input())
    solution(head, number)


if __name__ == '__main__':
    main()
    # test()
    # test2()
    # test3()
    # test4()
