import sys
from collections import deque
input = sys.stdin.readline

dx = [0, 0, -1, 1, 0, 0]
dy = [1, -1, 0, 0, 0, 0]
dz = [0, 0, 0, 0, 1, -1]


def bfs(q, graph):
    while q:
        h, r, c = q.popleft()
        for i in range(len(dx)):
            nh, nr, nc = h + dz[i], r + dy[i], c + dx[i]
            if 0 <= nh < len(graph) and 0 <= nr < len(graph[0]) and 0 <= nc < len(graph[0][0]):
                if graph[nh][nr][nc] == 0:
                    graph[nh][nr][nc] = graph[h][r][c] + 1
                    q.append((nh, nr, nc))
    return graph[h][r][c]


m, n, h = map(int, input().split())
graph = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]
q = deque()
for i in range(h):
    for j in range(n):
        for k in range(m):
            if graph[i][j][k] == 1:
                q.append((i, j, k))
day = bfs(q, graph) - 1 if q else -1

have_zero = False
for i in range(h):
    for j in range(n):
        if 0 in graph[i][j]:
            have_zero = True
            break
    if have_zero:
        break
if have_zero:
    print(-1)
else:
    print(day)
