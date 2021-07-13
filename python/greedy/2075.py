import sys
input = sys.stdin.readline

n = int(input())
array = list(map(int, input().split()))
for i in range(n-1):
    row = map(int, input().split())
    array.extend(row)
    array.sort()
    array = array[n:]
print(array[0])
