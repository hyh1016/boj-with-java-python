import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
breaked = set(input().split())
_max = abs(n-100)
count = 0
for i in range(_max):
    if n-i >= 0 and len(set(str(n-i)) & breaked) == 0:
        count += len(str(n-i))
        break
    if len(set(str(n+i)) & breaked) == 0:
        count += len(str(n+i))
        break
    count += 1
print(min(_max, count))
