number = input()
if len(number) == 1:
    number = '0' + number
cycle = 0
new_number = number
while True:
    new_number = new_number[1] + \
        str(int(new_number[0]) + int(new_number[1]))[-1]
    cycle += 1
    if new_number == number:
        break
print(cycle)
