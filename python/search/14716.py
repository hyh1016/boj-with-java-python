import sys
input = sys.stdin.readline
sys.setrecursionlimit(int(10e8))

dr = [1, -1, 0, 0, 1, -1, 1, -1]
dc = [0, 0, 1, -1, 1, 1, -1, -1]


def dfs(banner, r, c, visited):
    for i in range(len(dr)):
        nr, nc = r+dr[i], c+dc[i]
        if 0 <= nr < len(banner) and 0 <= nc < len(banner[0]) and banner[nr][nc] == 1 and not visited[nr][nc]:
            visited[nr][nc] = True
            dfs(banner, nr, nc, visited)


n, m = map(int, input().split())
banner = [list(map(int, input().split())) for i in range(n)]
visited = [[False]*(m) for _ in range(n)]
count = 0
for i in range(n):
    for j in range(m):
        if banner[i][j] == 1 and not visited[i][j]:
            dfs(banner, i, j, visited)
            count += 1
print(count)
