import sys
input = sys.stdin.readline
sys.setrecursionlimit(15000)


def backtracking(i, total):
    if len(total) == m:
        print(' '.join(map(str, total)))
        return
    if i > n:
        return
    total.append(i)
    backtracking(i, total)
    total.pop()
    backtracking(i+1, total)


n, m = map(int, input().split())
backtracking(1, [])
