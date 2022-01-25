year = input()

while len(set(str(year))) != len(year):
    int_year = int(year)
    int_year += 1
    year = str(int_year)
print(year)