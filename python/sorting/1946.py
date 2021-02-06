from sys import stdin
input = stdin.readline

t = int(input())
for i in range(t):
    n = int(input())
    data = [tuple(map(int, input().split())) for _ in range(n)]
    data.sort()
    min_value = data[0][1]
    count = 1
    for i in data:
        if min_value > i[1]:
            count += 1
            min_value = i[1]
    print(count)
