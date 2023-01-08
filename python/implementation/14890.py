import sys
input = sys.stdin.readline


N, L = map(int, input().split(' '))
graph = [list(map(int, input().split(' '))) for _ in range(N)]
answer = 0


def can_modify(r, c, is_row):
    height = graph[r][c]
    if is_row:
        for i in range(L):
            if (c+i >= N) or (not graph[r][c+i] == height):
                return False
    else:
        for i in range(L):
            if( r+i >= N) or (not graph[r+i][c] == height):
                return False
    return True


for i in range(N):

    can_go = True
    count = 0
    height = graph[i][0]
    j = 0
    while j < N:
        current = graph[i][j]
        if current == height:
            j += 1
            count += 1
        elif current == height-1 and can_modify(i, j, True):
            j += L
            count = 0
            height = current
        elif current == height+1 and count >= L:
            j += 1
            count = 1
            height = current
        else:
            can_go = False
            break
    if can_go:
        answer += 1

    can_go = True
    count = 0
    height = graph[0][i]
    j = 0
    while j < N:
        current = graph[j][i]
        if current == height:
            j += 1
            count += 1
        elif current == height-1 and can_modify(j, i, False):
            j += L
            count = 0
            height = current
        elif current == height+1 and count >= L:
            j += 1
            count = 1
            height = current
        else:
            can_go = False
            break
    if can_go:
        answer += 1

print(answer)
