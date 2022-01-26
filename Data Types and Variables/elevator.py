import math

person = int(input())
capacity_elevator = int(input())
courses = math.ceil(person / capacity_elevator)
print(courses)