import sys
import heapq

input = sys.stdin.readline
INF = int(1e7)


def dijkstra(graph, start, shortest):
    shortest[start] = 0
    q = []
    heapq.heappush(q, (shortest[start], start))
    while q:
        cost, index = heapq.heappop(q)
        if shortest[index] < cost:
            continue
        for i in graph[index]:
            new_cost = cost + i[1]
            if shortest[i[0]] > new_cost:
                shortest[i[0]] = new_cost
                heapq.heappush(q, (shortest[i[0]], i[0]))


N, M, X = map(int, input().split())
go = [[] for _ in range(N + 1)]
go_shortest = [INF] * (N + 1)
back = [[] for _ in range(N + 1)]
back_shortest = [INF] * (N + 1)
for i in range(M):
    start, end, time = map(int, input().split())
    go[end].append((start, time))
    back[start].append((end, time))
dijkstra(go, X, go_shortest)
dijkstra(back, X, back_shortest)
print(max([go_shortest[i] + back_shortest[i] for i in range(1, N + 1)]))
