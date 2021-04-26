import sys
from collections import deque
input = sys.stdin.readline

dx = [0, 0, -1, 1, 0, 0]
dy = [1, -1, 0, 0, 0, 0]
dz = [0, 0, 0, 0, 1, -1]


def get_day(graph, done, yet):
    if not done:
        return -1
    if not yet:
        return 0
    q = deque(done)
    h, r, c = 0, 0, 0
    while q:
        h, r, c = q.popleft()
        for i in range(len(dx)):
            nh, nr, nc = h + dz[i], r + dy[i], c + dx[i]
            if (nh, nr, nc) in yet:
                graph[nh][nr][nc] = graph[h][r][c] + 1
                yet.remove((nh, nr, nc))
                q.append((nh, nr, nc))
    if yet:
        return -1
    return graph[h][r][c] - 1


m, n, h = map(int, input().split())
graph = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]
done = []
yet = set()
for i in range(h):
    for j in range(n):
        for k in range(m):
            if graph[i][j][k] == 1:
                done.append((i, j, k))
            if graph[i][j][k] == 0:
                yet.add((i, j, k))
print(get_day(graph, done, yet))
