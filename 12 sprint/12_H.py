"""Задача H спринта 12.

Скобочная последовательность.
"""
import sys


def input_data() -> str:
    """Получение исходных данных."""
    return sys.stdin.readline().strip()


def is_correct_bracket_seq(sequence: str) -> bool:
    """Правильная ли скобочная последовательность."""
    stack = list()
    for char in sequence:
        if char in '{([':
            stack.append(char)
            continue
        try:
            if char == ']' and stack.pop() != '[':
                return False
            elif char == ')' and stack.pop() != '(':
                return False
            elif char == '}' and stack.pop() != '{':
                return False
        except IndexError:
            return False
    return len(stack) == 0


def test():
    """Тестирование функции."""
    assert is_correct_bracket_seq('{[()]}') is True
    assert is_correct_bracket_seq('') is True
    assert is_correct_bracket_seq('[(])') is False
    assert is_correct_bracket_seq('{[())]}') is False


def main():
    """Запуск программы."""
    sequence = input_data()
    print(is_correct_bracket_seq(sequence))


if __name__ == '__main__':
    main()
