import sys
input = sys.stdin.readline


def get_total_number(array, max_distance):
    current = array[0]
    count = 1
    for i in array:
        if i - current >= max_distance:
            count += 1
            current = i
    return count


def get_optimal_distance(array, target):
    start, end = 1, array[-1] - array[0]
    result = 0
    while start <= end:
        middle = (start + end) // 2
        total = get_total_number(array, middle)
        if total >= target:
            result = middle
            start = middle + 1
        elif total < target:
            end = middle - 1
    return result


n, c = map(int, input().split())
data = sorted([int(input()) for _ in range(n)])
print(get_optimal_distance(data, c))
