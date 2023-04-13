import sys

line = sys.stdin.readline().strip()
a, x, b, c = map(int, line.split())

y = a*x*x + b*x + c

print(str(y))