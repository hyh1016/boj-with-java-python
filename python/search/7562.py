import sys
from collections import deque
input = sys.stdin.readline

dy = [1, 1, -1, -1, 2, 2, -2, -2]
dx = [2, -2, 2, -2, 1, -1, 1, -1]


def bfs(graph, y, x, target_y, target_x):
    q = deque([(y, x, 0)])
    graph[y][x] = 1
    while q:
        y, x, count = q.popleft()
        if y == target_y and x == target_x:
            return count
        for i in range(len(dy)):
            ny, nx = y+dy[i], x+dx[i]
            if 0 <= ny < len(graph) and 0 <= nx < len(graph) and graph[ny][nx] == 0:
                graph[ny][nx] = 1
                q.append((ny, nx, count+1))


t = int(input())
for i in range(t):
    i = int(input())
    graph = [[0]*i for _ in range(i)]
    start_y, start_x = map(int, input().split())
    target_y, target_x = map(int, input().split())
    print(bfs(graph, start_y, start_x, target_y, target_x))
