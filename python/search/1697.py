from sys import stdin
from collections import deque


def bfs(n, k, time, visited):
    queue = deque([(n, time)])
    visited[n] = True
    while queue:
        n, time = queue.popleft()
        if n == k:
            return time
        for i in [n + 1, n - 1, n * 2]:
            if 0 <= i < len(visited) and not visited[i]:
                queue.append((i, time + 1))
                visited[i] = True


MAX = 100000
n, k = map(int, stdin.readline().split())
time = 0
visited = [False] * (MAX + 1)
result = bfs(n, k, time, visited)
print(result)
