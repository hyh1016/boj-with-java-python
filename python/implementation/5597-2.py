import sys
input = sys.stdin.readline

students = set(range(1, 31))
for i in range(28):
    students.remove(int(input()))
for i in sorted(students):
    print(i)
