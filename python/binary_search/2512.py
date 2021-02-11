from sys import stdin
input = stdin.readline


def get_optimal_value(array, target):
    start, end = 0, array[-1]
    result = 0
    while start <= end:
        middle = (start + end) // 2
        total_sum = sum([i if i <= middle else middle for i in array])
        if total_sum > target:
            end = middle - 1
        elif total_sum < target:
            result = middle
            start = middle + 1
        else:
            return middle
    return result


n = int(input())
values = sorted(list(map(int, input().split())))
m = int(input())

if m >= sum(values):
    print(values[-1])
else:
    value = get_optimal_value(values, m)
    print(value)
