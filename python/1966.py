from sys import stdin

case = int(stdin.readline())
for i in range(case):
    n, target = map(int, stdin.readline().split())
    importances = list(map(int, stdin.readline().split()))

    count = 1
    while True:
        if len(importances) == 1:
            print(count)
            break
        current = importances[0]
        importances = importances[1:]
        if current >= max(importances):
            if target == 0:
                print(count)
                break
            count += 1
        else:
            importances += [current]
        target = len(importances) - 1 if target == 0 else target - 1
