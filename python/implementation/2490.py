from sys import stdin

input_number = 3
for i in range(input_number):
    result = list(stdin.readline().split())
    number_of_0 = result.count('0')
    if number_of_0 == 1:
        print('A')
    elif number_of_0 == 2:
        print('B')
    elif number_of_0 == 3:
        print('C')
    elif number_of_0 == 4:
        print('D')
    else:
        print('E')
