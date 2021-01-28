from math import ceil

numbers = [0] * 10
count_6, count_9 = 0, 0
room_number = list(map(int, list(input())))

for i in room_number:
    if i == 6:
        count_6 += 1
    elif i == 9:
        count_9 += 1
    else:
        numbers[i] += 1

numbers.append(ceil((count_6 + count_9) / 2))
print(max(numbers))
