repeat = 28
student_numbers = [int(input()) for i in range(repeat)]

# 1: assign True - 28776KB, 68ms
submit_students = [False] * 30
for student_number in student_numbers:
    submit_students[student_number - 1] = True
first_student = submit_students.index(False) + 1
second_student = submit_students.index(False, first_student) + 1
print(first_student)
print(second_student)

# 2: remove number - 28776KB, 64ms ✔
all_students = list(range(1, 31))
for student_number in student_numbers:
    all_students.remove(student_number)
print(all_students[0])
print(all_students[1])
