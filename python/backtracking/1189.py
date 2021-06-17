import sys
input = sys.stdin.readline

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]


def backtracking(graph, y, x, count, visited, answer):
    if count > k:
        return
    if y == 0 and x == c-1:
        answer[count] += 1
        return
    for i in range(4):
        ny, nx = y+dy[i], x+dx[i]
        if 0 <= ny < r and 0 <= nx < c and graph[ny][nx] != 'T' and not visited[ny][nx]:
            visited[ny][nx] = True
            backtracking(graph, ny, nx, count+1, visited, answer)
            visited[ny][nx] = False


r, c, k = map(int, input().split())
graph = [list(input().rstrip()) for _ in range(r)]
visited = [[False]*c for _ in range(r)]
visited[r-1][0] = True
answer = [0]*(k+1)
backtracking(graph, r-1, 0, 1, visited, answer)
print(answer[k])
