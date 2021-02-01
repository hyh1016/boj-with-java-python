n, k = map(int, input().split())

for i in range(k):
    max_water = 1
    while True:
        new_water = max_water * 2
        if new_water > n:
            break
        max_water = new_water
    if max_water == n:
        print(0)
        break
    if i == k - 1:
        print(new_water - n)
    n -= max_water
