import sys
input = sys.stdin.readline
sys.setrecursionlimit(int(1e8))

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def get_min_value(maze, r, c, cost):
    for i in range(4):
        nr, nc = r+dr[i], c+dc[i]
        if nr < 0 or nr >= n or nc < 0 or nc >= n:
            continue
        next = cost[r][c] + (0 if maze[nr][nc] == 1 else 1)
        if cost[nr][nc] == -1 or next < cost[nr][nc]:
            cost[nr][nc] = next
            get_min_value(maze, nr, nc, cost)


n = int(input())
maze = [list(map(int, list(input().rstrip()))) for _ in range(n)]
cost = [[-1]*n for _ in range(n)]
cost[0][0] = 0
get_min_value(maze, 0, 0, cost)
print(cost[-1][-1])
