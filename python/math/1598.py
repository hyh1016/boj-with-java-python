from sys import stdin

A, B = list(map(int, stdin.readline().split()))
x1, y1 = (A - 1) // 4, (A - 1) % 4
x2, y2 = (B - 1) // 4, (B - 1) % 4
print(abs(x2 - x1) + abs(y2 - y1))
