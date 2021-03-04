import sys
input = sys.stdin.readline


def get_paper_number(graph, size, r, c):
    global white, blue
    first = graph[r][c]
    for i in range(size):
        for j in range(size):
            if graph[r+i][c+j] != first:
                nsize = int(size/2)
                get_paper_number(graph, nsize, r, c)
                get_paper_number(graph, nsize, r, c+nsize)
                get_paper_number(graph, nsize, r+nsize, c)
                get_paper_number(graph, nsize, r+nsize, c+nsize)
                return
    if first == 0:
        white += 1
    else:
        blue += 1


white, blue = 0, 0
n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
get_paper_number(graph, n, 0, 0)
print(white)
print(blue)
