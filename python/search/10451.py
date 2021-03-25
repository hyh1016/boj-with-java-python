import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)


def dfs(graph, v, visited):
    visited[v] = True
    if not visited[graph[v]]:
        dfs(graph, graph[v], visited)


for i in range(int(input())):
    n = int(input())
    graph = [0] + list(map(int, input().split()))
    visited = [False] * (n+1)
    count = 0
    for v in range(1, n+1):
        if not visited[v]:
            dfs(graph, v, visited)
            count += 1
    print(count)
