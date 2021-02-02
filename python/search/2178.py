from sys import stdin
from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def bfs(graph, row, column):
    queue = deque([(row, column)])
    while queue:
        row, column = queue.popleft()
        for i in range(len(dx)):
            nx, ny = row + dx[i], column + dy[i]
            if 0 <= nx < len(graph) and 0 <= ny < len(graph[0]) and graph[nx][ny] == 1:
                graph[nx][ny] = graph[row][column] + 1
                if nx == (len(graph) - 1) and ny == (len(graph[0]) - 1):
                    return graph[nx][ny]
                queue.append((nx, ny))


n, m = map(int, stdin.readline().split())
graph = [list(map(int, list(stdin.readline().rstrip()))) for i in range(n)]
print(bfs(graph, 0, 0))
