text = input().split(", ")
numbers = list(map(int, text))
positive = [num for num in numbers if num >= 0]
negative = [num for num in numbers if num < 0]
even = [num for num in numbers if num % 2 == 0]
odd = [num for num in numbers if num % 2 != 0]

positive_result = ", ".join(map(str, positive))
negative_result = ", ".join(map(str, negative))
even_result = ", ".join(map(str, even))
odd_result = ", ".join(map(str, odd))

print(f"Positive: {positive_result}")
print(f"Negative: {negative_result}")
print(f"Even: {even_result}")
print(f"Odd: {odd_result}")
