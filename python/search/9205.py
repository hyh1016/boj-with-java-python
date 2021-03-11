import sys
from collections import deque
input = sys.stdin.readline


def is_happy(store, start, target):
    visited = [False] * n
    q = deque([start])
    while q:
        x, y = q.popleft()
        if abs(target[0] - x) + abs(target[1] - y) <= 1000:
            return True
        for idx, val in enumerate(store):
            if not visited[idx] and abs(val[0] - x) + abs(val[1] - y) <= 1000:
                visited[idx] = True
                q.append(val)
    return False


t = int(input())
for i in range(t):
    n = int(input())
    start = tuple(map(int, input().split()))
    store = [tuple(map(int, input().split())) for _ in range(n)]
    target = tuple(map(int, input().split()))
    print('happy' if is_happy(store, start, target) else 'sad')
