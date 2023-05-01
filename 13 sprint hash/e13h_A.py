"""Задача A спринта 13 hash.

Полиномиальный хеш.
Алле очень понравился алгоритм вычисления полиномиального хеша.
Помогите ей написать функцию, вычисляющую хеш строки s.
В данной задаче необходимо использовать в качестве значений
отдельных символов их коды в таблице ASCII.

Полиномиальный хеш считается по формуле:
h(s) = (s1*a^(n-1) + s2*a^(n-2) + ... + sn) % m
"""
def input_data():
    a = int(input())
    m = int(input())
    s = input()
    return a, m, s


def h(s: str, a: int, m: int):
    result = 0
    for si in s:
        result = (result * a + ord(si)) % m
    return result


def main():
    a, m, s = input_data()
    print(h(s, a, m))


def test():
    assert h('a', 123, 100003) == 97
    assert h('hash', 123, 100003) == 6080
    assert h('HaSH', 123, 100003) == 56156


if __name__ == '__main__':
    test()
