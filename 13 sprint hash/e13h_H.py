"""Задача H спринта 13 hash.

Странное сравнение.
Жители Алгосского архипелага придумали новый способ сравнения строк.
Две строки считаются равными, если символы одной из них можно заменить
на символы другой так, что первая строка станет точной копией второй строки.
При этом необходимо соблюдение двух условий:

Порядок вхождения символов должен быть сохранён.
Одинаковым символам первой строки должны соответствовать
одинаковые символы второй строки. Разным символам —– разные.
Например, если строка s = «abacaba», то ей будет равна строка t = «xhxixhx»,
так как все вхождения «a» заменены на «x», «b» –— на «h», а «c» –— на «i».
Если же первая строка s=«abc», а вторая t=«aaa», то строки уже не будут равны,
так как разные буквы первой строки соответствуют одинаковым буквам второй.
"""

def input_data():
    return input(), input()


def compare_words(word1: str, word2: str) -> bool:
    """Сравнение двух слов."""

    def compare(word1: str, word2: str) -> bool:
        """Сравнение в прямом направлении."""
        accordance = {}
        for k_char in range(len(word1)):
            char = word1[k_char]
            if char in accordance:
                if accordance[char] != word2[k_char]:
                    return False
            else:
                accordance[char] = word2[k_char]
        return True

    return (len(word1) == len(word2)
            and compare(word1, word2)
            and compare(word2, word1))


def output(res: bool):
    print('YES' if res else 'NO')


def test():
    assert compare_words('mxyskaoghi', 'qodfrgmslc') is True
    assert compare_words('abacaba', 'xhxixhx') is True
    assert compare_words('abc', 'aaa') is False
    assert compare_words('agg', 'xdd') is True
    assert compare_words('agg', 'xda') is False


def main():
    word1, word2 = input_data()
    output(compare_words(word1, word2))


if __name__ == '__main__':
    main()
