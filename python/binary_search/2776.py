from sys import stdin
input = stdin.readline


def binary_search(array, target):
    start, end = 0, len(array) - 1
    while start <= end:
        middle = (start + end) // 2
        if target > array[middle]:
            start = middle + 1
        elif target < array[middle]:
            end = middle - 1
        else:
            return True
    return False


t = int(input())
for i in range(t):
    n = int(input())
    note1 = list(map(int, input().split()))
    m = int(input())
    note2 = list(map(int, input().split()))
    note1.sort()
    for i in note2:
        print(1) if binary_search(note1, i) else print(0)
