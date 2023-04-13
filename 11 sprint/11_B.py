import sys


def get_result_game(numbers: list) -> str:
    """Поучает результат игры.
    Если все числа четные или все - нечетные, то WIN,
    иначе FAIL.
    По правилам должно быть 3 числа,
    то есть кол-ва элементов не бывает 0."""
    isOdd = numbers[0] % 2
    for number in numbers[1:]:
        if number%2 != isOdd:
            return "FAIL"
    return "WIN"


line = sys.stdin.readline().strip()
numbers = list(map(int, line.split()))

print(get_result_game(numbers))
