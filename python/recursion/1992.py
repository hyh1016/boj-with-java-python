import sys
input = sys.stdin.readline


def make_tree(size, r, c):
    if size == 1:
        return data[r][c]
    start = data[r][c]
    for i in range(size):
        for j in range(size):
            if data[r + i][c + j] != start:
                new_size = int(size/2)
                return '(' + make_tree(new_size, r, c) + \
                    make_tree(new_size, r, c + new_size) + \
                    make_tree(new_size, r + new_size, c) + \
                    make_tree(new_size, r + new_size, c + new_size) + ')'
    return start


n = int(input())
data = [list(input().rstrip()) for _ in range(n)]
print(make_tree(n, 0, 0))
