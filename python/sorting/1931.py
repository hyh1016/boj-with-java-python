import sys
input = sys.stdin.readline

n = int(input())
meeting = [0] * n
for i in range(n):
    start, end = map(int, input().split())
    meeting[i] = (start, end)
meeting.sort()

count = 0
start_time, end_time = 0, 0
for i in meeting:
    if i[0] >= end_time:
        count += 1
        start_time, end_time = i[0], i[1]
    elif i[0] >= start_time and i[1] <= end_time:
        start_time, end_time = i[0], i[1]
print(count)
