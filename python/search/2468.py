from sys import stdin
from collections import deque
input = stdin.readline

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def get_count(graph, height):
    length = len(graph)
    visited = [([False] * length) for _ in range(length)]
    count = 0
    for i in range(length):
        for j in range(length):
            if graph[i][j] > height and not visited[i][j]:
                bfs(graph, height, i, j, visited)
                count += 1
    return count


def bfs(graph, height, x, y, visited):
    queue = deque([(x, y)])
    visited[x][y] = True
    while queue:
        x, y = queue.popleft()
        for i in range(len(dx)):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < len(graph) and 0 <= ny < len(graph[0]) and graph[x][y] > height:
                if not visited[nx][ny]:
                    queue.append((nx, ny))
                    visited[nx][ny] = True


n = int(input())
graph = [list(map(int, input().split())) for i in range(n)]
count = 0
for i in range(101):
    count = max(count, get_count(graph, i))
print(count)
