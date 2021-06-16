import sys
input = sys.stdin.readline
MAX = 100001

for i in range(int(input())):
    n = int(input())
    cafe = [[] for _ in range(MAX+1)]
    answer = []
    for _ in range(n):
        x, y = map(int, input().split())
        cafe[x].append(y)
    prev_y = 0
    for i in range(MAX+1):
        if not cafe[i]:
            continue
        cafe[i].sort(key=lambda y: abs(y-prev_y))
        prev_y = cafe[i][-1]
        answer += [(i, j) for j in cafe[i]]

    numbers = list(map(int, input().split()))
    for i in range(1, len(numbers)):
        print(*answer[numbers[i]-1])
