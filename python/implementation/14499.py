import sys
input = sys.stdin.readline


def move(dice, command):
    if command == 1:
        dice[3], dice[6] = dice[6], dice[3]
        dice[1], dice[3] = dice[3], dice[1]
        dice[4], dice[1] = dice[1], dice[4]
    if command == 2:
        dice[4], dice[6] = dice[6], dice[4]
        dice[1], dice[4] = dice[4], dice[1]
        dice[3], dice[1] = dice[1], dice[3]
    if command == 3:
        dice[1], dice[2] = dice[2], dice[1]
        dice[5], dice[1] = dice[1], dice[5]
        dice[6], dice[5] = dice[5], dice[6]
    if command == 4:
        dice[5], dice[6] = dice[6], dice[5]
        dice[1], dice[5] = dice[5], dice[1]
        dice[2], dice[1] = dice[1], dice[2]


dx = [0, 0, 0, -1, 1]
dy = [0, 1, -1, 0, 0]
dice = [0] * 7
n, m, x, y, k = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
commands = list(map(int, input().split()))
for i in commands:
    nx, ny = x+dx[i], y+dy[i]
    if 0 <= nx < n and 0 <= ny < m:
        x, y = nx, ny
        move(dice, i)
        if graph[x][y] == 0:
            graph[x][y] = dice[6]
        else:
            dice[6] = graph[x][y]
            graph[x][y] = 0
        print(dice[1])
