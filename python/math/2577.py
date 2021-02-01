repeat = 3
A, B, C = [int(input()) for i in range(repeat)]
sum_result = A * B * C
numbers = [0] * 10
for number in str(sum_result):
    numbers[int(number)] += 1
for i in numbers:
    print(i)
