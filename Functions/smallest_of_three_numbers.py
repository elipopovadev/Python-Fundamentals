num1 = int(input())
num2 = int(input())
num3 = int(input())

def find_min_num (num1, num2, num3):
    minNum = min(num1, num2, num3)
    return minNum

print(find_min_num (num1, num2, num3))
