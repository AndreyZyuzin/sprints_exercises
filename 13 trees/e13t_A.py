"""Задача A спринта 13 trees.

Лампочки.
Гоша повесил на стену гирлянду в виде бинарного дерева, в узлах которого
находятся лампочки. У каждой лампочки есть своя яркость.
Уровень яркости лампочки соответствует числу, расположенному в узле дерева.
Помогите Гоше найти самую яркую лампочку в гирлянде,
то есть такую, у которой яркость наибольшая.
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

def main():
    root = input_data()
    print(get_max(root))


def test():
    stick1 = Node(14)
    stick2 = Node(15)
    stick3 = Node(8, stick1, stick2)
    stick4 = Node(3)
    stick5 = Node(10, right=stick4)
    stick6 = Node(3, stick3, stick5)
    print(get_max(stick6))



if __name__ == '__main__':
    main()
