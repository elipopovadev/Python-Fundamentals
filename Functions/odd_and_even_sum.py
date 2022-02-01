number_string = input()

def return_odd_and_even_sum(number_string):
    odd_sum = 0
    even_sum = 0
    for char in number_string:
        char_digit = int(char)
        if char_digit % 2 != 0:
            odd_sum += char_digit
        else:
            even_sum += char_digit
    
    result = f"Odd sum = {odd_sum}, Even sum = {even_sum}"
    return result

print(return_odd_and_even_sum(number_string))