import sys
input = sys.stdin.readline


def heap_push(h, x):
    h.append(x)
    i = len(h) - 1
    while i // 2 > 0:
        parent = i // 2
        if h[i] <= h[parent]:
            break
        h[i], h[parent] = h[parent], h[i]
        i = parent


def heap_pop(h):
    if len(h) == 1:
        return 0
    h[1], h[-1] = h[-1], h[1]
    value = h.pop()
    sort_heap(h)
    return value


def sort_heap(h):
    i = 1
    while i * 2 < len(h):
        lc, rc = i * 2, (i * 2 + 1 if i * 2 + 1 < len(h) else None)
        mc = rc if rc and h[rc] > h[lc] else lc
        if h[i] >= h[mc]:
            break
        h[i], h[mc] = h[mc], h[i]
        i = mc


n = int(input())
h = [None]
answer = []
for i in range(n):
    x = int(input())
    if x == 0:
        answer.append(heap_pop(h))
    else:
        heap_push(h, x)
for i in answer:
    print(i)
