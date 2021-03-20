import sys
input = sys.stdin.readline

n = int(input())
key = list(map(int, input().split()))
line = []
for i in range(n, 0, -1):
    line.insert(key[i-1], i)
print(' '.join(list(map(str, line))))
