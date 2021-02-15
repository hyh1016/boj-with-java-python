import sys
input = sys.stdin.readline


def get_optimal_value(x, y):
    z = int((100 * y) / x)
    if z >= 99:
        return -1
    start, end = 1, x
    result = 0
    while start <= end:
        middle = (start + end) // 2
        new_z = int((100 * (y + middle)) / (x + middle))
        if new_z > z:
            result = middle
            end = middle - 1
        else:
            start = middle + 1
    return result


x, y = map(int, input().split())
print(get_optimal_value(x, y))
