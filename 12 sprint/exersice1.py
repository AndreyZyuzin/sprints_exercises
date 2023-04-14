"""Финальная задача 1 спринта 12.

Дек.
Deque - 85590520
Deque2 - 85590429
Отличие, когда начало и конец это один и тотже элемент, каким образом
определять - это пустота или переполнение.
"""
import sys
from typing import Tuple

class Deque:
    """Реализация дека."""

    def __init__(self, max_size: int = 50_000):
        self.__max_size = max_size
        self.__items = [0] * self.__max_size
        self.__front = 0
        self.__size = 0

    def get_direct_index(self, current_index) -> int:
        """Получение индекса в массиве из расчетного индекса."""
        return current_index % self.__max_size

    def is_overflow(self) -> bool:
        """Является ли заплнен дек."""
        return self.__size == self.__max_size

    def is_empty(self) -> bool:
        """Является ли пустой дек."""
        return self.__size == 0

    def push_back(self, value: int):
        """Добавить элемент в конец дека."""
        if self.is_overflow():
            raise DequeError('error')
        self.__size += 1
        self.__items[self.get_direct_index(self.__front - self.__size)] = value

    def push_front(self, value: int):
        """Добавить элемент в начало дека."""
        if self.is_overflow():
            raise DequeError('error')
        self.__size += 1
        self.__items[self.__front] = value
        self.__front = self.get_direct_index(self.__front + 1)

    def pop_front(self) -> int:
        """Вывести первый элемент дека и удалить его."""
        if self.is_empty():
            raise DequeError('error')
        self.__size -= 1
        self.__front = self.get_direct_index(self.__front - 1)
        result = self.__items[self.__front]
        print(result)
        return result

    def pop_back(self) -> int:
        """Вывести последний элемент дека и удалить его."""
        if self.is_empty():
            raise DequeError('error')
        result = self.__items[
            self.get_direct_index(self.__front - self.__size)]
        print(result)
        self.__size -= 1
        return result

    def run_commands(self, commands: list):
        """Запустить команды."""
        for command, *args in commands:
            try:
                self.__getattribute__(command)(*args)
            except DequeError as error:
                print(error)


class Deque2:
    """Реализация дека."""

    def __init__(self, max_size: int = 50_000):
        self.__max_size = max_size
        self.__items = [0] * self.__max_size
        self.__front = 0
        self.__back = 0

    def get_direct_index(self, current_index) -> int:
        """Получение индекса в массиве из расчетного индекса."""
        return current_index % self.__max_size

    def is_overflow(self) -> bool:
        """Является ли заплнен дек."""
        return self.__front - self.__back >= self.__max_size

    def is_empty(self) -> bool:
        """Является ли пустой дек."""
        return self.__front == self.__back

    def push_back(self, value: int):
        """Добавить элемент в конец дека."""
        if self.is_overflow():
            raise DequeError('error')
        self.__back -= 1
        self.__items[self.get_direct_index(self.__back)] = value

    def push_front(self, value: int):
        """Добавить элемент в начало дека."""
        if self.is_overflow():
            raise DequeError('error')
        self.__items[self.get_direct_index(self.__front)] = value
        self.__front = self.__front + 1

    def pop_front(self) -> int:
        """Вывести первый элемент дека и удалить его."""
        if self.is_empty():
            raise DequeError('error')
        self.__front -= 1
        result = self.__items[self.get_direct_index(self.__front)]
        print(result)
        return result

    def pop_back(self) -> int:
        """Вывести последний элемент дека и удалить его."""
        if self.is_empty():
            raise DequeError('error')
        result = self.__items[self.get_direct_index(self.__back)]
        print(result)
        self.__back += 1
        return result

    def run_commands(self, commands: list):
        """Запустить команды."""
        for command, *args in commands:
            try:
                self.__getattribute__(command)(*args)
            except DequeError as error:
                print(error)


class DequeError(Exception):
    """Общий класс исключений для Deque."""


def input_data() -> Tuple[int, list]:
    """Получение исходных данных."""
    input()
    max_size = int(input())
    commands = []
    for line in sys.stdin:
        command, *args = line.strip().split()
        commands.append((command, *args))
    return max_size, commands


def run_commands(deque: Deque, commands: list):
    """Запустить команды."""
    for command, *args in commands:
        try:
            getattr(deque, command)(*args)
        except DequeError as error:
            print(error)


def main():
    """Запуск программы."""
    max_size, commands = input_data()
    deque = Deque2(max_size)
    deque.run_commands(commands)


if __name__ == '__main__':
    main()
