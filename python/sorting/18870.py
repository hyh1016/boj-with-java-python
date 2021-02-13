from sys import stdin
input = stdin.readline

n = int(input())
data = list(map(int, input().split()))
level = dict(zip(sorted(set(data)), list(range(len(set(data))))))
for i in data:
    print(level[i], end=" ")
