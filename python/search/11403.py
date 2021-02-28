# dfs

import sys
input = sys.stdin.readline


def dfs(graph, r, c, visited):
    visited[r][c] = 1
    for i in range(n):
        if graph[c][i] == 1 and not visited[r][i]:
            dfs(graph, r, i, visited)


n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1 and not visited[i][j]:
            dfs(graph, i, j, visited)
for i in visited:
    for j in i:
        print(j, end=' ')
    print()
