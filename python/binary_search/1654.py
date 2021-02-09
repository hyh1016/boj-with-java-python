from sys import stdin
input = stdin.readline


def get_optimal_value(values, target):
    start, end = 1, max(values)
    result = 0
    while start <= end:
        middle = (start + end) // 2
        total_sum = sum([(v // middle) for v in values])
        if total_sum < target:
            end = middle - 1
        else:
            result = middle
            start = middle + 1
    return result


k, n = map(int, input().split())
lengths = [int(input()) for i in range(k)]
print(get_optimal_value(lengths, n))
