import sys
from collections import deque
input = sys.stdin.readline

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]


def bfs(graph, r, c):
    global total_time, start, size, count
    visited = [[False]*n for _ in range(n)]
    q = deque([(0, r, c)])
    visited[r][c] = True
    distances = []
    while q:
        time, r, c = q.popleft()
        if 0 < graph[r][c] < size:
            distances.append((time, r, c))
        for i in range(len(dy)):
            nr, nc = r+dy[i], c+dx[i]
            if 0 <= nr < n and 0 <= nc < n and not visited[nr][nc] and graph[nr][nc] <= size:
                q.append((time+1, nr, nc))
                visited[nr][nc] = True
    if not distances:
        return False
    time, r, c = sorted(distances)[0]
    graph[r][c] = 0
    total_time += time
    start = (r, c)
    count += 1
    if count == size:
        size += 1
        count = 0
    return True


n = int(input())
start = 0
graph = []
for i in range(n):
    row = list(map(int, input().split()))
    graph.append(row)
    for j in range(n):
        if row[j] == 9:
            start = (i, j)
            graph[i][j] = 0

total_time = 0
size = 2
count = 0
while True:
    if not bfs(graph, start[0], start[1]):
        break
print(total_time)
