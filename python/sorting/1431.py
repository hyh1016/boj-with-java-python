from sys import stdin
input = stdin.readline


def get_sum(x):
    x_sum = sum([int(i) for i in x if ord('0') <= ord(i) <= ord('9')])
    return x_sum


n = int(input())
data = [input().rstrip() for i in range(n)]
data.sort()
data.sort(key=get_sum)
data.sort(key=len)
for i in data:
    print(i)
