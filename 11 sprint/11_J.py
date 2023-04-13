import sys


number = int(input())

factors = []
while True:
    if number % 2:
        break
    number //= 2
    factors.append(str(2))

factor = 3
while number > 1:
    if factor * factor > number:
        factors.append(f'{number}')
        break
    while True:
        if number % factor:
            break
        number //= factor
        factors.append(f'{factor}')
    factor += 2


print(' '.join(factors))
