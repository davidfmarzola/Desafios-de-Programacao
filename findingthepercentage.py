student_marks = {} # dicionario
for _ in range(int(input())):
    name, *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores
       
query_name = input()
media = "{:.2f}".format(sum(student_marks[query_name])/len(student_marks[query_name]))
print(media)