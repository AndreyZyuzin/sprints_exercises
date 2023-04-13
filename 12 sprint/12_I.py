"""Задача I спринта 12.

Стек - Max.
"""
import sys
from typing import Any


class MyQueueSized:
    def __init__(self, max_size: int = 5000):
        self.__max_size = max_size
        self.__items = [None] * self.__max_size
        self.__current = 0
        self.__size = 0

    def push(self, value: Any):
        if self.__size >= self.__max_size:
            print('error')
            return
        self.__items[(self.__current + self.__size) % self.__max_size] = value
        self.__size += 1

    def peek(self):
        """Отобразить первый элемент в очереди."""
        print(self.__items[self.__current] if self.__size else 'None')

    def pop(self) -> Any:
        """Отобразить и удалить первый элемент в очереди."""
        if self.__size == 0:
            print('None')
            return
        print(self.__items[self.__current])
        self.__current = (self.__current + 1) % self.__max_size
        self.__size -= 1

    def size(self) -> int:
        return self.__size


def test():
    """Тестирование двусвязного списка."""
    queue = MyQueueSized(6)
    print(queue.size())
    queue.push(1)
    queue.push(2)
    queue.push(3)
    queue.peek()
    queue.pop()
    queue.pop()
    queue.pop()
    queue.pop()
    queue.push(4)
    queue.push(5)
    queue.push(6)
    queue.push(7)
    print(f'{queue._MyQueueSized__items}')
    queue.pop()
    queue.pop()
    queue.pop()
    queue.pop()
    queue.pop()

def main():
    """Запуск программы."""
    input()
    max_size = int(input())
    queue = MyQueueSized(max_size)
    for line in sys.stdin:
        commands = line.strip().split()
        command = commands[0]
        if command == 'push':
            queue.push(int(commands[1]))
        if command == 'pop':
            queue.pop()
        if command == 'peek':
            queue.peek()
        if command == 'size':
            print(queue.size())



if __name__ == '__main__':
    main()
