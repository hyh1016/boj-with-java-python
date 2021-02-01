from sys import stdin


def is_equal(num_list):
    value = num_list[0]
    for i in num_list[1:]:
        if value != i:
            return False
    return True


def solution():
    n, m = map(int, stdin.readline().split())
    rectangle = [list(stdin.readline().rstrip()) for i in range(n)]
    for i in range(min(n, m) - 1, 0, -1):
        for row in range(0, n - i):
            for column in range(0, m - i):
                if is_equal([rectangle[row][column], rectangle[row + i][column], rectangle[row][column + i], rectangle[row + i][column + i]]):
                    print((i + 1) ** 2)
                    return
    print(1)


solution()
