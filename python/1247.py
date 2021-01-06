from sys import stdin

answer = []
for i in range(3):
    s = sum([int(stdin.readline()) for i in range(int(stdin.readline()))])
    print('+' if s > 0 else '-' if s < 0 else '0')
