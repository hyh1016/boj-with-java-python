def get_computer_number(a, b):
    a = a % 10
    if a == 0:
        return 10
    if a == 1 or a == 5 or a == 6:
        return a
    if a == 4 or a == 9:
        b = (b % 2) if (b % 2) else 2
        return pow(a, b) % 10
    if a == 2 or a == 3 or a == 7 or a == 8:
        b = (b % 4) if (b % 4) else 4
        return pow(a, b) % 10


T = int(input())
result = []
for i in range(T):
    a, b = list(map(int, input().split(' ')))
    print(get_computer_number(a, b))
