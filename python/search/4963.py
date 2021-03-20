import sys
input = sys.stdin.readline
sys.setrecursionlimit(15000)

dy = [-1, 1, 0, 0, -1, 1, -1, 1]
dx = [0, 0, -1, 1, -1, 1, 1, -1]


def dfs(graph, r, c):
    graph[r][c] = 0
    for i in range(len(dy)):
        nr, nc = r+dy[i], c+dx[i]
        if 0 <= nr < n and 0 <= nc < m and graph[nr][nc] == 1:
            dfs(graph, nr, nc)


while True:
    m, n = map(int, input().split())
    if n == 0 and m == 0:
        break
    graph = [list(map(int, input().split())) for _ in range(n)]
    count = 0
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1:
                count += 1
                dfs(graph, i, j)
    print(count)
