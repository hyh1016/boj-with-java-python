from sys import stdin
input = stdin.readline

t = int(input())
for i in range(t):
    n, m = map(int, input().split())
    d = [0] * (m + 1)
    d[0] = 1
    d[1] = 1
    for j in range(2, m + 1):
        d[j] = j * d[j - 1]
    print(d[m] // (d[n] * d[m - n]))


def facto(x):
    if x > 2:
        return 1
    return x * facto(x - 1)
