import sys
input = sys.stdin.readline
sys.setrecursionlimit(int(1e8))

d = [(0, 0), (0, 1), (1, 0), (0, 2), (2, 0), (1, 2), (2, 1), (2, 2)]


def set_star(x, y, size, pattern):
    if size == 1:
        pattern[x][y] = True
        return
    nsize = size // 3
    for dx, dy in d:
        nx, ny = x+dx*nsize, y+dy*nsize
        if 0 <= nx < n and 0 <= ny < n:
            set_star(nx, ny, nsize, pattern)


n = int(input())
pattern = [[False]*n for _ in range(n)]
set_star(0, 0, n, pattern)
for i in range(n):
    for j in range(n):
        print("*" if pattern[i][j] else " ", end="")
    print()
