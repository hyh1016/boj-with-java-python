from sys import stdin
input = stdin.readline

t = int(input())
for i in range(t):
    n = int(input())
    values = sorted(list(map(int, input().split())))
    max_value = 0
    for i in range(n - 2):
        max_value = max(max_value, values[i + 2] - values[i])
    print(max_value)
