from sys import stdin

while True:
    numbers = list(stdin.readline())[:-1]
    if numbers[0] == '0':
        break
    result = 1
    for number in numbers:
        result += (3 if number == '1' else 5 if number == '0' else 4)
    print(result)
