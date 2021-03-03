import sys
input = sys.stdin.readline

n, m = map(int, input().split())
pocketmon = {}
for i in range(1, n + 1):
    name = input().rstrip()
    pocketmon[name] = i
names = list(pocketmon.keys())
answer = []
for i in range(m):
    question = input().rstrip()
    if question.isdigit():
        answer.append(names[int(question) - 1])
    else:
        answer.append(pocketmon[question])
for i in answer:
    print(i)
