from sys import stdin

station = 4
total_numbers = [0] * station
for i in range(station):
    out_number, in_number = list(map(int, stdin.readline().split()))
    total_numbers[i] = (in_number - out_number)
    if i:
        total_numbers[i] += total_numbers[i-1]
print(max(total_numbers))
