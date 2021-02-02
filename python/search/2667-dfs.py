from sys import stdin

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]


def dfs(graph, row, column):
    graph[row][column] = '0'
    home = 1
    for i in range(len(dx)):
        nx, ny = row + dx[i], column + dy[i]
        if 0 <= nx < len(graph[0]) and 0 <= ny < len(graph[0]) and graph[nx][ny] == '1':
            home += dfs(graph, nx, ny)
    return home


n = int(stdin.readline())
graph = [list(stdin.readline().rstrip()) for i in range(n)]
count_group = 0
count_home = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == '1':
            count_home.append(dfs(graph, i, j))
            count_group += 1
print(count_group)
for i in sorted(count_home):
    print(i)
