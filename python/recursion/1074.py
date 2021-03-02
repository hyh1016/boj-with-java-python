import sys
input = sys.stdin.readline


def get_order(size, row, column):
    global count
    if row == r and column == c:
        print(count)
        return
    next_size = int(size/2)
    if r-row < next_size and c-column < next_size:
        get_order(next_size, row, column)
    elif r-row < next_size and c-column >= next_size:
        count += next_size * next_size
        get_order(next_size, row, column + next_size)
    elif r-row >= next_size and c-column < next_size:
        count += 2 * next_size * next_size
        get_order(next_size, row + next_size, column)
    elif r-row >= next_size and c-column >= next_size:
        count += 3 * next_size * next_size
        get_order(next_size, row + next_size, column + next_size)


n, r, c = map(int, input().split())
count = 0
get_order(2 ** n, 0, 0)
