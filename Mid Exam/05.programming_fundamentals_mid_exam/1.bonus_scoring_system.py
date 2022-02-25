number_students = int(input())
total_count_lectures = int(input())
additional_bonus = int(input())

bonus_student_attendances = {}
for i in range(0, number_students):
    student_attendances = int(input())
    bonus = round(student_attendances / total_count_lectures * (5 + additional_bonus))
    bonus_student_attendances[bonus] = student_attendances
    
max_bonus = max(bonus_student_attendances.keys())
lectures_for_student = str(bonus_student_attendances[max_bonus])
print(f'Max Bonus: {max_bonus}.')
print(f'The student has attended {lectures_for_student} lectures.')

