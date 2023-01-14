from collections import namedtuple

n = int(input())
columns = input().split()
Students = namedtuple('Students', columns)
average = 0
for i in range(n):
    MARKS, CLASS, NAME, ID = input().split()
    student = Students(MARKS, CLASS, NAME, ID)
    average += int(student.MARKS)
print(average/n)
