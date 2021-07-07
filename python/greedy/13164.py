import sys
input = sys.stdin.readline

n, k = map(int, input().split())
data = list(map(int, input().split()))
diff = [data[i+1]-data[i] for i in range(n-1)]
print(sum(sorted(diff, reverse=True)[k-1:]))
