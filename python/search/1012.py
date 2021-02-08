import sys
sys.setrecursionlimit(10000)  # 재귀 한도 설정

input = sys.stdin.readline


dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def dfs(graph, y, x):
    graph[y][x] = 0
    for i in range(len(dx)):
        ny, nx = y + dy[i], x + dx[i]
        if 0 <= ny < len(graph) and 0 <= nx < len(graph[0]) and graph[ny][nx] == 1:
            dfs(graph, ny, nx)


t = int(input())
for i in range(t):
    m, n, k = map(int, input().split())
    graph = [[0] * m for _ in range(n)]
    for j in range(k):
        x, y = map(int, input().split())
        graph[y][x] = 1
    count = 0
    for row in range(n):
        for column in range(m):
            if graph[row][column] == 1:
                dfs(graph, row, column)
                count += 1
    print(count)
