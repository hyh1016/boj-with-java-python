from sys import stdin

n = int(stdin.readline())
times = list(map(int, stdin.readline().split()))
times.sort()
result = 0
for i in range(0, len(times)):
    result += times[i] * (len(times) - i)
print(result)
