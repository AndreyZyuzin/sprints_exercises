"""Финальная задача 2 спринта 12.

Калькулятор.
id = 85590356
"""
import operator
from typing import Union

OPERATIONS = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.floordiv,
}


class Stack():
    """Реализация стека."""

    def __init__(self, max_size: int = 1000):
        self.__max_size = max_size
        self.__items = [0] * max_size
        self.__top = -1

    def __increase_size(self):
        """Увеличение размер массива для стека."""
        self.__items = self.__items + [0] * self.__max_size
        self.__max_size *= 2

    def append(self, item: Union[int, str]) -> None:
        """Добавить в стек."""
        self.__top += 1
        if self.__top == self.__max_size:
            self.__increase_size()
        self.__items[self.__top] = item

    def pop(self) -> Union[int, str]:
        """Получение значение из верхушки стека."""
        if self.__top < 0:
            raise StackError('Ошибка при попытке получить значение '
                             'из пустоко стека')
        result = self.__items[self.__top]
        self.__top -= 1
        return result

    push = append
    # Поддержка метода, принятого для стека.


class StackError(Exception):
    """Общий класс исключений для Stack."""


def input_data() -> str:
    """Получение исходных данных"""
    return input()


def get_elements(line: str) -> list:
    """Преобразование строки в массив расчётных элементов."""
    return line.split()


def calculator(elements: list) -> int:
    """Расчет выражения."""
    stack = Stack()
    for element in elements:
        if element not in '+-/*':
            stack.append(element)
            continue
        second = int(stack.pop())
        first = int(stack.pop())
        stack.append(OPERATIONS[element](first, second))
    return stack.pop()


def main():
    """Запуск программы."""
    elements = get_elements(input_data())
    print(str(calculator(elements)))


if __name__ == '__main__':
    main()
