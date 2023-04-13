import sys

n_days = int(input())
line = sys.stdin.readline().rstrip()
temperatures = list(map(int, line.split()))


def get_random_factor(temperatures: list) -> int:
    """Получить хаотичностью погоды.

    Вчера и завтра должна быть положительная тенденция темературы.
    """
    n_days = len(temperatures)
    if n_days == 1:
        return 1
    k_day = 1
    res = 0
    while k_day < n_days - 1:
        if (temperatures[k_day] > temperatures[k_day - 1] and
            temperatures[k_day] > temperatures[k_day + 1]):
            res += 1
        k_day += 1
    if temperatures[0] > temperatures[1]:
        res += 1
    if temperatures[-1] > temperatures[-2]:
        res += 1
    return res

print(str(get_random_factor(temperatures)))
