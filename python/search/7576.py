from sys import stdin
from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def bfs(graph, queue):
    while queue:
        row, column = queue.popleft()
        for i in range(len(dx)):
            nx, ny = row + dx[i], column + dy[i]
            if 0 <= nx < len(graph) and 0 <= ny < len(graph[0]) and graph[nx][ny] == 0:
                graph[nx][ny] = graph[row][column] + 1
                queue.append((nx, ny))
    return graph[row][column]  # 마지막으로 꺼낸 위치 (반드시 depth가 최대)


m, n = map(int, stdin.readline().split())
graph = [list(map(int, stdin.readline().split())) for i in range(n)]
queue = deque()
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            queue.append((i, j))
max_day = bfs(graph, queue)
for i in graph:
    if i.count(0) > 0:
        max_day = 0
        break
if max_day == 1:
    print(0)
else:
    print(max_day - 1)
