import sys
input = sys.stdin.readline
sys.setrecursionlimit(15000)


def backtracking(numbers):
    if len(numbers) == m:
        print(' '.join(map(str, numbers)))
        return
    for i in data:
        if i in numbers:
            continue
        numbers.append(i)
        backtracking(numbers)
        numbers.pop()


n, m = map(int, input().split())
data = sorted(list(map(int, input().split())))
for i in data:
    backtracking([i])
