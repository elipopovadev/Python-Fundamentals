num1 = int(input())
num2 = int(input())
num3 = int(input())

def sum_numbers(num1, num2):
    sum = num1 + num2
    return sum

def subtract(sum, num3):
    result = sum - num3
    return result

def add_and_subtract(num1, num2, num3):
    sum = sum_numbers(num1, num2)
    print(subtract(sum, num3))
    
 
add_and_subtract(num1, num2, num3)
