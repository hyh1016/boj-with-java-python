from sys import stdin

C = int(stdin.readline())
for i in range(C):
    case = list(map(int, stdin.readline().split()))
    N, scores = case[0], case[1:]
    average = sum(scores) / N
    above_student = 0
    for i in scores:
        if i > average:
            above_student += 1
    print(format(above_student / N, ".3%"))
