"""Задача K спринта 12.

Рекурсивные числа Фибоначчи.
"""
def fibonaci(number: int) -> int:
    """Получение следующее число фибоначчи."""
    return fibonaci(number - 2) + fibonaci(number - 1) if number > 1 else 1

def main():
    number = int(input())
    print(fibonaci(number))


if __name__ == '__main__':
    main()
