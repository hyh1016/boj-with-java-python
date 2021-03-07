import sys
input = sys.stdin.readline
sys.setrecursionlimit(15000)

dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]


def dfs(graph, y, x, visited):
    visited[y][x] = True
    for i in range(len(dx)):
        ny, nx = y + dy[i], x + dx[i]
        if 0 <= ny < n and 0 <= nx < n and not visited[ny][nx]:
            if graph[y][x] == graph[ny][nx]:
                dfs(graph, ny, nx, visited)


n = int(input())
graph1 = []
graph2 = []
for i in range(n):
    row = input().rstrip()
    graph1.append(list(row))
    graph2.append(list(row.replace('G', 'R')))
visited1 = [[False] * n for _ in range(n)]
visited2 = [[False] * n for _ in range(n)]
count1, count2 = 0, 0
for i in range(n):
    for j in range(n):
        if not visited1[i][j]:
            count1 += 1
            dfs(graph1, i, j, visited1)
        if not visited2[i][j]:
            count2 += 1
            dfs(graph2, i, j, visited2)
print(count1, count2)
