import sys

_ = input()
line = sys.stdin.readline().strip().split()
another_number = int(input())

number = int(''.join(line))
sum = number + another_number


print(' '.join(str(sum)))
