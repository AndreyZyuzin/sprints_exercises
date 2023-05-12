"""Задача B спринта 13 trees.

Сбалансированное дерево.
Гоше очень понравилось слушать рассказ Тимофея про деревья.
Особенно часть про сбалансированные деревья.
Он решил написать функцию, которая определяет, сбалансировано ли дерево.
Дерево считается сбалансированным, если левое и правое поддеревья
каждой вершины отличаются по высоте не больше, чем на единицу.
"""
import sys


def input_data():
    """Получение исходные данные."""
    input()
    arr = []
    for line in sys.stdin:
        _, value, left, right = line.strip().split()
        left = None if left == 'None' else int(left)
        right = None if right == 'None' else int(right)
        arr.append({'value': int(value),
                    'left': left,
                    'right': right})
    for item in range(len(arr)-1, -1, -1):
        arr[item] = Node(
            arr[item]['value'],
            arr[arr[item]['left']] if arr[item]['left'] else None,
            arr[arr[item]['right']] if arr[item]['right'] else None,
            )
    return arr[0]


class Node:
    """Элемент дерева."""

    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __str__(self):
        return (f'{self.value}, '
                f'left: {self.left.value if self.left else None}, '
                f'right: {self.right.value if self.right else None}')


def get_max(tree: Node) -> int:
    result = tree.value
    if tree.left:
        value_left = get_max(tree.left)
        if value_left > result:
            result = value_left
    if tree.right:
        value_right = get_max(tree.right)
        if value_right > result:
            result = value_right
    return result


def is_tree(tree: Node) -> bool:
    """Является ли дерево балансированным."""
    def get_level(tree: Node):
        """Определение глубины дерева."""
        left = 0 if tree.left is None else get_level(tree.left)
        if left is False:
            return False
        right = 0 if tree.right is None else get_level(tree.right)
        if right is False:
            return False
        if abs(left - right) >= 2:
            return False
        return 1 + max(left, right)
    result = get_level(tree)
    return False if result is False else True


def main():
    root = input_data()
    print(is_tree(root))


def test():
    stick1 = Node(14)
    # stick101 = Node(101)
    # stick102 = Node(102, stick101)
    # stick1 = Node(14, stick102)
    stick2 = Node(15)
    stick3 = Node(8, stick1, stick2)
    stick4 = Node(3)
    stick5 = Node(10, right=stick4)
    stick6 = Node(3, stick3, stick5)
    print(is_tree(stick6))
    stick201 = Node(201)
    stick202 = Node(202, stick201)
    stick203 = Node(203, stick202)
    print(is_tree(stick202))
    print(is_tree(stick203))



if __name__ == '__main__':
    main()
