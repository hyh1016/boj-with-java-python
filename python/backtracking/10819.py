import sys
input = sys.stdin.readline


def get_max(A, prev, total):
    global result
    if not A:
        result = max(result, total)
        return
    for i in range(len(A)):
        current = A.pop(i)
        get_max(A, current, total+abs(prev-current))
        A.insert(i, current)


N = int(input())
A = list(map(int, input().split()))
result = 0
for i in range(len(A)):
    prev = A.pop(i)
    get_max(A, prev, 0)
    A.insert(i, prev)
print(result)
