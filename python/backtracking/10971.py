import sys
input = sys.stdin.readline
sys.setrecursionlimit(int(1e8))
INF = 1000000 * 100


def get_distance(i, current, total, visited):
    global min_distance
    if i == n:
        if graph[current][0] != 0:
            total += graph[current][0]
            min_distance = min(min_distance, total)
        return
    for next in range(1, n):
        if visited[next] or graph[current][next] == 0:
            continue
        visited[next] = True
        get_distance(i+1, next, total+graph[current][next], visited)
        visited[next] = False


n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
min_distance = INF
visited = [False]*n
visited[0] = True
get_distance(1, 0, 0, visited)
print(min_distance)
