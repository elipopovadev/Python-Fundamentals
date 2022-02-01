numbers = input().split(", ")

def check_palindrome(numbers):
    for num in numbers:
        reverse_number = num[::-1]
        if num == reverse_number:
           print(True)
        else:
            print(False)

check_palindrome(numbers)