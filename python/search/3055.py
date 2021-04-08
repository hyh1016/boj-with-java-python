import sys
from collections import deque
input = sys.stdin.readline

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def bfs(graph, water, start):
    q = deque([start])
    for i in water:
        q.append(i)
    while q:
        kind, r, c, count = q.popleft()
        if graph[r][c] != kind:
            continue
        for i in range(len(dr)):
            nr, nc = r+dr[i], c+dc[i]
            if 0 <= nr < len(graph) and 0 <= nc < len(graph[0]):
                if kind == 'S' and graph[nr][nc] == 'D':
                    return count+1
                if (graph[nr][nc] == '.') or (kind == '*' and graph[nr][nc] == 'S'):
                    graph[nr][nc] = kind
                    q.append((kind, nr, nc, count+1))
    return "KAKTUS"


r, c = map(int, input().split())
graph = []
water = []
start = 0
for i in range(r):
    row = list(input().rstrip())
    graph.append(row)
    for j in range(c):
        if row[j] == '*':
            water.append(('*', i, j, 0))
        if row[j] == 'S':
            start = ('S', i, j, 0)

print(bfs(graph, water, start))
