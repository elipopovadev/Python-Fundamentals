university = {}
line = input().split(" : ")
while line != ["end"]:
    course = line[0]
    student = line[1]
    if course not in university:
        university[course] = []
        university[course].append(student)
    else:
        university[course].append(student)
    
    line = input().split(" : ")

sorted_univeristy = dict(sorted(university.items(), key = lambda x: -len(x[1])))
for course_name, students in sorted_univeristy.items():
    print (f"{course_name}: {len(students)}")
    sorted_students = sorted(students)
    for student in sorted_students:
        print(f"-- {student}")
    