import sys
import heapq

input = sys.stdin.readline
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

M, N = map(int, input().split())
graph = [list(map(int, list(input().rstrip()))) for _ in range(N)]
visited = [[False] * M for _ in range(N)]
q = [(0, 0, 0)]
visited[0][0] = True
while q:
    w, x, y = heapq.heappop(q)
    if x == M - 1 and y == N - 1:
        print(w)
        break
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < M and 0 <= ny < N and not visited[ny][nx]:
            visited[ny][nx] = True
            heapq.heappush(q, (w + graph[ny][nx], nx, ny))
