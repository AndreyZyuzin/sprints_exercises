import sys

line = sys.stdin.readline()

simbols = [char.lower() for char in line if char.isalpha()]

def isPolindrom(simbols: list) -> bool:
    half_length = len(simbols) // 2
    for i_char in range(half_length):
        if simbols[i_char] != simbols[-i_char - 1]:
            return False
    return True

print(isPolindrom(simbols))
