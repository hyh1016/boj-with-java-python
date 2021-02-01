from sys import stdin

M = int(stdin.readline())
ball_position = 1
for i in range(M):
    X, Y = list(map(int, stdin.readline().split()))
    if ball_position == X:
        ball_position = Y
    elif ball_position == Y:
        ball_position = X
print(ball_position)
