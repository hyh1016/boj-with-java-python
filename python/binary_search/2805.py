def get_optimal_value(array, target, start, end):
    result = 0
    while start <= end:
        middle = (start + end) // 2
        total_sum = sum([i - middle for i in array if i > middle])
        if target > total_sum:
            end = middle - 1
        elif target < total_sum:
            result = middle
            start = middle + 1
        else:
            return middle
    return result


n, m = map(int, input().split())
heights = list(map(int, input().split()))
print(get_optimal_value(heights, m, 0, max(heights)))
