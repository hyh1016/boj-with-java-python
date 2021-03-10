from collections import Counter

for i in range(int(input())):
    count = Counter([input().split()[1] for _ in range(int(input()))])
    result = 1
    for i in count.values():
        result *= (i + 1)
    print(result - 1)
