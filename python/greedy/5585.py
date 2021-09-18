import sys
input = sys.stdin.readline

return_money = 1000 - int(input())
count = 0
for i in [500, 100, 50, 10, 5, 1]:
    if return_money // i == 0:
        continue
    count += return_money // i
    return_money = return_money % i
    if return_money == 0:
        break
print(count)
