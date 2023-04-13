import sys

number1 = input()
number2 = input()
len1 = len(number1)
len2 = len(number2)
number1 = number1.zfill(len2)
number2 = number2.zfill(len1)

result_array = []
k_symbol = len(number1)
next_symbol = 0
while k_symbol:
    k_symbol -= 1
    if number1[k_symbol] == '1':
        next_symbol += 1
    if number2[k_symbol] == '1':
        next_symbol += 1
    next_symbol, symbol = divmod(next_symbol, 2)
    result_array.append(str(symbol))
if next_symbol:
    result_array.append('1')

print(''.join(reversed(result_array)))
