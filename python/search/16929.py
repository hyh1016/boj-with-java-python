import sys


sys.setrecursionlimit(3000)
input = sys.stdin.readline
has_cycle = False


def find_cycle(graph, pr, pc, r, c, visited):
    global has_cycle
    if has_cycle:
        return
    
    visited[r][c] = True
    color = graph[r][c]
    for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        nr, nc = r+dr, c+dc
        if nr == pr and nc == pc:
            continue
        if 0 <= nr < len(graph) and 0 <= nc < len(graph[0]):
            if graph[nr][nc] == color:
                if visited[nr][nc]:
                    has_cycle = True
                    return
                find_cycle(graph, r, c, nr, nc, visited)


n, m = map(int, input().split())
graph = [list(input().rstrip()) for _ in range(n)]

visited = [[False]*m for _ in range(n)]
for i in range(n):
    for j in range(m):
        if visited[i][j]:
            continue
        find_cycle(graph, -1, -1, i, j, visited)
        if has_cycle:
            break
    if has_cycle:
        break
print('Yes' if has_cycle else 'No')
