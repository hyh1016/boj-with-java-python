import sys
input = sys.stdin.readline
INF = int(1e9)


def floyd(graph):
    for i in range(1, len(graph)):
        graph[i][i] = 0
    for k in range(1, len(graph)):
        for i in range(1, len(graph)):
            for j in range(1, len(graph)):
                graph[i][j] = min(graph[i][j], graph[i][k]+graph[k][j])


n = int(input())
m = int(input())
graph = [[INF]*(n+1) for _ in range(n+1)]
for i in range(m):
    a, b, c = map(int, input().split())
    graph[a][b] = min(graph[a][b], c)
floyd(graph)
for i in range(1, n+1):
    for j in range(1, n+1):
        print(graph[i][j] if graph[i][j] != INF else 0, end=' ')
    print()
