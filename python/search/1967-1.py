import sys
input = sys.stdin.readline
sys.setrecursionlimit(15000)


def dfs(graph, v, w, visited, total_sum):
    global index, wsum
    visited[v] = True
    isLeaf = True
    for i in graph[v]:
        if not visited[i[0]]:
            isLeaf = False
            dfs(graph, i[0], i[1], visited, total_sum+w)
    if isLeaf and total_sum+w > wsum:
        index = v
        wsum = total_sum+w


n = int(input())
graph = [[] for _ in range(n+1)]
for i in range(n-1):
    p, c, w = map(int, input().split())
    graph[p].append((c, w))
    graph[c].append((p, w))
index = 0
wsum = 0
dfs(graph, 1, 0, [False]*(n+1), 0)
dfs(graph, index, 0, [False]*(n+1), 0)
print(wsum)
