from collections import Counter

symbols1 = input()
symbols2 = input()

counter_symbols = Counter(symbols1 + symbols2)
for key, value in counter_symbols.items():
    if value % 2:
        result = key
        break

print(result)
