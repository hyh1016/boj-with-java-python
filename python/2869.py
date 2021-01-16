from math import ceil

up, down, total_length = list(map(int, input().split()))
day = ceil((total_length - down) / (up - down))
print(day)
