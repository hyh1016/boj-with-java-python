import sys
input = sys.stdin.readline
sys.setrecursionlimit(int(1e8))

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def check_deleted(graph, r, c, visited, deleted):
    for i in range(4):
        nr, nc = r+dr[i], c+dc[i]
        if not (0 <= nr < len(graph) and 0 <= nc < len(graph[0])) or visited[nr][nc]:
            continue
        visited[nr][nc] = True
        if graph[nr][nc] == 0:
            check_deleted(graph, nr, nc, visited, deleted)
        else:
            deleted.append((nr, nc))


n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
count = 0
prev = 0
while True:
    visited = [[False]*m for _ in range(n)]
    deleted = []
    visited[0][0] = True
    check_deleted(graph, 0, 0, visited, deleted)
    if not deleted:
        break
    for r, c in deleted:
        graph[r][c] = 0
    count += 1
    prev = len(deleted)
print(count)
print(prev)
