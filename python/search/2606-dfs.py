from sys import stdin


def dfs(graph, v, visited):
    visited[v] = True
    count = 1
    for i in range(len(graph[0])):
        if graph[v][i] == 1 and not visited[i]:
            count += dfs(graph, i, visited)
    return count


vertex = int(stdin.readline())
edge = int(stdin.readline())
graph = [[0] * (vertex + 1) for i in range(vertex + 1)]
visited = [False] * (vertex + 1)
for i in range(edge):
    v1, v2 = map(int, stdin.readline().split())
    graph[v1][v2] = graph[v2][v1] = 1
print(dfs(graph, 1, visited) - 1)
