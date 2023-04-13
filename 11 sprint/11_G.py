import sys

number10 = int(input())

symbols2 = []
while True:
    number10, rest = divmod(number10, 2)
    symbols2.append(str(rest))
    if not number10:
        break


print(''.join(reversed(symbols2)))
