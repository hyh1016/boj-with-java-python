import sys
import heapq
input = sys.stdin.readline

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def dijkstra(maze):
    visited = [[False]*n for _ in range(n)]
    visited[0][0] = True
    q = [(0, 0, 0)]
    while q:
        w, r, c = heapq.heappop(q)
        if r == n-1 and c == n-1:
            return w
        for i in range(4):
            nr, nc = r+dr[i], c+dc[i]
            if 0 <= nr < n and 0 <= nc < n and not visited[nr][nc]:
                visited[nr][nc] = True
                next_w = w + (0 if maze[nr][nc] == 1 else 1)
                heapq.heappush(q, (next_w, nr, nc))


n = int(input())
maze = [list(map(int, list(input().rstrip()))) for _ in range(n)]
print(dijkstra(maze))
