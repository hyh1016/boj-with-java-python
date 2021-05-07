import sys
from collections import deque
input = sys.stdin.readline


dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]


def start_game(board, turn_data):
    time = 0
    r, c = 1, 1
    direction = 0
    snake = deque([(r, c)])
    while True:
        time += 1
        r, c = r+dr[direction], c+dc[direction]
        if not(0 < r <= N and 0 < c <= N) or board[r][c] == 2:
            break
        snake.append((r, c))
        if board[r][c] == 0:
            tail_r, tail_c = snake.popleft()
            board[tail_r][tail_c] = 0
        board[r][c] = 2
        if turn_data and turn_data[0][0] == time:
            t, cmd = turn_data.popleft()
            direction = turn(direction, cmd)
    return time


def turn(direction, command):
    if command == 'L':
        direction = direction-1 if direction > 0 else 3
    else:
        direction = direction+1 if direction < 3 else 0
    return direction


N = int(input())
K = int(input())
board = [[0]*(N+1) for _ in range(N+1)]
for i in range(K):
    r, c = map(int, input().split())
    board[r][c] = 1
L = int(input())
turn_data = deque()
for i in range(L):
    t, cmd = input().split()
    turn_data.append((int(t), cmd))
print(start_game(board, turn_data))
