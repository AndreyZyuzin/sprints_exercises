"""Задача C спринта 13 hash.

Префиксные хеши.
Алла не остановилась на достигнутом –— теперь она хочет научиться
быстро вычислять хеши произвольных подстрок данной строки. Помогите ей!

На вход поступают запросы на подсчёт хешей разных подстрок.
Ответ на каждый запрос должен выполняться за O(1). Допустимо в начале работы
программы сделать предподсчёт для дальнейшей работы со строкой.

Напомним, что полиномиальный хеш считается по формуле
h(s) = (s1*a^(n-1) + s2*a^(n-2) + ... + sn) % m
"""
import sys


def input_data():
    a = int(input())
    m = int(input())
    s = input()
    _ = input()
    arr = [list(map(int, line.strip().split())) for line in sys.stdin]
    return a, m, s, arr


class String2:
    def __init__(self, word: str, koef_a: int, koef_m: int):
        self.word = word
        self.__a = koef_a
        self.__m = koef_m
        self._init_hash()

    def _init_hash(self):
        self.__hash = [0] * len(self.word)
        self.__hash_pow = [1] * len(self.word)
        tmp = 0
        for i_s, si in enumerate(self.word):
            tmp = (tmp * self.__a + ord(si)) % self.__m
            self.__hash[i_s] = tmp
        for i in range(1, len(self.word)):
            self.__hash_pow[i] = self.__hash_pow[i - 1] * self.__a % self.__m

    def _hash_sub(self, left: int, right: int) -> int:
        left -= 1
        right -= 1
        result = self.__hash[right]
        if left:
            result -= self.__hash[left-1] * self.__hash_pow[right - left + 1]
        return result % self.__m

    def __str__(self):
        return self.word


def hash(s: str, a: int, m: int):
    result = 0
    for si in s:
        result = (result * a + ord(si)) % m
    return result


def test():
    a, m, s = 1000, 1000009, 'abcdefgh'
    word = String2(s, a, m)
    arr = ((1, 1), (1, 5), (2, 3), (3, 4), (4, 4), (1, 8), (5, 8))
    print(word, word._String2__hash, word._String2__hash_pow)
    for begin, end in arr:
        print(begin, end, hash(s[begin-1:end], a, m), end=' ')
        print(word._hash_sub(begin, end))


def test2():
    a, m, s = 3, 7, ''.join(map(chr, [3, 5, 12, 7]))
    word = String2(s, a, m)
    arr = ((1, 1), (1, 2), (1, 3), (1, 4), (2, 2), (2, 3), (2, 4), (3, 3), (3, 4), (4, 4))
    print(word, word._String2__hash, word._String2__hash_pow)
    for begin, end in arr:
        print(begin, end, hash(s[begin-1:end], a, m), end=' ')
        print(word._hash_sub(begin, end))


def main():
    a, m, s, arr = input_data()
    word = String2(s, a, m)
    for begin, end in arr:
        # print(begin, end, hash(s[begin-1:end], a, m), end=' ')
        print(word._hash_sub(begin, end))


if __name__ == '__main__':
    main()
