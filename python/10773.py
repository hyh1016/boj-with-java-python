from sys import stdin

n = int(stdin.readline())
total_money = []
for i in range(n):
    money = int(stdin.readline())
    if money == 0:
        total_money.pop()
    else:
        total_money.append(money)
print(sum(total_money))
