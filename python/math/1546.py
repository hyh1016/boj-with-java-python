from sys import stdin

N = int(stdin.readline())
scores = list(map(int, stdin.readline().split()))
max_score = max(scores)

sum_result = 0
for i in scores:
    sum_result += (i / max_score) * 100
print(sum_result / N)
