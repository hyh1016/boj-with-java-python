import sys
input = sys.stdin.readline
sys.setrecursionlimit(15000)


def backtracking(numbers):
    if len(numbers) == m:
        print(' '.join(map(str, numbers)))
        return
    for new in range(numbers[-1]+1, n+1):
        numbers.append(new)
        backtracking(numbers)
        numbers.pop()


n, m = map(int, input().split())
for i in range(1, n+1):
    backtracking([i])
