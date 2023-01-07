import sys
input = sys.stdin.readline

inputs = input().split(' ')
N = int(inputs[0])
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
dp = list(map(int, inputs[1:]))
visited = [[False] * (2*N+1) for _ in range(2*N+1)]

answer = 0
def move(count, percent, x, y):
    global answer
    if count == N:
        answer += percent * (0.01 ** N)
        return

    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]
        if visited[ny][nx]:
            continue
        visited[ny][nx] = True
        move(count+1, percent*dp[i], nx, ny)
        visited[ny][nx] = False

visited[N][N] = True
move(0, 1, N, N)
print(answer)
