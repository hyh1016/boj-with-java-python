import sys
from collections import deque
input = sys.stdin.readline


def bfs(graph, start, target):
    visited = [False]*(n+1)
    q = deque([(start, 0)])
    visited[start] = True
    while q:
        v, cnt = q.popleft()
        if v == target:
            return cnt
        for i in range(1, n+1):
            if graph[v][i] and not visited[i]:
                q.append((i, cnt+1))
                visited[i] = True
    return -1


n = int(input())
a, b = map(int, input().split())
graph = [[False]*(n+1) for _ in range(n+1)]
for i in range(int(input())):
    x, y = map(int, input().split())
    graph[x][y] = graph[y][x] = True
print(bfs(graph, a, b))
