"""Задача L спринта 12.

Рекурсивные числа Фибоначчи.
"""
import sys


def fibonaci(number: int, power: int) -> int:
    """Получение число фибоначчи."""
    divider = 10**power
    a, b = 1, 1
    for _ in range(number - 1):
        c = (a + b) % divider
        a = b
        b = c
    return b

def main():
    line = sys.stdin.readline().strip()
    number, power = map(int, line.split())
    print(fibonaci(number, power))


if __name__ == '__main__':
    main()
