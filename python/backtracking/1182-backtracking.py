import sys
input = sys.stdin.readline
sys.setrecursionlimit(15000)


def set_count(data, i, selected, total_sum):
    global count
    if i == n:
        if selected > 0 and total_sum == s:
            count += 1
        return
    set_count(data, i+1, selected+1, total_sum+data[i])
    set_count(data, i+1, selected, total_sum)


n, s = map(int, input().split())
data = list(map(int, input().split()))
count = 0
set_count(data, 0, 0, 0)
print(count)
