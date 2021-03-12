import sys
input = sys.stdin.readline


def count_paper(graph, size, r, c):
    global count
    if size == 1:
        count[graph[r][c] + 1] += 1
        return
    for i in range(size):
        for j in range(size):
            if graph[r][c] != graph[r+i][c+j]:
                nsize = size // 3
                count_paper(graph, nsize, r, c)
                for a in [nsize, nsize*2]:
                    for b in [(r, c+a), (r+a, c), (r+a, c+a)]:
                        count_paper(graph, nsize, b[0], b[1])
                count_paper(graph, nsize, r+nsize, c+2*nsize)
                count_paper(graph, nsize, r+2*nsize, c+nsize)
                return
    count[graph[r][c] + 1] += 1


n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
count = [0] * 3
count_paper(graph, n, 0, 0)
for i in count:
    print(i)
