"""Задача E спринта 13 hash.

Подстроки.
На вход подается строка. Нужно определить длину наибольшей подстроки,
которая не содержит повторяющиеся символы.
"""
def input_data():
    return input()


def get_varied_substring(word: str) -> int:
    """Получить самую длинную подстраку с различными символами."""
    tmp = set()
    result = 0
    begin = end = 0
    while end < len(word):
        char = word[end]
        if char not in tmp:
            tmp.add(char)
            end += 1
            if end - begin > result:
                result = end - begin
            continue
        while True:
            if word[begin] == char:
                begin += 1
                end += 1
                break
            tmp.remove(word[begin])
            begin += 1
    return result






def test():
    s = 'abcabcbb'
    s = 'abcadebcbb'
    print(get_varied_substring(s))
    assert get_varied_substring('abcabcbb') == 3
    assert get_varied_substring('abcadebcbb') == 5
    assert get_varied_substring('bbbbb') == 1




def main():
    a, m, s, arr = input_data()
    word = String2(s, a, m)
    for begin, end in arr:
        # print(begin, end, hash(s[begin-1:end], a, m), end=' ')
        print(word._hash_sub(begin, end))


if __name__ == '__main__':
    test()
