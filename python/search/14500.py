import sys
input = sys.stdin.readline

dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]


def dfs(l, r, c, total, visited):
    global result
    if l == 4:
        result = max(result, total)
        return
    for i in range(len(dy)):
        nr, nc = r+dy[i], c+dx[i]
        if 0 <= nr < n and 0 <= nc < m and not visited[nr][nc]:
            visited[nr][nc] = True
            dfs(l+1, nr, nc, total+graph[nr][nc], visited)
            visited[nr][nc] = False


def dfs2(r, c):
    global result
    for i in range(len(dy)):
        total = graph[r][c]
        for j in range(len(dy)):
            if j == i:
                continue
            nr, nc = r+dy[j], c+dx[j]
            if 0 <= nr < n and 0 <= nc < m:
                total += graph[nr][nc]
            else:
                break
        result = max(result, total)


n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[False]*m for _ in range(n)]
result = 0

for i in range(n):
    for j in range(m):
        visited[i][j] = True
        dfs(1, i, j, graph[i][j], visited)
        dfs2(i, j)
        visited[i][j] = False
print(result)
