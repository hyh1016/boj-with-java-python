from sys import stdin
from collections import deque
input = stdin.readline

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def bfs(graph, y, x):
    queue = deque([(y, x)])
    graph[y][x] = 1
    area = 1
    while queue:
        y, x = queue.popleft()
        for i in range(len(dx)):
            ny, nx = y + dy[i], x + dx[i]
            if 0 <= ny < len(graph) and 0 <= nx < len(graph[0]) and graph[ny][nx] == 0:
                queue.append((ny, nx))
                graph[ny][nx] = 1
                area += 1
    return area


m, n, k = map(int, input().split())
graph = [[0] * n for i in range(m)]
for i in range(k):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(y1, y2):
        for j in range(x1, x2):
            graph[i][j] = 1

count = 0
area = []
for i in range(m):
    for j in range(n):
        if graph[i][j] == 0:
            area.append(bfs(graph, i, j))
            count += 1
print(count)
for i in sorted(area):
    print(i, end=' ')
