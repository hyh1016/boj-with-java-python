import sys
input = sys.stdin.readline


def heappush(array, value):
    array.append(value)
    i = len(array) - 1
    while i > 1:
        parent = int(i/2)
        if array[parent] <= array[i]:
            break
        array[parent], array[i] = array[i], array[parent]
        i = parent


def heappop(array):
    if len(array) == 1:
        return 0
    array[1], array[-1] = array[-1], array[1]
    value = array.pop()
    sort_heap(array)
    return value


def sort_heap(array):
    i = 1
    while i * 2 < len(array):
        left_child = i * 2
        right_child = (i * 2 + 1) if (i * 2 + 1) < len(array) else None
        min_child = right_child if right_child and array[right_child] < array[left_child] else left_child
        if array[min_child] >= array[i]:
            break
        array[min_child], array[i] = array[i], array[min_child]
        i = min_child


n = int(input())
data = [None]
answer = []
for i in range(n):
    x = int(input())
    if x == 0:
        answer.append(heappop(data))
    else:
        heappush(data, x)
for i in answer:
    print(i)
