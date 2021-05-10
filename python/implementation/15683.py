import sys
import copy
input = sys.stdin.readline

UP = (-1, 0)
RIGHT = (0, 1)
DOWN = (1, 0)
LEFT = (0, -1)
direction = [
    [],
    [[UP], [DOWN], [LEFT], [UP]],
    [[LEFT, RIGHT], [UP, DOWN]],
    [[UP, RIGHT], [RIGHT, DOWN], [DOWN, LEFT], [LEFT, UP]],
    [[LEFT, UP, RIGHT], [UP, RIGHT, DOWN], [RIGHT, DOWN, LEFT], [DOWN, LEFT, UP]],
    [[UP, RIGHT, DOWN, LEFT]]
]


def get_min(graph, cctv, current, empty):
    global answer
    if current == len(cctv):
        answer = min(answer, empty)
        return
    r, c = cctv[current]
    go = direction[graph[r][c]]
    for i in go:
        count = 0
        temp = copy.deepcopy(graph)
        for dr, dc in i:
            nr, nc = r, c
            while True:
                nr, nc = nr+dr, nc+dc
                if not (0 <= nr < n and 0 <= nc < m) or temp[nr][nc] == 6:
                    break
                if temp[nr][nc] == 0:
                    temp[nr][nc] = '#'
                    count += 1
        get_min(temp, cctv, current+1, empty-count)


n, m = map(int, input().split())
graph = []
cctv = []
empty = 0
for i in range(n):
    row = list(map(int, input().split()))
    graph.append(row)
    for j in range(m):
        if graph[i][j] == 0:
            empty += 1
        elif 0 < graph[i][j] < 6:
            cctv.append((i, j))
answer = 64
get_min(graph, cctv, 0, empty)
print(answer)
