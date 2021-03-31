import sys
input = sys.stdin.readline

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]


def move():
    global r, c, d
    for _ in range(4):
        d = 3 if d == 0 else d-1
        nr, nc = r+dr[d], c+dc[d]
        if graph[nr][nc] == 0:
            r, c = nr, nc
            return True
    nr, nc = r-dr[d], c-dc[d]
    if graph[nr][nc] == 2:
        r, c = nr, nc
        return True
    return False


def clean():
    global count
    graph[r][c] = 2
    count += 1


n, m = map(int, input().split())
r, c, d = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
count = 0
while True:
    if graph[r][c] == 0:
        clean()
    if not move():
        break
print(count)
