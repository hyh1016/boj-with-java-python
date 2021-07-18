import sys
input = sys.stdin.readline


dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def diffusion():
    global room
    result = [i[::] for i in room]
    for i in range(r):
        for j in range(c):
            if room[i][j] < 5:
                continue
            value = room[i][j] // 5
            for d in range(4):
                nr, nc = i+dr[d], j+dc[d]
                if 0 <= nr < r and 0 <= nc < c and room[nr][nc] != -1:
                    result[nr][nc] += value
                    result[i][j] -= value
    room = result


def up_wind(room, up):
    global total
    total -= room[up-1][0]
    for i in range(up-1, 0, -1):
        room[i][0] = room[i-1][0]
    for i in range(c-1):
        room[0][i] = room[0][i+1]
    for i in range(up):
        room[i][c-1] = room[i+1][c-1]
    for i in range(c-1, 1, -1):
        room[up][i] = room[up][i-1]
    room[up][1] = 0


def down_wind(room, down):
    global total
    total -= room[down+1][0]
    for i in range(down+1, r-1):
        room[i][0] = room[i+1][0]
    for i in range(c-1):
        room[r-1][i] = room[r-1][i+1]
    for i in range(r-1, down, -1):
        room[i][c-1] = room[i-1][c-1]
    for i in range(c-1, 1, -1):
        room[down][i] = room[down][i-1]
    room[down][1] = 0


r, c, t = map(int, input().split())
room = []
up, down = -1, -1
total = 0

for i in range(r):
    room.append(list(map(int, input().split())))
    for j in range(c):
        if room[i][j] == -1:
            if room[i-1][j] == -1:
                up = i-1
                down = i
        else:
            total += room[i][j]

for i in range(t):
    diffusion()
    up_wind(room, up)
    down_wind(room, down)

print(total)
