"""Задача I спринта 13 hash.

Общий подмассив.
Гоша увлёкся хоккеем и часто смотрит трансляции матчей.
Чтобы более-менее разумно оценивать силы команд, он сравнивает очки,
набранные во всех матчах каждой командой.

Гоша попросил вас написать программу, которая по результатам игр
двух выбранных команд найдёт наибольший по длине отрезок матчей,
когда эти команды зарабатывали одинаковые очки.

Рассмотрим первый пример:
Результаты первой команды: [1 2 3 2 1].
Результаты второй команды: [3 2 1 5 6].
Наиболее продолжительный общий отрезок этих массивов имеет
длину 3 –— это [3 2 1].
"""


def input_data():
    """Получение исходные данные."""
    input()
    arr1 = input()
    input()
    arr2 = input()
    return arr1, arr2


class String2:
    def __init__(self, word: str, koef_a: int = 1000, koef_m: int = 1000009):
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

    def is_sub_word(self, word: str) -> bool:
        """Проверка, что word входит в текущее строку."""
        for index in range(len(self) - len(word) + 2):
            if self.hash(word) == self._hash_sub(index, index + len(word) - 1):
                return True
        return False

    def __str__(self):
        return self.word

    def __len__(self):
        return len(self.word)

    def hash(self, word: str):
        result = 0
        for si in word:
            result = (result * self.__a + ord(si)) % self.__m
        return result


def line_to_string(line: str) -> String2:
    """Преобразование строки чисел в слова ascii."""
    return ''.join([chr(int(code)) for code in line.split()])


def get_length_subword(word1, word2) -> int:
    if word1.is_sub_word(word2):
        return len(word2)

    for l in range(1, len(word2)):
        w1 = word2[l:]
        w2 = word2[:-l]
        if word1.is_sub_word(w1) or word1.is_sub_word(w2):
            return len(word2) - l

#    for l in range(1, len(word2)):
#        if word1.is_sub_word(word2[l:]) or word1.is_sub_word(word2[:-l]):
#            return len(word2) - l
    return 0


def output(res: bool):
    print('YES' if res else 'NO')


def test():
    line1, line2 = '61 62 63 64 65', '64 65 69'
    word1 = line_to_string(line1)
    word2 = line_to_string(line2)
    word1 = 'defghada'
    word2 = 'abcdefgh'
    if len(word1) > len(word2):
        word1, word2 = String2(word1), word2
    else:
        word1, word2 = String2(word2), word1
    print(get_length_subword(word1, word2))


def main():
    line1, line2 = input_data()
    word1 = line_to_string(line1)
    word2 = line_to_string(line2)
    if len(word1) > len(word2):
        word1, word2 = String2(word1), word2
    else:
        word1, word2 = String2(word2), word1
    print(get_length_subword(word1, word2))


if __name__ == '__main__':
    test()
