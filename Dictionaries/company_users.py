register = {}
line = input().split(" -> ")
while line != ["End"]:
    company_name = line[0]
    employee_Id = line [1]
    if company_name not in register:
        register[company_name] = []
        register[company_name].append(employee_Id)
    elif company_name in register and employee_Id not in register[company_name]:
         register[company_name].append(employee_Id)
    elif company_name in register and employee_Id in register[company_name]:
         pass
     
    line = input().split(" -> ")

sorted_register = dict(sorted(register.items(), key = lambda x: x[0]))
for company_name, employees in sorted_register.items():
    print(company_name)
    for employee_Id in employees:
        print(f"-- {employee_Id}")
    