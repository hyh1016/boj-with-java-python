import sys
from collections import deque
input = sys.stdin.readline


dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def move(graph, r, c, min_diff, max_diff, visited):
    total_sum = 0
    union = []
    q = deque([(r, c)])
    visited[r][c] = True
    while q:
        r, c = q.popleft()
        total_sum += graph[r][c]
        union.append((r, c))
        for i in range(4):
            nr, nc = r+dr[i], c+dc[i]
            if 0 <= nr < len(graph) and 0 <= nc < len(graph[0]) and not visited[nr][nc]:
                if min_diff <= abs(graph[r][c] - graph[nr][nc]) <= max_diff:
                    visited[nr][nc] = True
                    q.append((nr, nc))
    if len(union) == 1:
        return False
    for r, c in union:
        graph[r][c] = int(total_sum / len(union))
    return True


N, L, R = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
count = 0
while True:
    visited = [[False]*N for _ in range(N)]
    have_union = False
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                if move(graph, i, j, L, R, visited):
                    have_union = True
    if not have_union:
        break
    count += 1
print(count)
