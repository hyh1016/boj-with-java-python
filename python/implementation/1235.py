from sys import stdin

n = int(stdin.readline())
student_numbers = [stdin.readline().rstrip() for i in range(n)]

for i in range(len(student_numbers[0])):
    numbers = [0] * n
    for j in range(n):
        numbers[j] = student_numbers[j][-1-i:]
    if len(set(numbers)) == len(numbers):
        print(i + 1)
        break
