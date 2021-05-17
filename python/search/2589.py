import sys
from collections import deque
input = sys.stdin.readline
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def bfs(graph, i, j):
    visited = [[False]*m for _ in range(n)]
    visited[i][j] = True
    time = 0
    q = deque([(i, j, time)])
    while q:
        r, c, time = q.popleft()
        for i in range(4):
            nr, nc = r+dr[i], c+dc[i]
            if 0 <= nr < n and 0 <= nc < m and graph[nr][nc] == 'L' and not visited[nr][nc]:
                visited[nr][nc] = True
                q.append((nr, nc, time+1))
    return time


n, m = map(int, input().split())
graph = [list(input().rstrip()) for _ in range(n)]
answer = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == 'L':
            answer = max(answer, bfs(graph, i, j))
print(answer)
