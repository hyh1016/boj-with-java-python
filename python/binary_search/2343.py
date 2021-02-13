from sys import stdin
input = stdin.readline


def get_optimal_value(array, target):
    start, end = max(array), sum(array)
    while start <= end:
        middle = (start + end) // 2
        bluray_number = get_bluray_number(array, middle)
        if bluray_number > target:
            start = middle + 1
        else:
            end = middle - 1
    return start


def get_bluray_number(array, length):
    sum_length = 0
    count = 0
    for i in array:
        if sum_length + i > length:
            count += 1
            sum_length = 0
        sum_length += i
    count += 1
    return count


n, m = map(int, input().split())
lessons = list(map(int, input().split()))
print(get_optimal_value(lessons, m))
