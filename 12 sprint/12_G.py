"""Задача G спринта 12.

Стек - Max.
"""
import sys


class Stack:
    LIMIT_ITEM = 100000
    def __init__(self):
        self.items = [0] * self.LIMIT_ITEM
        self.__top = -1
        self.__max_items = [0] * self.LIMIT_ITEM

    def push(self, item):
        self.__top += 1
        self.items[self.__top] = item
        if self.__top == 0:
            self.__max_items[self.__top] = item
            return
        previous_max = self.__max_items[self.__top - 1]
        self.__max_items[self.__top] = (item 
                                        if item > previous_max
                                        else previous_max)

    def pop(self):
        if self.__top < 0:
            raise EmptyStackError
        self.__top -= 1

    def get_max(self):
        if self.__top < 0:
            return
        return self.__max_items[self.__top]


class StackError(Exception):
    """Общий класс исключений для Training."""

class EmptyStackError(StackError):
    """Ошибка при попытке получить значение из пустого стека."""
    def __str__(self):
        return 'error'


def test():
    stack = Stack()
    stack.push(0)
    stack.push(5)
    print(stack.get_max())
    stack.pop()
    print(stack.get_max())


def main():
    """Запуск программы."""
    stack = Stack()
    input()
    for line in sys.stdin:
        try:
            commands = line.strip().split()
            command = commands[0]
            if command == 'push':
                stack.push(int(commands[1]))
            if command == 'pop':
                stack.pop()
            if command == 'get_max':
                print(stack.get_max())
        except EmptyStackError as error:
            print(error)



if __name__ == '__main__':
    main()
