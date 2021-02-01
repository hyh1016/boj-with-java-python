from sys import stdin

s = list(stdin.readline().rstrip())
count = {'0': 0, '1': 0}

for i in range(len(s) - 1):
    if s[i] != s[i + 1]:
        count[s[i]] += 1
count[s[-1]] += 1
print(min(count.values()))
