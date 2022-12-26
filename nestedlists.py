
def nestedlist():
    students = []
    for j in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])
    return students

def orderedlist(studentsmatrix):
    grades = []
    for j in range(len(studentsmatrix)):
        grades.append(studentsmatrix[j][1])
    grades = sorted(grades)
    return grades

def nameofstudentswithsecondlowestgrade(studentsmatrix, secondlowervalue):
    liststudentssecondlowestgrade = []
    for i in range(len(studentsmatrix)):
        if studentsmatrix[i][1] == secondlowervalue:
            liststudentssecondlowestgrade.append(studentsmatrix[i][0])
            liststudentssecondlowestgrade = sorted(liststudentssecondlowestgrade)
    print('\n'.join(map(str, liststudentssecondlowestgrade)))

studentsmatrix = nestedlist()
listadenotasordenadas = orderedlist(studentsmatrix)
secondlowervalue = listadenotasordenadas[1]
nameofstudentswithsecondlowestgrade(studentsmatrix, secondlowervalue)
