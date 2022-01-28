from statistics import mean

university = {}
number_row = int(input())

for i in range(number_row):
    student = input()
    grade = float(input())
    
    if student not in university:
        university[student] = []
        university[student].append(grade)
    else:
        university[student].append(grade)

sorted_dict = dict(sorted(university.items(), key = lambda x:  -mean(x[1])))
for student, grades in sorted_dict.items():
    if mean(grades) >= 4.50:
        average_grade = mean(grades)
        print(f"{student} -> {average_grade:.2f}")
        