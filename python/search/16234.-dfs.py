import sys
input = sys.stdin.readline
sys.setrecursionlimit(int(1e8))


def move(graph, r, c, union):
    visited[r][c] = True
    for i in range(4):
        nr, nc = r+dr[i], c+dc[i]
        if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc]:
            if L <= abs(graph[r][c] - graph[nr][nc]) <= R:
                union.append((nr, nc))
                move(graph, nr, nc, union)


dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
N, L, R = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
count = 0

while True:
    visited = [[False]*N for _ in range(N)]
    have_union = False
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                union = [(i, j)]
                move(graph, i, j, union)
                if len(union) == 1:
                    continue
                have_union = True
                new_value = int(sum([graph[r][c]
                                     for r, c in union]) / len(union))
                for r, c in union:
                    graph[r][c] = new_value
    if not have_union:
        break
    count += 1
print(count)
