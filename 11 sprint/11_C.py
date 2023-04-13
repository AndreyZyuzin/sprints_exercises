import sys

width = int(input())
height = int(input())
array2d = []
for _ in range(width):
    line = sys.stdin.readline().rstrip()
    row = list(map(int, line.split()))
    array2d.append(row)
coordinate_y = int(input())
coordinate_x = int(input())

nears = []
tmp = coordinate_x - 1
if tmp >= 0:
    nears.append(array2d[coordinate_y][tmp])

tmp = coordinate_x + 1
if tmp < height:
    nears.append(array2d[coordinate_y][tmp])

tmp = coordinate_y - 1
if tmp >= 0:
    nears.append(array2d[tmp][coordinate_x])

tmp = coordinate_y + 1
if tmp < width:
    nears.append(array2d[tmp][coordinate_x])

nears.sort()

print(' '.join(list(map(str, nears))))
