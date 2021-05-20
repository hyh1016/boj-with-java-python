import sys
input = sys.stdin.readline
sys.setrecursionlimit(int(1e8))


def dfs(graph, v, visited):
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)


n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
answer = 0
visited = [[False]*(n+1) for _ in range(n+1)]
for i in range(1, n+1):
    dfs(graph, i, visited[i])
for i in range(1, n+1):
    count = 0
    for j in range(1, n+1):
        if visited[i][j] or visited[j][i]:
            count += 1
    if count == n:
        answer += 1
print(answer)
