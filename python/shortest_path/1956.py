import sys
input = sys.stdin.readline
INF = sys.maxsize

v, e = map(int, input().split())
graph = [[INF]*(v+1) for _ in range(v+1)]
for i in range(e):
    a, b, c = map(int, input().split())
    graph[a][b] = c
for m in range(1, v+1):
    for i in range(1, v+1):
        for j in range(1, v+1):
            graph[i][j] = min(graph[i][j], graph[i][m]+graph[m][j])
shortest = min([graph[i][i] for i in range(1, v+1)])
print(shortest if shortest != INF else -1)
