import sys
from itertools import combinations
from collections import deque
input = sys.stdin.readline


dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]


def bfs():
    visited = [[False]*m for _ in range(n)]
    count = len(empty)-3
    q = deque(start_list)
    while q:
        r, c = q.popleft()
        for i in range(len(dy)):
            nr, nc = r+dy[i], c+dx[i]
            if 0 <= nr < n and 0 <= nc < m and graph[nr][nc] == 0 and not visited[nr][nc]:
                visited[nr][nc] = True
                count -= 1
                q.append((nr, nc))
    return count


n, m = map(int, input().split())
graph = [[0]*m for _ in range(n)]
empty = []
start_list = []
for i in range(n):
    row = list(map(int, input().split()))
    for j in range(m):
        graph[i][j] = row[j]
        if row[j] == 0:
            empty.append((i, j))
        elif row[j] == 2:
            start_list.append((i, j))

candidate = list(combinations(empty, 3))
result = 0
for i in candidate:
    c1, c2, c3 = i
    graph[c1[0]][c1[1]] = graph[c2[0]][c2[1]] = graph[c3[0]][c3[1]] = 1
    result = max(result, bfs())
    graph[c1[0]][c1[1]] = graph[c2[0]][c2[1]] = graph[c3[0]][c3[1]] = 0
print(result)
